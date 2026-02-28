import streamlit as st
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(page_title="Quantum Error Correction Project", layout="wide")

st.title("🧬 Interactive Quantum Error Correction System")
st.markdown("### 3-Qubit Bit-Flip Error Correction Code")

# ---------------------------------
# USER INPUT PANEL
# ---------------------------------
st.sidebar.header("⚙️ User Controls")

apply_error = st.sidebar.checkbox("Apply Bit-Flip Error (X)", value=True)
shots = st.sidebar.slider("Number of shots", 128, 2048, 1024)

# ---------------------------------
# THEORY SECTION
# ---------------------------------
with st.expander("📘 Theory: What is Quantum Error Correction?"):
    st.markdown("""
**Quantum Error Correction (QEC)** protects quantum information from noise.

### Bit-Flip Code:
- Encodes 1 logical qubit into 3 physical qubits
- Corrects one bit-flip (X) error
- Uses majority voting

### Steps:
1. Encoding
2. Error injection
3. Decoding
4. Correction
5. Measurement
""")

# ---------------------------------
# BUILD CIRCUIT FUNCTION
# ---------------------------------
def build_qec_circuit(apply_error):
    qc = QuantumCircuit(3, 1)

    # Encode
    qc.cx(0, 1)
    qc.cx(0, 2)

    # Error
    if apply_error:
        qc.x(1)

    # Decode & correct
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.ccx(1, 2, 0)

    # Measure
    qc.measure(0, 0)
    return qc

# ---------------------------------
# RUN BUTTON
# ---------------------------------
if st.button("🚀 Run Quantum Experiment"):
    qc = build_qec_circuit(apply_error)

    st.subheader("Quantum Circuit")
    st.code(qc.draw(output="text"))

    backend = AerSimulator()
    result = backend.run(qc, shots=shots).result()
    counts = result.get_counts()

    st.subheader("Measurement Results")
    st.write(counts)

    fig = plot_histogram(counts)
    st.pyplot(fig)

    # ---------------------------------
    # INTERPRETATION
    # ---------------------------------
    st.subheader("Result Interpretation")
    if "0" in counts:
        st.success("✔ Error successfully corrected. Logical qubit recovered.")
    else:
        st.warning("⚠ Error not corrected. Noise exceeded correction ability.")

# ---------------------------------
# FOOTER
# ---------------------------------
st.markdown("---")
st.caption("Quantum Error Correction Project | Educational & Research Demo")