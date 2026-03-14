document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('healthForm');
    const submitBtn = document.getElementById('submitBtn');
    const spinner = document.getElementById('spinner');
    const btnText = document.querySelector('.btn-text');
    const mainPanel = document.querySelector('.main-panel');
    const resultsSection = document.getElementById('resultsSection');
    const predictionBadge = document.getElementById('predictionBadge');
    const recommendationContent = document.getElementById('recommendationContent');
    const resetBtn = document.getElementById('resetBtn');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // UI state: loading
        btnText.textContent = 'Analyzing...';
        spinner.classList.remove('hidden');
        submitBtn.disabled = true;

        // Gather data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (!response.ok) {
                throw new Error(result.error || 'Prediction failed');
            }

            // Display Results
            showResults(result.prediction, result.recommendation);

        } catch (error) {
            alert("Error: " + error.message);
        } finally {
            // UI state: reset loading
            btnText.textContent = 'Analyze Pulse';
            spinner.classList.add('hidden');
            submitBtn.disabled = false;
        }
    });

    resetBtn.addEventListener('click', () => {
        resultsSection.classList.add('hidden');
        mainPanel.classList.remove('hidden');
        form.reset();
        
        // Remove animation class and add it back for proper reflow if we wanted a re-enter animation,
        // but simple toggle is okay enough here.
        mainPanel.style.animation = 'fadeInUp 0.6s ease forwards';
    });

    function showResults(prediction, recommendation) {
        // Hide form, show results
        mainPanel.classList.add('hidden');
        resultsSection.classList.remove('hidden');

        // Reset badge classes
        predictionBadge.className = 'prediction-badge';
        
        // Format class name (replace spaces with hyphens)
        const badgeClass = `badge-${prediction.replace(/\s+/g, '-')}`;
        predictionBadge.classList.add(badgeClass);
        
        predictionBadge.textContent = prediction;
        recommendationContent.textContent = recommendation;
    }
});
