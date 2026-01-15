import streamlit as st
import os
import zipfile
import io
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import time

# ---------- CONFIG ----------
load_dotenv()
GOOGLE_API_KEY = os.getenv("gemini")
if not GOOGLE_API_KEY:
    st.error("🚫**GOOGLE_API_KEY missing** in .env file")
    st.stop()

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

st.set_page_config(
    page_title="WebMint AI - Production Website Generator",
    page_icon="🪄",
    layout="wide",
)

# ---------- FIXED: GENERATE_WEBSITE FUNCTION MOVED TO TOP ----------
def generate_website(prompt_text):
    """Generate complete production website from prompt"""
    system_message = """You are a senior frontend engineer and UI/UX expert. 
Goal: Generate a complete, production-ready static website based ONLY on the user description. 
Requirements: 
- Use modern, semantic HTML5 structure (header, main, section, footer, etc.).
- Add clear sections: hero, features/benefits, call-to-action, and any additional sections explicitly requested. 
- Ensure the layout is responsive and mobile-friendly (flexbox or CSS grid, no frameworks). 
- Use clean, readable class names and consistent indentation. 
- Do NOT include inline CSS or inline JavaScript inside the HTML. 
Styling: 
- Provide all styling in a separate CSS file. 
- Use a modern look with good spacing, hierarchy, and accessible color contrast. 
- Use a simple Google Font (e.g., Inter, Poppins, or similar) imported in CSS. 
- Include hover states for buttons and links. 
- Respect any colors, branding, or style instructions from the user description.
- make the website impresive and attractive
- add a perfect images to the website make sure all images are modern and inpired by the topic and pick the impresive images to make website more impresive 
Behavior (JavaScript): 
- Only write vanilla JavaScript. 
- Add smooth scroll for internal navigation links if there is a navbar. 
- Add small, useful interactions if relevant (e.g., mobile nav toggle, simple animations, FAQ accordion). 
- Do NOT use external JS libraries or frameworks. 
Output format (strict):
Return your answer in EXACTLY this structure with no extra text, comments, or explanations:

--html--
HTML
--html--

--css--
CSS
--css--

--js--
JS
--js--"""

    try:
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        message = [("system", system_message), ("user", prompt_text)]
        response = model.invoke(message)
        
        content = response.content or ""
        
        html_parts = content.split("--html--")
        html = html_parts[1].strip() if len(html_parts) > 1 else ""
        
        css_parts = content.split("--css--")
        css = css_parts[1].strip() if len(css_parts) > 1 else ""
        
        js_parts = content.split("--js--")
        js = js_parts[1].strip() if len(js_parts) > 1 else ""
        
        # Auto-fix links
        if '<link rel="stylesheet" href="style.css">' not in html.lower():
            html = html.replace('</head>', '\n    <link rel="stylesheet" href="style.css">\n  </head>')
        if '<script src="script.js"' not in html.lower():
            html = html.replace('</body>', '\n    <script defer src="script.js"></script>\n  </body>')
            
        return html, css, js
        
    except Exception as e:
        st.error(f"Generation error: {str(e)}")
        return "", "", ""

# ---------- ENHANCED CSS - SMALL LEFT-ALIGNED BUTTONS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700;800&display=swap');

