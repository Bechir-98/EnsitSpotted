document.addEventListener("DOMContentLoaded", () => {
    const textarea = document.querySelector("textarea");
    const form = document.querySelector("form");
    const button = form?.querySelector("button");

    if (textarea) {
        textarea.addEventListener("input", () => {
            const value = textarea.value;

            // Detect Arabic characters
            const arabicRegex = /[\u0600-\u06FF]/;

            if (arabicRegex.test(value)) {
                textarea.style.direction = "rtl";
                textarea.style.textAlign = "right";
            } else {
                textarea.style.direction = "ltr";
                textarea.style.textAlign = "left";
            }
        });
    }

    if (form && button) {
        form.addEventListener("submit", () => {
            button.disabled = true;
            button.textContent = "Sending...";
        });
    }
});
