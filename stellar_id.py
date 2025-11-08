# STELLAR-ID: Astronaut Authentication Dashboard
import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Page setup
st.set_page_config(page_title="STELLAR-ID", layout="centered")
st.title("🛡️ STELLAR-ID: Astronaut Authentication")

# Biometric input simulation
st.subheader("🔍 Biometric Scan")
iris_score = st.slider("Iris Match (%)", 0, 100, 85)
voice_score = st.slider("Voiceprint Match (%)", 0, 100, 80)

# Simulated behavior score
behavior_score = random.randint(60, 100)

# Confidence calculation
confidence = (iris_score + voice_score + behavior_score) / 3
st.metric("🧠 Confidence Score", f"{confidence:.2f}")

# Access decision
access_granted = confidence >= 75
if access_granted:
    st.success("✅ Access Granted")
else:
    st.error("❌ Access Denied")

# Anomaly detection
if confidence < 60 or iris_score < 50 or voice_score < 50:
    st.warning("⚠️ Anomaly Detected: Unusual biometric pattern")

st.subheader("🔐 Secure Enclave")
st.text("Mission Token: STELLAR-2025-X9")
st.text("Biometric Template: Encrypted")


st.subheader("📋 Access Log")
if "log" not in st.session_state:
    st.session_state.log = []

if st.button("Log Attempt"):
    st.session_state.log.append({
        "Time": datetime.now().strftime("%H:%M:%S"),
        "Iris": iris_score,
        "Voice": voice_score,
        "Behavior": behavior_score,
        "Score": round(confidence, 2),
        "Access": "Granted" if access_granted else "Denied"
    })

df = pd.DataFrame(st.session_state.log)
st.dataframe(df)

# Murph Protocol
st.subheader("🆘 Murph Protocol")
if st.button("Activate Emergency Override"):
    st.info("🆘 Override triggered. Crew consensus required.")

