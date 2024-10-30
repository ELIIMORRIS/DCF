document.querySelectorAll('.collapsible').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        button.classList.toggle('active');
        
        if (content.style.maxHeight) {
            content.style.maxHeight = null;  // Collapses the section
        } else {
            content.style.maxHeight = content.scrollHeight + "px";  // Expands the section smoothly
        }
    });
});

const items = document.querySelectorAll('.item');
const lists = document.querySelectorAll('.list');

items.forEach(item => {
    item.addEventListener('dragstart', dragStart);
    item.addEventListener('dragend', dragEnd);
});

lists.forEach(list => {
    list.addEventListener('dragover', dragOver);
    list.addEventListener('drop', drop);
});

function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.id);
    setTimeout(() => {
        e.target.classList.add('hide');
    }, 0);
}

function dragEnd(e) {
    e.target.classList.remove('hide');
}

function dragOver(e) {
    e.preventDefault();
}

function drop(e) {
    e.preventDefault();
    const id = e.dataTransfer.getData('text/plain');
    const draggable = document.getElementById(id);
    e.target.appendChild(draggable);
}
