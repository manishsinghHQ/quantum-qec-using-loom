from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import streamlit as st
# ---------------------------------
# 1. Create Quantum Circuit
# 3 qubits + 1 classical bit
# ---------------------------------
qc = QuantumCircuit(3, 1)

# ---------------------------------
# 2. Encode Logical Qubit
# |ψ⟩ → |ψψψ⟩
# ---------------------------------
qc.cx(0, 1)
qc.cx(0, 2)

# ---------------------------------
# 3. Inject Bit-Flip Error (X)
# Simulate error on qubit 1
# ---------------------------------
qc.x(1)   # Comment this line to test "no error"

# ---------------------------------
# 4. Decode & Correct Error
# ---------------------------------
qc.cx(0, 1)
qc.cx(0, 2)
qc.ccx(1, 2, 0)  # Majority vote correction

# ---------------------------------
# 5. Measure Logical Qubit
# ---------------------------------
qc.measure(0, 0)

# ---------------------------------
# 6. Run on Simulator
# ---------------------------------
backend = AerSimulator()
result = backend.run(qc, shots=1024).result()
counts = result.get_counts()

# ---------------------------------
# 7. Display Results
# ---------------------------------
print("Measurement Counts:", counts)
fig = plot_histogram(counts)
st.pyplot(fig)