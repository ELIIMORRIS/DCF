document.addEventListener("DOMContentLoaded", function(){
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })
  });
  

function markAsComplete(item) {
    localStorage.setItem(item, 'completed');
    const button = document.getElementById('btn-' + item);
    button.textContent = 'Completed';
    button.disabled = true;
}

function checkCompletionStatus(item) {
    const button = document.getElementById('btn-' + item);
    if (localStorage.getItem(item) === 'completed') {
        button.textContent = 'Completed';
        button.disabled = true;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    checkCompletionStatus('spreadsheet_formulae');
});

document.addEventListener('DOMContentLoaded', function() {
    const pageId = document.body.getAttribute('data-page-id');
    if (pageId) {
        checkCompletionStatus(pageId);
    }
});

function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
}

function drop(event) {
    event.preventDefault();
    const blockId = event.dataTransfer.getData("text");
    const block = document.getElementById(blockId).cloneNode(true);

    // Remove draggable attribute so it's only draggable from the library
    block.removeAttribute("draggable");

    // Append the cloned block to the editor area
    event.target.appendChild(block);
}

function runCode() {
    const editor = document.querySelector('.editor');
    const blocks = editor.querySelectorAll('.code-block');
    let output = "";

    blocks.forEach(block => {
        if (block.innerText.includes("print")) {
            output += block.innerText.replace("print(", "").replace(")", "") + "<br>";
        } else if (block.innerText.includes("x =")) {
            let x = 10;
            output += `Variable x set to ${x} <br>`;
        } else if (block.innerText.includes("y = x + 5")) {
            let y = 15;
            output += `Variable y calculated as x + 5 = ${y} <br>`;
        }
    });

    document.getElementById("output").innerHTML = output;
}

function clearCode() {
    const editor = document.querySelector('.editor');
    editor.innerHTML = "<h5>Drop Code Here</h5>"; // Reset the editor content
    document.getElementById("output").innerHTML = ""; // Clear the output area
}
