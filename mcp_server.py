"""
MCP Server for Kalman Filter 1D State Estimator Skill
"""

import json
import sys
from client import KalmanFilter1D

kf = KalmanFilter1D()

def handle_call(name: str, args: dict) -> dict:
    if name == "filter_measurement":
        z = args.get("measurement", 0.0)
        u = args.get("control", 0.0)
        est, var = kf.step(z, u)
        return {"estimated_state": est, "variance": var}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_call(req.get("method"), req.get("params", {}))
        sys.stdout.write(json.dumps(res) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
