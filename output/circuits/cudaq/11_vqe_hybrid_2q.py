import cudaq
from scipy.optimize import minimize
from collections import Counter
import numpy as np

shots = 1024

params = [
  0, # var0
  0, # var2
  0, # var1
  0, # var3
  0, # var4
  0, # var6
  0, # var5
  0, # var7
  0, # var8
  0, # var10
  0, # var9
  0, # var11
  0, # var12
  0, # var14
  0, # var13
  0 # var15
]

tolerance = 0.001

@cudaq.kernel
def circuit(params: list[float]):
  q = cudaq.qvector(2)
  ry(params[0], q[0])
  ry(params[1], q[1])
  rz(params[2], q[0])
  rz(params[3], q[1])
  cx(q[0], q[1])
  ry(params[4], q[0])
  ry(params[5], q[1])
  rz(params[6], q[0])
  rz(params[7], q[1])
  cx(q[0], q[1])
  ry(params[8], q[0])
  ry(params[9], q[1])
  rz(params[10], q[0])
  rz(params[11], q[1])
  cx(q[0], q[1])
  ry(params[12], q[0])
  ry(params[13], q[1])
  rz(params[14], q[0])
  rz(params[15], q[1])
  # mz(q[0])
  # mz(q[1])

def objective_function(params):
  state = cudaq.get_state(circuit, params)
  
  # Hamiltonian
  H = np.array([
    [0, 0, 0, 0],
    [0, -1.8302, 0.182, 0],
    [0, 0.182, -0.2738, 0],
    [0, 0, 0, 0.1824]
  ])
  
  # Expectation value: <Ψ|H|Ψ>
  cost = np.real(np.dot(np.dot(state, H), np.conjugate(state).transpose()))
  

  return cost

minimum = minimize(objective_function, params, method="Powell", tol=tolerance)
print("cost:", minimum.fun, "params:", minimum.x)
