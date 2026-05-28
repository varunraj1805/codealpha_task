const quizData = [
    {
        question: "1. Which of the following URLs is a typical example of a phishing link?",
        answers: ["https://www.paypal.com", "https://www.paypa1.com/login", "https://support.google.com", "https://amazon.in"],
        correct: 1
    },
    {
        question: "2. An urgent email claims your bank account will be suspended in 24 hours unless you click a link. This technique is called:",
        answers: ["Technical Glitch", "Whaling", "Social Engineering (Urgency)", "Data Mining"],
        correct: 2
    },
    {
        question: "3. What should you always check before entering credentials on a website?",
        answers: ["The website's logo brightness", "The full URL domain name and HTTPS status", "The background color", "If the page loads fast"],
        correct: 1
    }
];

let currentQuestion = 0;
let score = 0;

function loadQuiz() {
    const qEl = document.getElementById("question");
    const buttons = document.querySelectorAll(".options .btn");
    
    document.getElementById("quiz").classList.remove("hide");
    document.getElementById("result").classList.add("hide");

    qEl.innerText = quizData[currentQuestion].question;
    buttons.forEach((btn, index) => {
        btn.innerText = quizData[currentQuestion].answers[index];
    });
}

function selectAnswer(index) {
    if (index === quizData[currentQuestion].correct) {
        score++;
    }
    currentQuestion++;
    if (currentQuestion < quizData.length) {
        loadQuiz();
    } else {
        showResults();
    }
}

function showResults() {
    document.getElementById("quiz").classList.add("hide");
    document.getElementById("result").classList.remove("hide");
    document.getElementById("score").innerText = `Your score: ${score} / ${quizData.length}`;
}

function restartQuiz() {
    currentQuestion = 0;
    score = 0;
    loadQuiz();
}

loadQuiz();