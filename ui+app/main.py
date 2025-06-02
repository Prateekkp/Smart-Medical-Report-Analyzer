import streamlit as st
import tempfile
from pdf_ocr import extract_text_from_pdf, extract_text_from_image
from llm_groq import ask_groq_llm

st.set_page_config(
    page_title=" Smart Medical Report Analyzer",
    page_icon="🧠",  
    layout="wide"
)

# ---------- HEADER ----------
st.markdown("<h1 style='text-align: center;'>🧠 Smart Medical Report Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>AI-powered tool to summarize and interpret medical reports</h4>", unsafe_allow_html=True)
st.markdown("---")

# ---------- FILE UPLOAD ----------
st.subheader("📤 Upload your medical report (PDF or Image)")
uploaded_file = st.file_uploader("", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.success(f"📄 File uploaded: `{uploaded_file.name}`")

    # ---------- TEXT EXTRACTION ----------
    st.subheader("🔍 Extracting Text...")
    if uploaded_file.name.lower().endswith(".pdf"):
        extracted_text = extract_text_from_pdf(temp_path)
    else:
        extracted_text = extract_text_from_image(temp_path)

    if extracted_text:
        st.success("✅ Text extracted successfully!")

        # Split into two columns
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("#### 📃 Original Text")
            st.text_area("", extracted_text, height=300)
        with col2:
            st.markdown("#### 🤖 AI-Based Medical Summary")
            if st.button("🔎 Analyze Report"):
                with st.spinner("Analyzing report using LLM..."):
                    analysis = ask_groq_llm(extracted_text)
                    st.success("✅ Analysis complete")
                    st.markdown(analysis)
    else:
        st.error("⚠️ Could not extract text. Please upload a clearer document.")

else:
    st.info("📂 Please upload a file to begin analysis.")

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built with 💡 by Prateek | Powered by Groq API & LLaMA</p>", unsafe_allow_html=True)
