from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from scipy.optimize import minimize
from collections import Counter
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

var0 = 0
var1 = 0
var2 = 0

tolerance = 0.001

def objective_function(params):
  qc = QuantumCircuit()

  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')

  qc.add_register(q)
  qc.add_register(c)

  qc.u(params[0], params[1], params[2], q[0])
  qc.cx(q[0], q[1])
  qc.measure(q[0], c[0])
  qc.measure(q[1], c[1])

  job = execute(qc, backend=backend, shots=shots)
  job_result = job.result()
  counts = Counter(job_result.get_counts(qc))

  cost = 0
  cost += np.abs(counts["00"] / shots - 0.5)
  cost += np.abs(counts["11"] / shots - 0.5)

  return cost

params = np.array([var0, var1, var2])

minimum = minimize(objective_function, params, method="Powell", tol=tolerance)
print("cost:", minimum.fun, "params:", minimum.x)
