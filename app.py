import streamlit as st
import os
import importlib
import textwrap
import base64
import zipfile
from io import BytesIO

# ============================================================
# Page Config
# ============================================================
st.set_page_config(
    page_title="AI/ML Project Hub - Premium Edition",
    page_icon="🤖",
    layout="wide"
)

# ============================================================
# Custom Theme / Premium UI CSS
# ============================================================
st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

/* Glassmorphism Cards */
.glass {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Title */
.main-title {
    font-size: 42px !important;
    font-weight: 800 !important;
    color: #00B4FF !important;
    text-align: center;
    margin-bottom: -10px;
}

/* Subtitle */
.sub {
    text-align:center;
    font-size:20px;
    color: #AAA;
    margin-bottom:30px;
}

/* Fade Animations */
@keyframes fadein {
    from {opacity: 0;}
    to {opacity: 1;}
}
.fade {
    animation: fadein 1.2s;
}

/* Copy Button */
.copy-btn {
    background: #0A84FF;
    color: white;
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 14px;
    cursor: pointer;
}
.copy-btn:hover {
    background: #046FD6;
}

footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ============================================================
# Header
# ============================================================
st.markdown('<div class="main-title fade">🤖 AI & ML Premium Project Hub</div>', unsafe_allow_html=True)
st.markdown('<div class="sub fade">50+ Industry-Grade Projects • Beautiful UI • Built by <b>Ankit Mishra</b></div>', unsafe_allow_html=True)
st.markdown(" ")

# ============================================================
# LOAD PROJECT FILES
# ============================================================

PROJECTS = {}
project_folder = "PROJECT"

if not os.path.exists(project_folder):
    os.makedirs(project_folder)

for file in os.listdir(project_folder):
    if file.endswith(".py"):
        try:
            module = importlib.import_module(f"{project_folder}.{file.replace('.py','')}")
            if hasattr(module, "PROJECT"):
                project = module.PROJECT
                
                category = project.get("category", "🔰 Uncategorized")
                if category not in PROJECTS:
                    PROJECTS[category] = {}
                PROJECTS[category][project["name"]] = project
        except Exception as e:
            st.warning(f"⚠️ Error loading file {file}: {e}")

# ============================================================
# SIDEBAR — Navigation Box
# ============================================================

with st.sidebar:
    st.title("📂 All Projects")
    search = st.text_input("🔍 Search Projects")

    category = st.selectbox("Select Category", list(PROJECTS.keys()))

    proj_list = list(PROJECTS[category].keys())
    if search:
        proj_list = [p for p in proj_list if search.lower() in p.lower()]

    selected = st.selectbox("Select Project", proj_list)

    st.markdown("---")
    st.info("💡 Tip: Add/Remove projects by adding .py files inside `/projects/` folder.")

# ============================================================
# ZIP DOWNLOAD BUTTON
# ============================================================

def create_zip():
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w") as zipf:
        for file in os.listdir(project_folder):
            zipf.write(os.path.join(project_folder, file), arcname=file)
    buffer.seek(0)
    return buffer

st.download_button(
    label="📦 Download All 50 Projects (ZIP)",
    data=create_zip(),
    file_name="AI_ML_Projects_By_Ankit_Mishra.zip",
    mime="application/zip"
)

# ============================================================
# DISPLAY PROJECT DETAILS
# ============================================================
project = PROJECTS[category][selected]

st.markdown(f"<h1 class='fade'>{project.get('icon', '📘')} {project['name']}</h1>", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["📄 Overview", "🧭 Steps", "💻 Code", "📁 Files"])

# ============================================================
# TAB 1: OVERVIEW
# ============================================================
with tab1:
    st.markdown("### 🔍 Project Description")
    st.write(project.get("description", ""))

    st.markdown("### 📦 Dataset")
    st.info(project.get("dataset", "No dataset info."))

    if "image" in project:
        st.image(project["image"], use_container_width=True)

# ============================================================
# TAB 2: STEPS
# ============================================================
with tab2:
    st.markdown("### 🧭 Steps Performed")
    st.markdown(f"<div class='glass fade'>{project.get('steps', '')}</div>", unsafe_allow_html=True)

# ============================================================
# TAB 3: CODE
# ============================================================
with tab3:

    st.markdown("### 💻 Complete Project Code")

    # Copy Code Button JS
    st.markdown("""
    <script>
    function copyCode() {
        navigator.clipboard.writeText(document.getElementById('codeblock').innerText);
        alert("Code copied!");
    }
    </script>
    """, unsafe_allow_html=True)

    st.markdown('<button class="copy-btn" onclick="copyCode()">📋 Copy Code</button>', unsafe_allow_html=True)

    st.markdown(f"<pre id='codeblock' class='glass fade'>{project['code']}</pre>", unsafe_allow_html=True)

# ============================================================
# TAB 4: FILES LIST
# ============================================================
with tab4:
    st.markdown("### 📁 Project Files Inside `/projects/`")
    st.write(os.listdir(project_folder))

# ============================================================
# FOOTER
# ============================================================
st.markdown("""
<br><br>
<hr>
<div style='text-align:center; color:#888; font-size:16px;'>
    🚀 Premium App Developed with ❤️ by <b>Ankit Mishra</b>  
    <br>AI/ML Full Project Hub • Streamlit Edition
</div>
""", unsafe_allow_html=True)
