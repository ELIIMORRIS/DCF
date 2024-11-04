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

document.addEventListener("DOMContentLoaded", function() {
    // Function to decrement badge count
    function decrementBadge(badgeId) {
        const badge = document.getElementById(badgeId);
        let count = parseInt(badge.innerText);
        
        if (count > 0) {
            count--;
            badge.innerText = count;
            // Hide badge if count reaches 0
            if (count === 0) {
                badge.style.display = "none";
            }
        }
    }

    // Attach click event to links in Progression Step 2 tab
    document.querySelectorAll("#ps-step2 a").forEach(link => {
        link.addEventListener("click", function() {
            decrementBadge("ps-step2-badge");
        });
    });

    // Attach click event to links in Progression Step 3 tab
    document.querySelectorAll("#ps-step3 a").forEach(link => {
        link.addEventListener("click", function() {
            decrementBadge("ps-step3-badge");
        });
    });

    // Similarly, set up for Data Literacy tabs
    document.querySelectorAll("#dl-step2 a").forEach(link => {
        link.addEventListener("click", function() {
            decrementBadge("dl-step2-badge");
        });
    });
    document.querySelectorAll("#dl-step3 a").forEach(link => {
        link.addEventListener("click", function() {
            decrementBadge("dl-step3-badge");
        });
    });
});
