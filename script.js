document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to enhance the user experience
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(input => {
        input.addEventListener('input', function () {
            // Ensure the quantity is a positive integer
            const quantity = parseInt(this.value, 10);
            if (isNaN(quantity) || quantity <= 0) {
                this.value = 1;
            }
        });
    });
});
