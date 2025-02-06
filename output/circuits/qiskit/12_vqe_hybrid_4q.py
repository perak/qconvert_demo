from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from scipy.optimize import minimize
from collections import Counter
import numpy as np

backend = Aer.get_backend("statevector_simulator")

shots = 1024

var0 = 0
var2 = 0
var4 = 0
var6 = 0
var1 = 0
var3 = 0
var5 = 0
var7 = 0
var8 = 0
var10 = 0
var12 = 0
var14 = 0
var9 = 0
var11 = 0
var13 = 0
var15 = 0
var16 = 0
var18 = 0
var20 = 0
var22 = 0
var17 = 0
var19 = 0
var21 = 0
var23 = 0
var24 = 0
var26 = 0
var28 = 0
var30 = 0
var25 = 0
var27 = 0
var29 = 0
var31 = 0
var32 = 0
var34 = 0
var36 = 0
var38 = 0
var33 = 0
var35 = 0
var37 = 0
var39 = 0
var40 = 0
var42 = 0
var44 = 0
var46 = 0
var41 = 0
var43 = 0
var45 = 0
var47 = 0

tolerance = 0.001

def objective_function(params):
  qc = QuantumCircuit()

  q = QuantumRegister(4, 'q')
  c = ClassicalRegister(4, 'c')

  qc.add_register(q)
  qc.add_register(c)

  qc.ry(params[0], q[0])
  qc.ry(params[1], q[1])
  qc.ry(params[2], q[2])
  qc.ry(params[3], q[3])
  qc.rz(params[4], q[0])
  qc.rz(params[5], q[1])
  qc.rz(params[6], q[2])
  qc.rz(params[7], q[3])
  qc.cx(q[0], q[1])
  qc.cx(q[0], q[2])
  qc.cx(q[0], q[3])
  qc.cx(q[1], q[2])
  qc.cx(q[1], q[3])
  qc.cx(q[2], q[3])
  qc.ry(params[8], q[0])
  qc.ry(params[9], q[1])
  qc.ry(params[10], q[2])
  qc.ry(params[11], q[3])
  qc.rz(params[12], q[0])
  qc.rz(params[13], q[1])
  qc.rz(params[14], q[2])
  qc.rz(params[15], q[3])
  qc.cx(q[0], q[1])
  qc.cx(q[0], q[2])
  qc.cx(q[0], q[3])
  qc.cx(q[1], q[2])
  qc.cx(q[1], q[3])
  qc.cx(q[2], q[3])
  qc.ry(params[16], q[0])
  qc.ry(params[17], q[1])
  qc.ry(params[18], q[2])
  qc.ry(params[19], q[3])
  qc.rz(params[20], q[0])
  qc.rz(params[21], q[1])
  qc.rz(params[22], q[2])
  qc.rz(params[23], q[3])
  qc.cx(q[0], q[1])
  qc.cx(q[0], q[2])
  qc.cx(q[0], q[3])
  qc.cx(q[1], q[2])
  qc.cx(q[1], q[3])
  qc.cx(q[2], q[3])
  qc.ry(params[24], q[0])
  qc.ry(params[25], q[1])
  qc.ry(params[26], q[2])
  qc.ry(params[27], q[3])
  qc.rz(params[28], q[0])
  qc.rz(params[29], q[1])
  qc.rz(params[30], q[2])
  qc.rz(params[31], q[3])
  qc.cx(q[0], q[1])
  qc.cx(q[0], q[2])
  qc.cx(q[0], q[3])
  qc.cx(q[1], q[2])
  qc.cx(q[1], q[3])
  qc.cx(q[2], q[3])
  qc.ry(params[32], q[0])
  qc.ry(params[33], q[1])
  qc.ry(params[34], q[2])
  qc.ry(params[35], q[3])
  qc.rz(params[36], q[0])
  qc.rz(params[37], q[1])
  qc.rz(params[38], q[2])
  qc.rz(params[39], q[3])
  qc.cx(q[0], q[1])
  qc.cx(q[0], q[2])
  qc.cx(q[0], q[3])
  qc.cx(q[1], q[2])
  qc.cx(q[1], q[3])
  qc.cx(q[2], q[3])
  qc.ry(params[40], q[0])
  qc.ry(params[41], q[1])
  qc.ry(params[42], q[2])
  qc.ry(params[43], q[3])
  qc.rz(params[44], q[0])
  qc.rz(params[45], q[1])
  qc.rz(params[46], q[2])
  qc.rz(params[47], q[3])
  # qc.measure(q[0], c[0])
  # qc.measure(q[1], c[1])
  # qc.measure(q[2], c[2])
  # qc.measure(q[3], c[3])

  job = execute(qc, backend=backend, shots=shots)
  job_result = job.result()
  state = job_result.get_statevector(qc).data

  
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

params = np.array([var0, var2, var4, var6, var1, var3, var5, var7, var8, var10, var12, var14, var9, var11, var13, var15, var16, var18, var20, var22, var17, var19, var21, var23, var24, var26, var28, var30, var25, var27, var29, var31, var32, var34, var36, var38, var33, var35, var37, var39, var40, var42, var44, var46, var41, var43, var45, var47])

minimum = minimize(objective_function, params, method="Powell", tol=tolerance)
print("cost:", minimum.fun, "params:", minimum.x)
