"""
Demonstration of Kalman Filter 1D State Estimator Skill
"""

from client import KalmanFilter1D

def main():
    print("=== Filtering Noisy Agent Sensor Stream with Kalman Filter ===")
    kf = KalmanFilter1D(initial_state=0.0, initial_variance=10.0, process_variance=0.01, measurement_variance=0.5)

    # True latent state is stationary at 10.0 with noisy measurements
    noisy_readings = [10.5, 9.2, 11.1, 9.8, 10.3, 9.4, 10.7, 10.1]

    print("Step-by-Step Kalman Estimation:")
    for idx, z in enumerate(noisy_readings, 1):
        est, var = kf.step(z)
        print(f"  Step {idx}: Reading={z:4.1f} | Filtered State={est:.3f} (Covariance={var:.4f})")

    assert 9.8 <= kf.x <= 10.3
    assert kf.p < 0.2  # Uncertainty significantly reduced
    print("\nKalman Filter 1D State Estimator Verification PASS!")

if __name__ == "__main__":
    main()
