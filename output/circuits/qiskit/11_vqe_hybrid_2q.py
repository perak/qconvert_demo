from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from scipy.optimize import minimize
from collections import Counter
import numpy as np

backend = Aer.get_backend("statevector_simulator")

shots = 1024

var0 = 0
var2 = 0
var1 = 0
var3 = 0
var4 = 0
var6 = 0
var5 = 0
var7 = 0
var8 = 0
var10 = 0
var9 = 0
var11 = 0
var12 = 0
var14 = 0
var13 = 0
var15 = 0

tolerance = 0.001

def objective_function(params):
  qc = QuantumCircuit()

  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')

  qc.add_register(q)
  qc.add_register(c)

  qc.ry(params[0], q[0])
  qc.ry(params[1], q[1])
  qc.rz(params[2], q[0])
  qc.rz(params[3], q[1])
  qc.cx(q[0], q[1])
  qc.ry(params[4], q[0])
  qc.ry(params[5], q[1])
  qc.rz(params[6], q[0])
  qc.rz(params[7], q[1])
  qc.cx(q[0], q[1])
  qc.ry(params[8], q[0])
  qc.ry(params[9], q[1])
  qc.rz(params[10], q[0])
  qc.rz(params[11], q[1])
  qc.cx(q[0], q[1])
  qc.ry(params[12], q[0])
  qc.ry(params[13], q[1])
  qc.rz(params[14], q[0])
  qc.rz(params[15], q[1])
  # qc.measure(q[0], c[0])
  # qc.measure(q[1], c[1])

  job = execute(qc, backend=backend, shots=shots)
  job_result = job.result()
  state = job_result.get_statevector(qc).data

  
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

params = np.array([var0, var2, var1, var3, var4, var6, var5, var7, var8, var10, var9, var11, var12, var14, var13, var15])

minimum = minimize(objective_function, params, method="Powell", tol=tolerance)
print("cost:", minimum.fun, "params:", minimum.x)
