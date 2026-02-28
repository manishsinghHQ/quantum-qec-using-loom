import numpy as np
from quantum import bit_flip_noise, normalize

def encode(state):
    return [state.copy(), state.copy(), state.copy()]

def inject_noise(encoded, p):
    noisy = []
    errors = []
    for i, q in enumerate(encoded):
        nq, e = bit_flip_noise(q, p)
        noisy.append(nq)
        if e:
            errors.append(i)
    return noisy, errors

def measure(qubit):
    probs = np.abs(qubit) ** 2
    return int(np.argmax(probs))

def correct(noisy):
    measurements = [measure(q) for q in noisy]
    majority = round(sum(measurements) / 3)

    corrected = []
    for m in measurements:
        if m == majority:
            corrected.append(np.array([1, 0]) if m == 0 else np.array([0, 1]))
        else:
            corrected.append(np.array([0, 1]) if majority == 1 else np.array([1, 0]))
    return corrected

def decode(corrected):
    return normalize(corrected[0])