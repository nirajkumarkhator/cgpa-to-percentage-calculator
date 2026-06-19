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
<meta name="description" content="Free CGPA to Percentage Calculator for students. Convert CGPA to percentage using standard formulas like ×9.5, ×10, and university rules. Fast, accurate and mobile friendly tool.">
<meta name="keywords" content="CGPA to percentage calculator, CGPA calculator, GPA to percentage, percentage calculator for students, convert CGPA to percentage, CGPA × 9.5, CGPA × 10">
<meta name="author" content="CGPA Calculator Tool">
""", unsafe_allow_html=True)

# Header
st.title("🎓 CGPA to Percentage Calculator")
st.write("""
👉 Convert your CGPA into percentage instantly using standard academic formulas.  
✔ Fast calculation  
✔ Mobile friendly  
✔ Free for all students  
""")

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

# Calculation logic (FIXED)
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
    Calculation used:  
    {formula}  
    Result: {percentage:.2f}%
    """)

# SEO Content Section (Humanized)
st.markdown("---")

st.header("📘 What is CGPA to Percentage Conversion?")

st.write("""
CGPA (Cumulative Grade Point Average) is a grading system used in schools and universities.

To convert CGPA into percentage, different institutions use different formulas:

- Most common formula: CGPA × 9.5  
- Engineering colleges: CGPA × 10  
- Some universities: (CGPA − 0.5) × 10  

This tool helps you calculate instantly without confusion.
""")

# Example Section
st.subheader("📊 Example Calculation")

st.write("""
If your CGPA is 8.0:

- Using ×9.5 → 76%
- Using ×10 → 80%
- Using (−0.5)×10 → 75%
""")

# FAQ
st.header("❓ Frequently Asked Questions")

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
