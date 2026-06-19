import streamlit as st

# Page SEO
st.set_page_config(
    page_title="CGPA to Percentage Calculator - Free Online Tool",
    page_icon="🎓",
    layout="centered"
)

# SEO Content
st.title("🎓 CGPA to Percentage Calculator")
st.write(
    "Convert CGPA to Percentage instantly using the standard formula. "
    "This free online CGPA to Percentage Calculator helps students calculate academic percentages accurately."
)

# Calculator
cgpa = st.number_input(
    "Enter Your CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.01
)

formula = st.selectbox(
    "Select Conversion Formula",
    [
        "Percentage = CGPA × 9.5",
        "Percentage = (CGPA - 0.5) × 10"
    ]
)

if st.button("Calculate Percentage"):
    if formula == "Percentage = CGPA × 9.5":
        percentage = cgpa * 9.5
    else:
        percentage = (cgpa - 0.5) * 10

    st.success(f"Percentage: {percentage:.2f}%")

# Quick Table
st.subheader("CGPA to Percentage Chart")

table_data = {
    "CGPA": [6, 7, 8, 8.5, 9, 9.5, 10],
    "Percentage": [
        57.0,
        66.5,
        76.0,
        80.75,
        85.5,
        90.25,
        95.0
    ]
}

st.table(table_data)

# SEO Content
st.header("How to Convert CGPA to Percentage?")

st.write("""
The most commonly used formula is:

**Percentage = CGPA × 9.5**

For example:

- CGPA = 8.0
- Percentage = 8.0 × 9.5
- Percentage = 76%

Different universities may use different conversion formulas.
Always check your university guidelines.
""")

# FAQ Schema Style Content
st.header("Frequently Asked Questions")

with st.expander("What is CGPA?"):
    st.write(
        "CGPA stands for Cumulative Grade Point Average. "
        "It measures a student's academic performance."
    )

with st.expander("How do I convert CGPA into Percentage?"):
    st.write(
        "Use the formula Percentage = CGPA × 9.5 unless your university specifies another formula."
    )

with st.expander("Is this calculator free?"):
    st.write("Yes, this CGPA to Percentage Calculator is completely free.")

# Footer
st.markdown("---")
st.caption("© 2026 CGPA to Percentage Calculator")
