document.addEventListener("DOMContentLoaded", function() {
    // initialize tooltips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    tooltipTriggerList.forEach(el => new bootstrap.Tooltip(el));

    // Check completion status for 'spreadsheet_formulae'
    checkCompletionStatus('spreadsheet_formulae');

    // Check completion status for the current page ID, if available
    const pageId = document.body.getAttribute('data-page-id');
    if (pageId) {
        checkCompletionStatus(pageId);
    }
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

function showImage(imageUrl) {
    // Update the source of the zoomed image
    document.getElementById('zoomedImage').src = imageUrl;
  }

// Select elements
const steps = document.querySelectorAll('.step'); // Initial step elements
const stepsContainer = document.getElementById('steps'); // Original container
const dropzone = document.getElementById('dropzone'); // Dropzone container
const checkOrderButton = document.getElementById('checkOrder'); // Check button
const resetButton = document.getElementById('resetGame'); // Reset button
const result = document.getElementById('result'); // Result display

// Track the order of steps dropped
let droppedSteps = [];

// Enable dragging
steps.forEach(step => {
    step.addEventListener('dragstart', (e) => {
        e.dataTransfer.setData('text', e.target.id);
    });
});

// Allow dropping in the dropzone
dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
});

dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    const stepId = e.dataTransfer.getData('text');
    const stepElement = document.getElementById(stepId);

    // Add step to the dropzone if not already there
    if (!droppedSteps.includes(stepId)) {
        droppedSteps.push(stepId);
        dropzone.appendChild(stepElement);
    }
});

// Check the order
checkOrderButton.addEventListener('click', () => {
    const correctOrder = ['step1', 'step2', 'step3', 'step4'];

    if (JSON.stringify(droppedSteps) === JSON.stringify(correctOrder)) {
        result.textContent = 'Yes! You have brushed your teeth in the right order!';
        result.style.color = 'green';
    } else {
        result.textContent = 'Oops! Try again.';
        result.style.color = 'red';
    }
});

// Reset functionality
resetButton.addEventListener('click', () => {
    // Clear the dropzone
    dropzone.innerHTML = '<p>Drop steps here in order!</p>';
    
    // Move all step elements back to the original container
    steps.forEach(step => {
        stepsContainer.appendChild(step);
    });

    // Reset the droppedSteps array
    droppedSteps = [];

    // Clear the result message
    result.textContent = '';
});
