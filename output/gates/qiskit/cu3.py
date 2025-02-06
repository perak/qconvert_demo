from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(2, 'q')

qc.add_register(q)

qc.cu(-2.554803775126938, 0.07538532764859829, 1.3869906544679287, 0, q[0], q[1])

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
