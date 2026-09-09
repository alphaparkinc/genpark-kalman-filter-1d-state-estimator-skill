# GenPark Kalman Filter 1D State Estimator Skill

1D linear Kalman filter for real-time optimal state estimation and noisy sensor stream fusion.

Learn more at [GenPark](https://genpark.ai) and the [GenPark MCP Catalog](https://genpark.ai/mcp).

```mermaid
graph LR
    A[Predict: x_k = x_k-1 + u_k, P_k = P_k-1 + Q] --> B[Calculate Kalman Gain K = P / (P + R)]
    B --> C[Update State: x = x + K * (z - x)]
    C --> D[Update Covariance: P = (1 - K) * P]
    D -->|Next Step| A
```

## Features
- Recursive predictor-corrector equations.
- Dynamic measurement uncertainty weighting.
- Pure Python standard library.
