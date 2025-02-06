from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(1, 'q')

qc.add_register(q)

qc.u(2.2280239390326413, -2.6835813463878475, -2.7058560853257885, q[0])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
