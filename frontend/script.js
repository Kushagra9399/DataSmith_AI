let sessionId = localStorage.getItem("session_id") || "";

const form = document.getElementById("upload-form");

const chatBox = document.getElementById("chat-box");

const textInput = document.getElementById("text-input");

const fileInput = document.getElementById("file-input");

const submitButton = document.querySelector("button");


// ---------- SUBMIT ----------
form.addEventListener("submit", async (e) => {

    e.preventDefault();

    if (submitButton.disabled) {
        return;
    }

    const text = textInput.value.trim();

    const file = fileInput.files[0];

    // ---------- VALIDATION ----------
    if (!text && !file) {

        addMessage(
            "bot",
            "Please enter text or upload a file."
        );

        return;
    }

    // ---------- USER MESSAGE ----------
    addMessage(
        "user",
        text || `Uploaded file: ${file.name}`
    );

    const formData = new FormData();

    formData.append("text", text);

    formData.append("session_id", sessionId);

    if (file) {
        formData.append("file", file);
    }

    // ---------- LOADING ----------
    startLoading();

    try {

        const response = await fetch(
            "http://127.0.0.1:8000/process",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        console.log(data);

        if (data.session_id) {

            sessionId = data.session_id;

            localStorage.setItem(
                "session_id",
                sessionId
            );
        }

        let botResponse = "";

        // ---------- FOLLOW-UP ----------
        if (data.follow_up_question) {

            botResponse = `
# Follow-Up Question

${data.follow_up_question}
            `;
        }

        // ---------- NORMAL RESPONSE ----------
        else {

            botResponse = `
# Intent
${data.intent}

# Result
${typeof data.result === "object"
    ? JSON.stringify(data.result, null, 2)
    : data.result
}
            `;
        }

        addMessage("bot", botResponse);

    } catch (error) {

        console.error(error);

        addMessage(
            "bot",
            `# Error\n${error.message}`
        );
    }

    stopLoading();
});


// ---------- START LOADING ----------
function startLoading() {

    submitButton.disabled = true;

    submitButton.innerText = "Processing...";

    textInput.disabled = true;

    fileInput.disabled = true;

    textInput.style.opacity = "0.7";

    fileInput.style.opacity = "0.7";
}


// ---------- STOP LOADING ----------
function stopLoading() {

    submitButton.disabled = false;

    submitButton.innerText = "Send";

    textInput.disabled = false;

    fileInput.disabled = false;

    textInput.style.opacity = "1";

    fileInput.style.opacity = "1";

    textInput.value = "";

    fileInput.value = "";
}


// ---------- ADD MESSAGE ----------
function addMessage(sender, text) {

    const div = document.createElement("div");

    div.classList.add("message");

    div.classList.add(sender);

    // ---------- MARKDOWN RENDER ----------
    div.innerHTML = marked.parse(text);

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}