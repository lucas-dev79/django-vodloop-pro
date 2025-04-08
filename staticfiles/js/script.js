
    document.addEventListener('DOMContentLoaded', function () {
        const preloader = document.getElementById('preloader');
        const mainContent = document.getElementById('main-content');

        // Simulate content loading
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 1000); // Adjust the timeout as needed
    });
