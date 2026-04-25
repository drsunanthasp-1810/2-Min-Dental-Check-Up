import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Dental Check",
    page_icon="🦷",
    layout="centered"
)

# -----------------------------
# MOBILE APP STYLE UI
# -----------------------------
st.markdown("""
<style>

/* Page background */
body {
    background-color: #eef2f7;
}

/* Center container (mobile frame) */
.block-container {
    max-width: 420px;
    margin: auto;
    padding: 20px;
}

/* App container */
.app-container {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
}

/* Title */
h1 {
    font-size: 24px;
    text-align: center;
    color: #0d6efd;
}

/* Card style */
.card {
    background-color: #ffffff;
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 12px;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}

/* Result styles */
.condition {
    background-color: #e6f4ea;
    border-left: 5px solid #2e7d32;
}

.action {
    background-color: #e7f1ff;
    border-left: 5px solid #0d6efd;
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
    font-size: 16px;
}

/* Radio spacing */
.stRadio > div {
    gap: 8px;
}

/* Select box spacing */
.stSelectbox {
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# APP CONTAINER START
# -----------------------------
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.title("🦷 Dental Self-Check")
st.caption("2-minute quick assessment")

st.warning("This tool provides general guidance and is not a medical diagnosis.")

st.divider()

# -----------------------------
# INPUT
# -----------------------------
pain = st.radio(
    "Are you experiencing any pain or discomfort in your teeth or gums?",
    ["Yes", "No"]
)

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
    trigger = st.selectbox("Trigger", ["Cold/Heat", "Sweet", "Biting", "Spontaneous"])
    duration = st.selectbox("Duration", ["<1 day", "1–3 days", ">3 days"])

    if trigger == "Cold/Heat" and pain_type == "Sharp":
        result = "Tooth Sensitivity / Early Caries"
        action = "Visit dentist soon"
        advice = "Use desensitizing toothpaste and avoid cold foods."
        avoid = "Do not ignore if symptoms worsen."
        visit = "If symptoms persist beyond 3 days."

    elif trigger == "Sweet":
        result = "Possible Dental Caries"
        action = "Visit dentist soon"
        advice = "Maintain oral hygiene and reduce sugar intake."
        avoid = "Avoid frequent sweets."
        visit = "Within a few days."

    elif trigger == "Spontaneous" and duration == ">3 days":
        result = "Possible Pulpitis"
        action = "Seek immediate dental care"
        advice = "Consult a dentist immediately."
        avoid = "Avoid delaying treatment."
        visit = "Immediately."

    elif trigger == "Biting":
        result = "Possible Cracked Tooth"
        action = "Visit dentist soon"
        advice = "Avoid chewing on that side."
        avoid = "Hard foods."
        visit = "Within 2–3 days."

    else:
        result = "Unclear Dental Pain"
        action = "Monitor and consult dentist"
        advice = "Observe symptoms."
        avoid = "Ignoring worsening pain."
        visit = "If persists > 2 days."

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
        action = "Maintain routine care"
        advice = "Brush twice daily and floss."
        avoid = "Skipping checkups."
        visit = "Routine visit every 6 months."

    elif symptom == "Bleeding gums":
        result = "Gingivitis"
        action = "Routine dental visit"
        advice = "Improve oral hygiene."
        avoid = "Ignoring bleeding."
        visit = "Within a week."

    elif symptom == "Swelling":
        result = "Possible Infection"
        action = "Seek immediate care"
        advice = "Consult dentist urgently."
        avoid = "Delaying treatment."
        visit = "Immediately."

    elif symptom == "Ulcer":
        result = "Aphthous Ulcer"
        action = "Monitor"
        advice = "Maintain hygiene."
        avoid = "Spicy foods."
        visit = "If >5 days."

    elif symptom == "Bad breath":
        result = "Halitosis"
        action = "Dental check recommended"
        advice = "Clean tongue."
        avoid = "Poor hygiene."
        visit = "Within a week."

    elif symptom == "Stains":
        result = "Extrinsic Staining"
        action = "Optional cleaning"
        advice = "Professional cleaning helps."
        avoid = "Tobacco/coffee."
        visit = "Optional."

    elif symptom == "Other / Not listed":
        result = "Unspecified issue"
        action = "Consult dentist"
        advice = "Professional evaluation needed."
        avoid = "Self-diagnosis."
        visit = "If concerned."

# -----------------------------
# RESULT DISPLAY
# -----------------------------
if result:
    st.divider()
    st.subheader("🧾 Result")

    st.markdown(f"""
    <div class="card condition">
        <strong>Possible Condition:</strong><br>{result}
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card action">
        <strong>Recommended Action:</strong><br>{action}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("### ✅ What you can do now")
    st.write(advice)

    st.write("### ⚠️ What to avoid")
    st.write(avoid)

    st.write("### 📅 When to see a dentist")
    st.write(visit)
    st.markdown('</div>', unsafe_allow_html=True)

    st.caption("This is general guidance and not a clinical diagnosis.")

# -----------------------------
# FOOTER
# -----------------------------
st.divider()
st.caption("Dr. Sunantha S P")

# Close container
st.markdown('</div>', unsafe_allow_html=True)
