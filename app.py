import streamlit as st

# Page Config
st.set_page_config(
    page_title="CGPA to Percentage Calculator | Free Online Tool for Students",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# SEO META (Streamlit HTML injection)
st.markdown("""
<meta name="google-site-verification" content="bE4LnfEmR_kVKm_yJ1fKTbzhlo8OAoyqCVBrfD55VFg" />
<meta name="description" content="Free CGPA to Percentage Calculator for students. Convert CGPA to percentage using standard formulas like ×9.5, ×10, and university rules. Fast, accurate and mobile friendly tool.">
<meta name="keywords" content="CGPA to percentage calculator, CGPA calculator, GPA to percentage, percentage calculator for students, convert CGPA to percentage, CGPA × 9.5, CGPA × 10">
<meta name="author" content="CGPA Calculator Tool">
""", unsafe_allow_html=True)

# LOGO (NEW ADDITION)
st.image("assets/logo.png", width=120)

# Header
st.title("CGPA to Percentage Calculator")

st.write("""
Convert your CGPA into percentage instantly using standard academic formulas.  
This tool is fast, mobile friendly, and designed for students.
""")

# 👉 SPPU PAGE LINK (NEW ADDITION)
st.markdown("### University Calculator")
st.page_link("sppu", label="Open SPPU Calculator")

# Input
cgpa = st.number_input(
    "Enter Your CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.01
)

# Formula selection
formula = st.selectbox(
    "Select Conversion Formula",
    [
        "Percentage = CGPA × 9.5 (Most Common)",
        "Percentage = CGPA × 10 (Engineering)",
        "Percentage = (CGPA − 0.5) × 10"
    ]
)

# Calculation logic
def calculate(cgpa, formula):

    if formula == "Percentage = CGPA × 9.5 (Most Common)":
        return cgpa * 9.5

    elif formula == "Percentage = CGPA × 10 (Engineering)":
        return cgpa * 10

    elif formula == "Percentage = (CGPA − 0.5) × 10":
        return (cgpa - 0.5) * 10

    return cgpa * 9.5  # safe fallback

# Button
if st.button("🚀 Calculate Percentage"):

    percentage = calculate(cgpa, formula)

    st.success(f"🎯 Your Percentage: {percentage:.2f}%")

    st.info(f"""
Calculation Used:  
{formula}  

Final Result: {percentage:.2f}%
""")

# SEO CONTENT
st.markdown("---")

st.header("What is CGPA to Percentage Conversion?")

st.write("""
CGPA (Cumulative Grade Point Average) is a widely used academic grading system in schools and universities.

Different institutions use different formulas to convert CGPA into percentage. The most common methods include CGPA multiplied by 9.5, CGPA multiplied by 10, and adjusted formulas such as (CGPA − 0.5) × 10.

This calculator helps students quickly convert CGPA into percentage without manual calculations or confusion. It is especially useful for job applications, higher education admissions, and competitive exams where percentage marks are required.

Since universities may follow different conversion rules, users should always check their official guidelines. However, this tool provides a fast and reliable estimation based on commonly accepted academic formulas.
""")

# Example Section
st.subheader("Example Calculation")

st.write("""
If your CGPA is 8.0:

- Using ×9.5 → 76%
- Using ×10 → 80%
- Using (−0.5)×10 → 75%
""")

# FAQ
st.header("Frequently Asked Questions")

with st.expander("What is CGPA?"):
    st.write("CGPA stands for Cumulative Grade Point Average used to measure academic performance.")

with st.expander("Which formula should I use?"):
    st.write("Use CGPA × 9.5 unless your university specifies otherwise.")

with st.expander("Is this calculator accurate?"):
    st.write("Yes, it uses standard academic conversion formulas.")

with st.expander("Is this free?"):
    st.write("Yes, 100% free for students.")

# Footer SEO
st.markdown("---")
st.caption("© 2026 CGPA to Percentage Calculator | Built for Students")
