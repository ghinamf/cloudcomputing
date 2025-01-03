document.addEventListener("DOMContentLoaded", () => {
    const symptoms = [
        "Feeling nervous", "Panic attacks", "Breathing rapidly", "Sweating",
        "Trouble concentrating", "Trouble sleeping", "Trouble with work",
        "Hopelessness", "Anger", "Overreacting", "Change in eating habits",
        "Suicidal thoughts", "Feeling tired", "No close friends",
        "Social media addiction", "Weight gain", "Obsession with material possessions",
        "Introversion", "Stressful memories popping up", "Nightmares",
        "Avoiding people or activities", "Feeling negative", "Blaming yourself",
    ];

    const questionsContainer = document.getElementById("questions-container");

    symptoms.forEach((symptom, index) => {
        const questionContainer = document.createElement("div");
        questionContainer.classList.add("question-box");
        questionContainer.innerHTML = `
            <label>${symptom}?</label>
            <div>
                <input type="radio" name="symptom-${index}" value="1" required> Yes
                <input type="radio" name="symptom-${index}" value="0"> No
            </div>
        `;
        questionsContainer.appendChild(questionContainer);
    });

    document.getElementById("symptom-form").addEventListener("submit", async (event) => {
        event.preventDefault();
    
        // Collect form data
        const formData = new FormData(event.target);
        const symptoms = Array.from(formData.values()).map(value => parseInt(value));
    
        try {
            // Send the data to the backend
            const response = await fetch('/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ symptoms }), // Send JSON object
            });
    
            const result = await response.json();
            if (response.ok) {
                alert(`Your mental health prediction: ${result.prediction}`);
            } else {
                console.error(result.error);
                alert(`Error: ${result.error}`);
            }
        } catch (error) {
            console.error("Network error:", error);
            alert("Error submitting responses.");
        }
    });
    
});
