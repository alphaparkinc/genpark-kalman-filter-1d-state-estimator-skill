"""
Kalman Filter 1D State Estimator Skill Client
Pure Python Standard Library implementation of the Linear Kalman Filter (Kalman / Welch & Bishop).
Performs recursive Predict-Update cycles for continuous latent state estimation under Gaussian noise.
"""

from typing import List, Dict, Any, Tuple, Optional


class KalmanFilter1D:
    def __init__(self, initial_state: float = 0.0, initial_variance: float = 1.0,
                 process_variance: float = 1e-3, measurement_variance: float = 0.1):
        self.x = initial_state         # State estimate
        self.p = initial_variance      # Estimate covariance
        self.q = process_variance      # Process noise variance Q
        self.r = measurement_variance  # Measurement noise variance R

    def predict(self, control_u: float = 0.0):
        """Time update (Predict phase)."""
        self.x = self.x + control_u
        self.p = self.p + self.q

    def update(self, measurement_z: float) -> Tuple[float, float, float]:
        """
        Measurement update (Correct phase).
        Returns (state_estimate, kalman_gain, updated_covariance).
        """
        # Kalman Gain: K = P / (P + R)
        k = self.p / (self.p + self.r)
        # State update: x = x + K * (z - x)
        self.x = self.x + k * (measurement_z - self.x)
        # Covariance update: P = (1 - K) * P
        self.p = (1.0 - k) * self.p
        return self.x, k, self.p

    def step(self, measurement_z: float, control_u: float = 0.0) -> Tuple[float, float]:
        self.predict(control_u)
        self.update(measurement_z)
        return self.x, self.p
