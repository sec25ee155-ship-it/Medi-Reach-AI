"""Illustrative, non-clinical rules for the MediReach AI demo."""
SAMPLE_DATA = {
    "Routine example": {"age": 35, "temperature_c": 36.8, "heart_rate": 78, "systolic_bp": 118, "diastolic_bp": 76, "spo2": 98, "symptoms": []},
    "Fever example": {"age": 24, "temperature_c": 38.5, "heart_rate": 96, "systolic_bp": 120, "diastolic_bp": 80, "spo2": 97, "symptoms": ["fever", "cough"]},
    "Needs prompt review": {"age": 68, "temperature_c": 37.2, "heart_rate": 108, "systolic_bp": 158, "diastolic_bp": 96, "spo2": 93, "symptoms": ["weakness"]},
    "Urgent warning example": {"age": 52, "temperature_c": 37.0, "heart_rate": 118, "systolic_bp": 90, "diastolic_bp": 60, "spo2": 88, "symptoms": ["breathlessness"]},
}

def assess_risk(age, temperature_c, heart_rate, systolic_bp, diastolic_bp, spo2, symptoms):
    """Return demo risk level, summary, guidance, and urgent flag.

    These thresholds are intentionally simple demonstration rules, not medical advice.
    """
    symptoms = set(symptoms or [])
    urgent = (
        "chest_pain" in symptoms or "fainting" in symptoms or
        "breathlessness" in symptoms or spo2 < 90 or
        systolic_bp < 90 or temperature_c >= 40
    )
    flags = []
    if temperature_c >= 38.0: flags.append("raised temperature")
    if heart_rate < 50 or heart_rate > 100: flags.append("heart rate outside the demo reference range")
    if systolic_bp >= 140 or diastolic_bp >= 90: flags.append("raised blood pressure reading")
    if spo2 < 95: flags.append("lower oxygen saturation reading")
    if symptoms: flags.append("reported symptoms")

    if urgent:
        level = "High"
        summary = "The demo identified an urgent warning sign. This result cannot determine the cause."
        guidance = "Seek urgent professional assessment now; use local emergency services for severe or rapidly worsening symptoms."
    elif flags:
        level = "Moderate"
        summary = "The demo found one or more items that may deserve follow-up: " + ", ".join(flags) + "."
        guidance = "Consider contacting a qualified healthcare professional, especially if symptoms persist or worsen."
    else:
        level = "Low"
        summary = "No demo rule was triggered by the values entered. This does not rule out illness."
        guidance = "Continue routine preventive care and consult a healthcare professional if concerned."

    return {"level": level, "summary": summary, "guidance": guidance, "urgent": urgent, "flags": flags}
