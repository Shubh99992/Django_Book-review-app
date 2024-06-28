document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.getElementById("sidebar");
    const content = document.getElementById("content");
    const hamburger = document.getElementById("hamburger");

    hamburger.addEventListener("click", function() {
        sidebar.classList.toggle("collapsed");
        content.classList.toggle("collapsed");
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const collapsibleHeaders = document.querySelectorAll(".collapsible-header");

    collapsibleHeaders.forEach(header => {
        header.addEventListener("click", function() {
            this.classList.toggle("active");
            const content = this.nextElementSibling;
            if (content.style.display === "block") {
                content.style.display = "none";
                content.style.maxHeight = "0";
            } else {
                content.style.display = "block";
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });
});
