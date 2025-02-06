from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from qiskit_ionq import GPIGate, GPI2Gate, MSGate
from qiskit import transpile
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(1, 'q')

qc.add_register(q)


# gpi2
qc.u(np.pi / 2, -0.5898269553487046 - (np.pi / 2), (np.pi / 2) - -0.5898269553487046, q[0])


qc = transpile(qc, backend)
job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
