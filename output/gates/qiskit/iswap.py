from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(2, 'q')

qc.add_register(q)


# iswap
qc.u(np.pi / 2, -1 * np.pi / 2, -1 * np.pi, q[0])
qc.u(np.pi / 2, -1 * np.pi / 2, np.pi, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 2, 0, 3 * np.pi / 2, q[0])
qc.u(np.pi / 2, 3 * np.pi / 2, 0, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 2, 0, 0, q[0])
qc.u(np.pi, np.pi / 4, -1 * np.pi / 4, q[1])


job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
