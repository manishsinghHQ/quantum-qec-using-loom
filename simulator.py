import numpy as np
from loom import task, run
from qec import encode, inject_noise, correct, decode

@task
def single_trial(initial_state, error_prob):
    encoded = encode(initial_state)
    noisy, errors = inject_noise(encoded, error_prob)
    corrected = correct(noisy)
    decoded = decode(corrected)

    success = np.allclose(
        np.abs(decoded),
        np.abs(initial_state),
        atol=0.1
    )

    return {
        "errors": errors,
        "success": success
    }

@task
def batch_trials(initial_state, error_prob, trials):
    success_count = 0

    for _ in range(trials):
        result = single_trial(initial_state, error_prob)
        if result["success"]:
            success_count += 1

    return success_count / trials

def run_simulation(initial_state, error_prob, trials):
    result = run(batch_trials(initial_state, error_prob, trials))
    return result