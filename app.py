import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from simulator import run_simulation, single_trial

st.set_page_config(page_title="Quantum QEC with Loom")

st.title("Quantum Error Correction Simulator (with Loom)")

st.markdown("""
This application demonstrates **3-qubit Bit-Flip Quantum Error Correction**
using **Python, Loom for experiment orchestration, and Streamlit for visualization**.
""")

error_prob = st.slider("Bit-flip error probability", 0.0, 1.0, 0.1)
trials = st.slider("Number of trials", 10, 500, 100)

initial_state = np.array([1, 0])  # |0>

if st.button("Run Simulation"):
    single = single_trial(initial_state, error_prob)
    success_rate = run_simulation(initial_state, error_prob, trials)

    st.subheader("Single Trial")
    st.write("Error positions:", single["errors"])
    st.write("Correction success:", single["success"])

    st.subheader("Batch Statistics (Loom)")
    st.write(f"Success rate over {trials} trials: **{success_rate:.2f}**")

    fig, ax = plt.subplots()
    ax.bar(["Success", "Failure"], [success_rate, 1 - success_rate])
    ax.set_ylabel("Probability")
    st.pyplot(fig)