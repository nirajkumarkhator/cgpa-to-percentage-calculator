import streamlit as st

st.set_page_config(
    page_title="SPPU CGPA to Percentage Calculator",
    page_icon="🎓",
    layout="centered"
)

st.title("SPPU CGPA to Percentage Calculator")

cgpa = st.number_input(
    "Enter Your CGPA",
    min_value=0.0,
    max_value=10.0,
    step=0.01
)

grade = st.selectbox(
    "Select Grade",
    [
        "O (Outstanding)",
        "A+ (Excellent)",
        "A (Very Good)",
        "B+ (Good)",
        "B (Above Average)",
        "C (Average)",
        "D (Pass)"
    ]
)

def sppu_convert(cgpa, grade):

    if grade == "O (Outstanding)":
        return 20 * cgpa - 100

    elif grade == "A+ (Excellent)":
        return 12 * cgpa - 25

    elif grade == "A (Very Good)":
        return 10 * cgpa - 7.5

    elif grade == "B+ (Good)":
        return 5 * cgpa + 26.25

    elif grade == "B (Above Average)":
        return 10 * cgpa - 2.5

    elif grade == "C (Average)":
        return 10 * cgpa - 2.5

    elif grade == "D (Pass)":
        return 6.6 * cgpa + 13.6

    return cgpa * 9.5


if st.button("Calculate Percentage"):
    percentage = sppu_convert(cgpa, grade)
    st.success(f"Percentage: {percentage:.2f}%")

st.markdown("---")

st.header("SPPU CGPA to Percentage Conversion System")

st.write("""
Savitribai Phule Pune University (SPPU) follows a structured grading system to evaluate student performance. Instead of using a single universal formula, SPPU applies different conversion formulas based on the grade obtained by the student. This ensures a more accurate representation of academic performance in percentage form.

The grading system is divided into multiple categories such as Outstanding, Excellent, Very Good, Good, Above Average, Average, and Pass. Each grade corresponds to a specific CGPA range, starting from 4.00 up to 10.00.

For students who have achieved higher grades such as O (Outstanding) or A+ (Excellent), the percentage conversion formula is more favorable and reflects strong academic performance. For example, the Outstanding grade uses a formula of 20 × CGPA − 100, while the A+ grade uses 12 × CGPA − 25.

Mid-level grades such as A and B+ follow moderate conversion formulas, ensuring balanced evaluation. Lower grades like C and D use simpler formulas to calculate the final percentage, making the system consistent across all performance levels.

It is important to note that the exact formula depends on the grade assigned and not just the CGPA value. Therefore, students must first identify their grade category before calculating the final percentage.

This calculator helps SPPU students quickly convert CGPA into percentage without manually applying formulas. It ensures accuracy, saves time, and reduces confusion during result analysis or job application processes where percentage marks are required.
""")

st.header("Frequently Asked Questions")

with st.expander("How does SPPU convert CGPA to percentage?"):
    st.write("SPPU uses grade-based formulas instead of a single fixed conversion formula. Each grade category has its own equation.")

with st.expander("Is CGPA enough to calculate percentage?"):
    st.write("No, you also need to know your grade category because SPPU uses different formulas for different grades.")

with st.expander("Is this calculator accurate?"):
    st.write("Yes, it follows official SPPU grading and conversion rules based on university guidelines.")

with st.expander("Why does SPPU use different formulas?"):
    st.write("SPPU uses multiple formulas to ensure fair evaluation of students across different performance levels.")

st.markdown("---")
st.caption("SPPU CGPA to Percentage Calculator")
