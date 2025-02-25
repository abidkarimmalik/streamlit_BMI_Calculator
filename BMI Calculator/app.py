import streamlit as st

st.title("Smart BMI Analyzer")
st.write("Smart BMI Calculator is a powerful tool designed to provide precise Body Mass Index (BMI) calculations while offering deeper health insights.")

# Unit converter
unit_system = st.radio("Height unit system:", ["Metric (meters)", "Imperial (feet/inches)"])

if unit_system == "Metric (meters)":
    height = st.number_input("Enter height (meters):", min_value=0.5, max_value=3.0, value=1.7, step=0.1)
else:
    col1, col2 = st.columns(2)
    with col1:
        feet = st.number_input("Feet", min_value=1, max_value=8, value=5)
    with col2:
        inches = st.number_input("Inches", min_value=0, max_value=11, value=0)
    height = feet * 0.3048 + inches * 0.0254  # Convert to meters
    st.caption(f"Converted height: {height:.2f} meters")

weight = st.number_input("Enter weight (kg):", min_value=1.0, value=60.0)

# BMI Calculation
bmi = weight / (height ** 2)

# Progress bar visualization
st.subheader("BMI Progress")
target_max = 40  # Maximum BMI value for visualization
progress_value = min(bmi / target_max, 1.0)  # Cap at 100%
st.progress(progress_value)

# Category markers
st.markdown("""
<style>
.bmi-marker {
    display: inline-block;
    margin: 0 15px;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    f'<div style="text-align:center">'
    '<span class="bmi-marker">Underweight<br><18.5</span>'
    '<span class="bmi-marker">Healthy<br>18.5-24.9</span>'
    '<span class="bmi-marker">Overweight<br>25-29.9</span>'
    '<span class="bmi-marker">Obese<br>30+</span>'
    '</div>',
    unsafe_allow_html=True
)

# Results display
st.subheader("Results")
col_a, col_b = st.columns(2)
with col_a:
    st.metric("BMI Score", f"{bmi:.1f}")
with col_b:
    if bmi < 18.5:
        st.error("Underweight 🎈")
        st.write("Consider consulting a nutritionist")
    elif 18.5 <= bmi < 25:
        st.success("Healthy Weight ✅")
        st.write("Great job maintaining your health!")
    elif 25 <= bmi < 30:
        st.warning("Overweight ⚠️")
        st.write("Regular exercise can help improve your health")
    else:
        st.error("Obese ❗")
        st.write("Please consult a healthcare provider")