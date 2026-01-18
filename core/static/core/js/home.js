// Handle form submission and optional animations
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');

    if (form) {
        form.addEventListener('submit', () => {
            const button = form.querySelector('button');
            if (button) {
                button.disabled = true;
                button.textContent = 'Sending...';
            }
        });
    }
});
