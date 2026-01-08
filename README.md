<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>AI Website Generator using LangChain, Google Gemini & Streamlit</h1>

<div class="box">
    <h2>📌 Repository Description</h2>
    <p>
        An AI-powered Streamlit application that generates complete frontend websites using HTML, CSS, and JavaScript from a single prompt. Built with LangChain and Google Gemini, it allows users to instantly create and download production-ready website code.
    </p>
</div>

<div class="box">
    <h2>🚀 Project Overview</h2>
    <p>
        This project enables users to generate a fully functional frontend website by simply describing their idea in natural language.
        Using LangChain’s <strong>ChatGoogleGenerativeAI</strong> model and a <strong>Streamlit</strong> interface, the application:
    </p>
    <ul>
        <li>Accepts a user prompt describing a website</li>
        <li>Generates clean HTML, CSS, and JavaScript code</li>
        <li>Automatically packages the files into a downloadable ZIP</li>
    </ul>
</div>

<div class="box">
    <h2>🛠️ Tech Stack</h2>
    <ul>
        <li>Python</li>
        <li>Streamlit</li>
        <li>LangChain</li>
        <li>Google Gemini (ChatGoogleGenerativeAI)</li>
        <li>HTML, CSS, JavaScript</li>
        <li>dotenv</li>
    </ul>
</div>

<div class="box">
    <h2>📂 Project Structure</h2>
    <pre>
AI-Website-Generator/
│
├── files/
│   ├── app.py          # Main Streamlit application
│   ├── structure.py    # Application structure & logic
│   ├── .env            # API key storage
│   ├── req.txt         # Project dependencies
│
├── README.html

  </pre>
</div>

<div class="box">
    <h2>⚙️ Virtual Environment Setup</h2>
    <h3>Create Virtual Environment</h3>
    <pre>python -m venv venv</pre>

  <h3>Activate Virtual Environment</h3>
    <pre>
Windows:
venv\Scripts\activate

Mac / Linux:
source venv/bin/activate
    </pre>
</div>

<div class="box">
    <h2>📦 Install Dependencies</h2>
    <p>Navigate to the <strong>files</strong> folder and run:</p>
    <pre>pip install -r req.txt</pre>
</div>

<div class="box">
    <h2>🔑 Environment Variable Setup</h2>
    <p>Create a <code>.env</code> file inside the <strong>files</strong> folder:</p>
    <pre>GEMINI=your_google_gemini_api_key</pre>
</div>

<div class="box">
    <h2>▶️ Running the Application</h2>
    <pre>streamlit run app.py</pre>
    <p>The application will open automatically in your browser.</p>
</div>

<div class="box">
    <h2>🧠 How the Application Works</h2>
    <ol>
        <li>User enters a website idea in the Streamlit interface</li>
        <li>Clicks the <strong>Generate</strong> button</li>
        <li>LangChain sends the prompt to Google Gemini</li>
        <li>The AI generates HTML, CSS, and JavaScript</li>
        <li>Files are zipped and ready for download</li>
    </ol>
</div>

<div class="box">
    <h2>📌 Key Features</h2>
    <ul>
        <li>Prompt-based website generation</li>
        <li>Strictly structured HTML, CSS, and JS output</li>
        <li>Instant ZIP download</li>
        <li>Secure API handling using dotenv</li>
        <li>Production-ready frontend code</li>
    </ul>
</div>

<div class="box">
    <h2>📈 Use Cases</h2>
    <ul>
        <li>Rapid website prototyping</li>
        <li>Frontend learning projects</li>
        <li>Hackathons & demos</li>
        <li>Portfolio projects</li>
        <li>AI automation tools</li>
    </ul>
</div>

<footer>
    <p>✨ Build websites faster with AI-powered automation</p>
</footer>

</body>
</html>