/* FULL PAGE GLOW HERO EFFECT */
* {margin:0;padding:0;box-sizing:border-box;}
body, .stApp { 
    background: 
        radial-gradient(ellipse 80% 50% at 20% 10%, rgba(139,69,19,0.4) 0%, transparent 50%),
        radial-gradient(ellipse 60% 40% at 80% 20%, rgba(218,165,32,0.3) 0%, transparent 50%),
        radial-gradient(circle at 50% 100%, rgba(10,7,3,0.95) 0%, #000 70%);
    background-attachment: fixed;
    color: #fdfbf7;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
}

/* GLOW HERO OVERLAY */
.glow-hero-overlay {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: 
        radial-gradient(circle 30% at 20% 20%, rgba(255,215,0,0.12) 0%, transparent 60%),
        radial-gradient(circle 25% at 80% 80%, rgba(255,140,0,0.1) 0%, transparent 60%);
    animation: goldShimmerFull 15s ease-in-out infinite;
    z-index: -1;
    pointer-events: none;
}

@keyframes goldShimmerFull {
    0%, 100% { opacity: 0.4; transform: rotate(0deg) scale(1); }
    33% { opacity: 0.7; transform: rotate(120deg) scale(1.02); }
    66% { opacity: 0.5; transform: rotate(240deg) scale(1.01); }
}

[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stStatusWidget"] {display: none !important;}

/* SMALL LEFT-ALIGNED BUTTONS - IDENTICAL STYLE */
.button-row {
    display: flex !important;
    gap: 1rem !important;
    align-items: center !important;
    justify-content: flex-start !important;
    margin-top: 2rem !important;
    padding: 1rem 0 !important;
    max-width: 400px !important;
}

.stButton > button {
    width: auto !important;
    height: 56px !important;
    min-width: 160px !important;
    background: linear-gradient(135deg, #ffd700 0%, #ff8c00 50%, #ff4500 100%) !important;
    border: none !important;
    border-radius: 20px !important;
    color: #1a0f05 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.95rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
    padding: 0 1.8rem !important;
    box-shadow: 
        0 20px 50px rgba(255,215,0,0.5),
        0 0 0 1px rgba(255,215,0,0.8),
        inset 0 1px 0 rgba(255,255,255,0.3) !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    backdrop-filter: blur(15px) !important;
    flex-shrink: 0 !important;
}

.stButton > button:hover {
    transform: translateY(-6px) scale(1.03) !important;
    box-shadow: 
        0 30px 70px rgba(255,215,0,0.7),
        0 0 30px rgba(255,215,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.4) !important;
}

/* DOWNLOAD BUTTON - EMERALD GREEN */
.download-epic .stButton > button {
    background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%) !important;
    box-shadow: 
        0 20px 50px rgba(16,185,129,0.5),
        0 0 0 1px rgba(16,185,129,0.8) !important;
}

.download-epic .stButton > button:hover {
    box-shadow: 
        0 30px 70px rgba(16,185,129,0.7),
        0 0 30px rgba(16,185,129,0.5) !important;
}

/* BUTTON SHIMMER */
.stButton > button::before {
    content: ''; 
    position: absolute; 
    top: 0; 
    left: -150%; 
    width: 150%; 
    height: 100%; 
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
    transition: left 0.6s;
}

.stButton > button:hover::before {
    left: 150%;
}

/* ALL OTHER STYLES */
.header-premium {display:flex;justify-content:space-between;align-items:center;margin-bottom:3.5rem;padding-bottom:2.5rem;border-bottom:2px solid rgba(218,165,32,0.3);}
.logo-epic {font-family:'Space Grotesk',sans-serif;font-size:clamp(1.8rem,5vw,2.6rem);font-weight:900;background:linear-gradient(135deg,#ffd700,#ffed4e,#ff8c00);-webkit-background-clip:text;background-clip:text;color:transparent;}
.status-elite {display:flex;align-items:center;gap:0.75rem;background:linear-gradient(135deg,rgba(255,215,0,0.25),rgba(255,140,0,0.2));border:2px solid rgba(255,215,0,0.5);border-radius:50px;padding:0.85rem 1.75rem;font-weight:700;font-size:1rem;backdrop-filter:blur(20px);}

h2.epic-title {font-family:'Space Grotesk',sans-serif;font-size:clamp(3.5rem,9vw,5.5rem);font-weight:950;line-height:1.05;margin:0 0 1.5rem 0;background:linear-gradient(135deg,#fdfbf7,#ffd700);-webkit-background-clip:text;background-clip:text;letter-spacing:-0.03em;}
.glow-highlight {background:linear-gradient(135deg,#ffd700,#ff8c00);-webkit-background-clip:text;background-clip:text;}
.subtitle-pro {font-size:clamp(1.2rem,3.5vw,1.6rem);color:#e8e3d7;line-height:1.8;max-width:1170px;margin-bottom:4rem;}

.stTextArea textarea {width:100% !important;min-height:260px !important;border:2px solid rgba(218,165,32,0.35) !important;border-radius:24px !important;background:rgba(8,6,4,0.92) !important;color:#fdfbf7 !important;font-family:'Inter',monospace !important;font-size:1.05rem !important;padding:1.8rem !important;line-height:1.7 !important;box-shadow:0 20px 60px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.12);}
.stTextArea textarea:focus {border-color:#ffd700 !important;box-shadow:0 0 0 5px rgba(255,215,0,0.25),0 30px 80px rgba(255,215,0,0.2) !important;transform:translateY(-4px);}

.success-epic {background:linear-gradient(145deg,rgba(34,197,94,0.25),rgba(16,185,29,0.18));border:3px solid rgba(34,197,94,0.6);border-radius:32px;padding:4rem;text-align:center;margin-top:3rem;box-shadow:0 40px 120px rgba(34,197,94,0.4);animation:pulse-glow 2s ease-in-out infinite;}
@keyframes pulse-glow {0%,100%{box-shadow:0 40px 120px rgba(34,197,94,0.4);}50%{box-shadow:0 40px 120px rgba(34,197,94,0.6),0 0 60px rgba(34,197,94,0.3);}}
</style>
""", unsafe_allow_html=True)

# ---------- FULL-PAGE GLOW HERO BACKGROUND LAYER ----------
st.markdown('<div class="glow-hero-overlay"></div>', unsafe_allow_html=True)

# ---------- YOUR ORIGINAL LAYOUT ----------
st.markdown("""
    <div class="header-premium">
        <div class="logo-epic">WebMint AI</div>
        <div class="status-elite">
            <span style="font-size:1.4em;">⚡</span>
            Enterprise Production Ready
        </div>
    </div>
    
    <h2 class="epic-title">
        From Prompt to <span class="glow-highlight">Website,</span><br>Simplified
    </h2>
    <p class="subtitle-pro">
        WebMint AI transforms natural language prompts into complete, responsive websites.
        Describe your idea once and receive structured HTML, modern CSS, and clean JavaScript designed with smooth interactions, refined visuals, and consistent performance across devices.
        Built to simplify website creation while maintaining modern design standards, WebMint AI helps you move from concept to implementation with clarity and precision.
    </p>
""", unsafe_allow_html=True)

prompt = st.text_area(
    "",
    placeholder="""Describe your vision.🪄
Outline the structure, visual direction, and experience you want. WebMint AI will intelligently translate your idea into a complete, responsive website.""",
    height=260,
    label_visibility="collapsed",
    key="website_prompt"
)

# ---------- SMALL LEFT-ALIGNED BUTTONS ROW ----------
st.markdown('<div class="button-row">', unsafe_allow_html=True)

# ✅ FIXED: Function is now defined BEFORE being called
if st.button("Generate Website🪄", key="generate", use_container_width=False):
    if prompt.strip():
        with st.spinner('🎨 Crafting your website'):
            time.sleep(1.5)
            
            html, css, js = generate_website(prompt)  # ✅ NOW DEFINED ABOVE
            
            if html and css and js:
                zip_buffer = io.BytesIO()
                with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
                    zf.writestr("index.html", html)
                    zf.writestr("style.css", css)
                    zf.writestr("script.js", js)
                
                zip_buffer.seek(0)
                
                # st.markdown("""
                # <div class="success-epic">
                #     <h2 style="font-size:3.5rem;color:#10b981;">✅ YOUR WEBSITE IS LIVE!</h2>
                #     <p style="font-size:1.4rem;">Production masterpiece ready for deployment 🚀</p>
                # </div>
                # """, unsafe_allow_html=True)
                st.markdown('<div class="button-row">', unsafe_allow_html=True)
                #st.markdown('<div class="button-row download-epic">', unsafe_allow_html=True)
                st.download_button(
                    "Download Instantly⭐",
                    data=zip_buffer.getvalue(),
                    file_name="production-website.zip",
                    mime="application/zip",
                    use_container_width=False,
                    key="download_epic"
                )
                st.markdown('</div>', unsafe_allow_html=True)
                
                
                #st.success("✨ Fully responsive • Cinematic animations • Production optimized")
            else:
                st.error("❌ Generation failed. Try a more specific prompt.")
    else:
        st.warning("✨ Enter your website vision first!")

st.markdown('</div>', unsafe_allow_html=True)  # button-row

# ---------- SPACER ----------
st.markdown("---")
