import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="2-Min Dental Check",
    page_icon="🦷",
    layout="centered"
)

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
.main {
    padding-top: 10px;
}
.result-box {
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.condition {
    background-color: #0f5132;
    color: #d1e7dd;
}
.action {
    background-color: #1c2541;
    color: #cfe2ff;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🦷 2-Min Dental Self-Check")
st.write("Quickly understand your dental issue in under 2 minutes.")

# -----------------------------
# Disclaimer
# -----------------------------
st.warning("This tool provides general guidance only and is not a medical diagnosis.")

st.divider()

# -----------------------------
# Input
# -----------------------------
pain = st.radio("Are you experiencing any pain or discomfort in your teeth or gums?", ["Yes", "No"])

result = None
action = ""
advice = ""
avoid = ""
visit = ""

# -----------------------------
# PAIN FLOW
# -----------------------------
if pain == "Yes":
    pain_type = st.selectbox("Type of pain", ["Sharp", "Dull/Continuous", "While eating"])
    trigger = st.selectbox("Trigger", ["Cold", "Sweet", "Biting", "Spontaneous"])
    duration = st.selectbox("Duration", ["<1 day", "1–3 days", ">3 days"])

    if trigger == "Cold" and pain_type == "Sharp":
        result = "Tooth Sensitivity / Early Caries"
        action = "Visit dentist soon"
        advice = "Use desensitizing toothpaste and avoid cold foods."
        avoid = "Do not ignore if symptoms worsen."
        visit = "If symptoms persist beyond 3 days."

    elif trigger == "Sweet":
        result = "Possible Dental Caries"
        action = "Visit dentist soon"
        advice = "Maintain oral hygiene and reduce sugar intake."
        avoid = "Avoid frequent consumption of sweets."
        visit = "Within a few days."

    elif trigger == "Spontaneous" and duration == ">3 days":
        result = "Possible Pulpitis"
        action = "Seek immediate dental care"
        advice = "Consult a dentist as soon as possible."
        avoid = "Avoid self-medication and delaying care."
        visit = "Immediately."

    elif trigger == "Biting":
        result = "Possible Cracked Tooth / Occlusal Issue"
        action = "Visit dentist soon"
        advice = "Avoid chewing on the affected side."
        avoid = "Avoid hard foods."
        visit = "Within 2–3 days."

    else:
        result = "Unclear Dental Pain"
        action = "Monitor and consult dentist if needed"
        advice = "Observe symptoms closely."
        avoid = "Ignoring worsening pain."
        visit = "If pain persists beyond 2 days."

# -----------------------------
# NO PAIN FLOW
# -----------------------------
elif pain == "No":
    symptom = st.selectbox(
        "What do you notice?",
        [
            "No noticeable issues",
            "Bleeding gums",
            "Swelling",
            "Ulcer",
            "Bad breath",
            "Stains",
            "Other / Not listed"
        ]
    )

    if symptom == "No noticeable issues":
        result = "No obvious dental concern"
        action = "Maintain routine oral care"
        advice = "Brush twice daily, floss regularly, and maintain hygiene."
        avoid = "Skipping regular dental checkups."
        visit = "Routine checkup every 6 months."

    elif symptom == "Bleeding gums":
        result = "Gingivitis"
        action = "Routine dental visit recommended"
        advice = "Improve brushing technique and floss regularly."
        avoid = "Ignoring bleeding gums."
        visit = "Within a week."

    elif symptom == "Swelling":
        result = "Possible Abscess / Infection"
        action = "Seek immediate dental care"
        advice = "Consult a dentist urgently."
        avoid = "Delaying treatment."
        visit = "Immediately."

    elif symptom == "Ulcer":
        result = "Aphthous Ulcer"
        action = "Monitor condition"
        advice = "Maintain oral hygiene and consider topical gels."
        avoid = "Spicy or irritating foods."
        visit = "If it persists beyond 5 days."

    elif symptom == "Bad breath":
        result = "Halitosis (Possible gum-related issue)"
        action = "Dental check recommended"
        advice = "Clean tongue and maintain oral hygiene."
        avoid = "Poor oral hygiene habits."
        visit = "Within a week."

    elif symptom == "Stains":
        result = "Extrinsic Staining"
        action = "Cosmetic dental cleaning optional"
        advice = "Professional cleaning can help remove stains."
        avoid = "Excess tobacco or coffee consumption."
        visit = "Optional visit for cleaning."

    elif symptom == "Other / Not listed":
        result = "Unspecified condition"
        action = "Dental consultation recommended"
        advice = "Since your concern is not listed, a professional evaluation is best."
        avoid = "Self-diagnosis."
        visit = "Visit dentist if concerned."

# -----------------------------
# RESULT DISPLAY
# -----------------------------
if result:
    st.divider()
    st.subheader("🧾 Result")

    st.markdown(f"""
    <div class="result-box condition">
        <strong>Possible Condition:</strong> {result}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="result-box action">
        <strong>Recommended Action:</strong> {action}
    </div>
    """, unsafe_allow_html=True)

    st.write("### ☑️ What you can do now:")
    st.write(advice)

    st.write("### 🙅‍♀️ What to avoid:")
    st.write(avoid)

    st.write("### 🏥 When to see a dentist:")
    st.write(visit)

    st.caption("This guidance is based on your inputs and should not replace professional consultation.")

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.caption("Developed by Dr. Sunantha")