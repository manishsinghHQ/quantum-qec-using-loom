import numpy as np
import random

X = np.array([[0, 1],
              [1, 0]], dtype=complex)

def normalize(state):
    norm = np.linalg.norm(state)
    return state / norm if norm != 0 else state

def apply_gate(state, gate):
    return normalize(gate @ state)

def bit_flip_noise(state, p):
    if random.random() < p:
        return apply_gate(state, X), True
    return state, False