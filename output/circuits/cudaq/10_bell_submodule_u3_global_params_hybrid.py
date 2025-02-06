import cudaq
from scipy.optimize import minimize
from collections import Counter
import numpy as np

shots = 1024

params = [
  0, # var0
  0, # var1
  0 # var2
]

tolerance = 0.001

@cudaq.kernel
def sub(var0: float, var1: float, var2: float, q_0: cudaq.qubit, q_1: cudaq.qubit):
  u3(var0, var1, var2, q_0)
  cx(q_0, q_1)

@cudaq.kernel
def circuit(params: list[float]):
  q = cudaq.qvector(2)
  sub(params[0], params[1], params[2], q[0], q[1])
  mz(q[0])
  mz(q[1])

def objective_function(params):
  counts = cudaq.sample(circuit, params, shots_count=shots)
  counts = Counter(dict(counts.items()))
  cost = 0
  cost += np.abs(counts["00"] / shots - 0.5)
  cost += np.abs(counts["11"] / shots - 0.5)

  return cost

minimum = minimize(objective_function, params, method="Powell", tol=tolerance)
print("cost:", minimum.fun, "params:", minimum.x)
