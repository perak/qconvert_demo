import cudaq
from scipy.optimize import minimize
from collections import Counter
import numpy as np

shots = 1024

params = [
  0, # var0
  0, # var2
  0, # var4
  0, # var6
  0, # var1
  0, # var3
  0, # var5
  0, # var7
  0, # var8
  0, # var10
  0, # var12
  0, # var14
  0, # var9
  0, # var11
  0, # var13
  0, # var15
  0, # var16
  0, # var18
  0, # var20
  0, # var22
  0, # var17
  0, # var19
  0, # var21
  0, # var23
  0, # var24
  0, # var26
  0, # var28
  0, # var30
  0, # var25
  0, # var27
  0, # var29
  0, # var31
  0, # var32
  0, # var34
  0, # var36
  0, # var38
  0, # var33
  0, # var35
  0, # var37
  0, # var39
  0, # var40
  0, # var42
  0, # var44
  0, # var46
  0, # var41
  0, # var43
  0, # var45
  0 # var47
]

tolerance = 0.001

@cudaq.kernel
def circuit(params: list[float]):
  q = cudaq.qvector(4)
  ry(params[0], q[0])
  ry(params[1], q[1])
  ry(params[2], q[2])
  ry(params[3], q[3])
  rz(params[4], q[0])
  rz(params[5], q[1])
  rz(params[6], q[2])
  rz(params[7], q[3])
  cx(q[0], q[1])
  cx(q[0], q[2])
  cx(q[0], q[3])
  cx(q[1], q[2])
  cx(q[1], q[3])
  cx(q[2], q[3])
  ry(params[8], q[0])
  ry(params[9], q[1])
  ry(params[10], q[2])
  ry(params[11], q[3])
  rz(params[12], q[0])
  rz(params[13], q[1])
  rz(params[14], q[2])
  rz(params[15], q[3])
  cx(q[0], q[1])
  cx(q[0], q[2])
  cx(q[0], q[3])
  cx(q[1], q[2])
  cx(q[1], q[3])
  cx(q[2], q[3])
  ry(params[16], q[0])
  ry(params[17], q[1])
  ry(params[18], q[2])
  ry(params[19], q[3])
  rz(params[20], q[0])
  rz(params[21], q[1])
  rz(params[22], q[2])
  rz(params[23], q[3])
  cx(q[0], q[1])
  cx(q[0], q[2])
  cx(q[0], q[3])
  cx(q[1], q[2])
  cx(q[1], q[3])
  cx(q[2], q[3])
  ry(params[24], q[0])
  ry(params[25], q[1])
  ry(params[26], q[2])
  ry(params[27], q[3])
  rz(params[28], q[0])
  rz(params[29], q[1])
  rz(params[30], q[2])
  rz(params[31], q[3])
  cx(q[0], q[1])
  cx(q[0], q[2])
  cx(q[0], q[3])
  cx(q[1], q[2])
  cx(q[1], q[3])
  cx(q[2], q[3])
  ry(params[32], q[0])
  ry(params[33], q[1])
  ry(params[34], q[2])
  ry(params[35], q[3])
  rz(params[36], q[0])
  rz(params[37], q[1])
  rz(params[38], q[2])
  rz(params[39], q[3])
  cx(q[0], q[1])
  cx(q[0], q[2])
  cx(q[0], q[3])
  cx(q[1], q[2])
  cx(q[1], q[3])
  cx(q[2], q[3])
  ry(params[40], q[0])
  ry(params[41], q[1])
  ry(params[42], q[2])
  ry(params[43], q[3])
  rz(params[44], q[0])
  rz(params[45], q[1])
  rz(params[46], q[2])
  rz(params[47], q[3])
  # mz(q[0])
  # mz(q[1])
  # mz(q[2])
  # mz(q[3])

def objective_function(params):
  state = cudaq.get_state(circuit, params)
  
  # Hamiltonian
  H = np.array([
    [-0.00001, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, -1.25247, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, -1.25247, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1.83045, 0, 0, 0, 0, 0, 0, 0, 0, 0.18128, 0, 0, 0],
    [0, 0, 0, 0, -0.47595, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, -1.24625, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -1.06493, 0, 0, -0.18128, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, -1.16075, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, -0.47595, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, -0.18128, 0, 0, -1.06493, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1.24625, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1.16075, 0, 0, 0, 0],
    [0, 0, 0, 0.18128, 0, 0, 0, 0, 0, 0, 0, 0, -0.25449, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.36131, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -0.36131, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.20635]
  ])
  
  # Expectation value: <Ψ|H|Ψ>
  cost = np.real(np.dot(np.dot(state, H), np.conjugate(state).transpose()))
  

  return cost

minimum = minimize(objective_function, params, method="Powell", tol=tolerance)
print("cost:", minimum.fun, "params:", minimum.x)
