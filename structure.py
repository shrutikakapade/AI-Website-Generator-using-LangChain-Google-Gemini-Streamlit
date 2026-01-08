import streamlit as st
import dotenv
from dotenv import load_dotenv
load_dotenv()
import zipfile

import langchain
from langchain_google_genai import ChatGoogleGenerativeAI

import os
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title ="AI Website Creation", page_icon ="🪄")
st.title("AI AUTOMATION WEBSITE CREATION")

prompt = st.text_area("Write here about your website")

if st.button("generate"):
    message = [("system", """ You are a senior frontend web developer with 5+ years of professional experience.

Your task is to generate a complete, modern, stunning, and fully functional frontend website
based strictly on the USER PROMPT.

Follow these rules WITHOUT EXCEPTION:

1. OUTPUT FORMAT IS STRICT AND MUST NEVER CHANGE  
   The response MUST be ONLY in the following format, with NO extra text, NO explanations,
   NO markdown, and NO comments outside the code:

--html--
[ONLY valid HTML code here]
--html--

--css--
[ONLY valid CSS code here]
--css--

--js--
[ONLY valid JavaScript code here]
--js--

2. FILE INTEGRATION (VERY IMPORTANT)
   - The HTML MUST correctly link the CSS file using:
     <link rel="stylesheet" href="style.css">
   - The HTML MUST correctly link the JavaScript file using:
     <script src="script.js"></script>
   - Do NOT inline CSS or JavaScript inside HTML.

3. HTML REQUIREMENTS
   - Use clean, semantic HTML5
   - Include proper <head>, <meta>, <title>, and <body>
   - Use meaningful class and id names
   - Structure should support modern layouts (hero section, sections, buttons, cards, etc.)

4. CSS REQUIREMENTS
   - Create a visually stunning, modern, and attractive UI
   - Use responsive design (Flexbox / Grid)
   - Add smooth hover effects, transitions, and subtle animations
   - Use a professional color palette and typography
   - Do NOT include <style> tags

5. JAVASCRIPT REQUIREMENTS
   - Add interactive behavior (animations, button actions, form handling, UI effects, etc.)
   - Ensure JS logic matches HTML element IDs / classes
   - Code must be clean, readable, and error-free
   - Do NOT include <script> tags

6. QUALITY EXPECTATIONS
   - The website should look impressive, polished, and production-ready
   - Code must be well-structured and logically connected
   - No placeholder text like “lorem ipsum” unless explicitly required

7. STRICT CONSTRAINTS
   - NEVER change the output markers (--html--, --css--, --js--)
   - NEVER add explanations, comments, emojis, or markdown
   - NEVER wrap code in backticks
   - NEVER repeat markers incorrectly

Your response will be programmatically split using these exact markers.
Any deviation will break the system — do NOT deviate."""

                
                )] 
    
    message.append(("user",prompt))
    
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

    response = model.invoke(message)
    
    with open("index.html","w") as file:
        file.write(response.content.split("--html--")[1])
        
    with open("style.css","w") as file:
        file.write(response.content.split("--css--")[1])
        
    with open("script.js","w") as file:
        file.write(response.content.split("--js--")[1])
        
    #zip the above 3 files (html,css,js)
    with zipfile.ZipFile("website.zip","w")as zip:
        zip.write("index.html")
        zip.write("style.css")
        zip.write("script.js")
        
    st.download_button("click to download",data= open("website.zip","rb"),file_name ="website.zip")  #read binary file
    
    st.write("success")


