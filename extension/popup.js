const messageContainer = document.getElementById("message-container");
const userInput = document.getElementById("user-input");
const sendChat = document.getElementById("send-chat");
const sendPageButton = document.getElementById("send-page");
const analyzeButton = document.getElementById("analyze");


sendPageButton.onclick = async function (e) {
    let queryOptions = { active: true, currentWindow: true };
    await chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {   
        chrome.tabs.sendMessage(tabs[0].id, { color: "green" }, function (doc) {
            chrome.runtime.sendMessage({ action: "sendpage", message: doc['doc'] }, function (response) {
                if (response) {
                    messageContainer.innerHTML += `<p><strong>Server response:</strong> ${response.reply}</p>`;
                }
            })
        })
    });
};

document.addEventListener("DOMContentLoaded", function () {
    sendChat.addEventListener("click", function () {
        const message = userInput.value.trim();
       //var message = document.documentElement.innerHTML;
        if (message !== "") {
            messageContainer.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
            userInput.value = "";
            sendMessage(message);
        }
    });

    userInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendChat.click();
        }
    });

    function sendMessage(message) {
        chrome.runtime.sendMessage({ action: 'openpanel' });
         chrome.runtime.sendMessage({ action: "sendchat", message }, function (response) {
             if (response) {
                messageContainer.innerHTML += `<p><strong>Server response:</strong> ${response.reply}</p>`;
            }
        });
    }

    analyzeButton.addEventListener("click", function () {
        chrome.runtime.sendMessage({ action: "analyze" }, function (response) {
            if (response) {
                messageContainer.innerHTML = `<p>${response.reply}</p>`;
            }
        });
    });


});
