from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

var0 = 1.570796326794896
var1 = 1.570796326794897
var2 = 2.968731284043518
var3 = 3.141592653589794

def sub(qc, var0, var1, var2, var3, a, b):
  qc.u(var0, var1, var2, a)
  qc.cu(var3, -1 * np.pi / 2, np.pi / 2, 0, a, b)


qc = QuantumCircuit()

q = QuantumRegister(2, 'q')
c = ClassicalRegister(2, 'c')

qc.add_register(q)
qc.add_register(c)

sub(qc, var0, var1, var2, var3, q[0], q[1])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
