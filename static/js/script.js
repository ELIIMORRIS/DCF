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
