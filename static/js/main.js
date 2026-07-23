document.addEventListener('DOMContentLoaded', function () {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 5000);
    });

    // Confirm before submitting job application
    const applyForm = document.querySelector('form[enctype="multipart/form-data"]');
    if (applyForm && window.location.pathname.includes('/apply/')) {
        applyForm.addEventListener('submit', function (e) {
            const coverLetter = document.querySelector('#id_cover_letter');
            if (coverLetter && coverLetter.value.trim().length < 20) {
                e.preventDefault();
                alert('Please write a cover letter with at least 20 characters.');
            }
        });
    }
});
