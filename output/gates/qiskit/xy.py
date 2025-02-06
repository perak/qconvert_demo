from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(2, 'q')

qc.add_register(q)


# xy
qc.rz(3 * np.pi / 4, q[0])
qc.rz(-3 * np.pi / 4, q[1])
qc.rx(np.pi / 2, q[0])
qc.rx(np.pi / 2, q[1])
qc.cz(q[0], q[1])
qc.rz(-1 * np.pi / 2, q[0])
qc.rz(np.pi / 2, q[1])
qc.rx(np.pi / 2, q[0])
qc.rx(np.pi / 2, q[1])
qc.rz(-1.9399957263832133 / 2, q[0])
qc.rz(-1.9399957263832133 / 2, q[1])
qc.rx(-1 * np.pi / 2, q[0])
qc.rx(-1 * np.pi / 2, q[1])
qc.cz(q[0], q[1])
qc.rz(-1 * np.pi / 2, q[0])
qc.rz(-1 * np.pi / 2, q[1])
qc.rx(np.pi / 2, q[0])
qc.rx(-1 * np.pi / 2, q[1])
qc.rz(np.pi / 4, q[0])
qc.rz(3 * np.pi / 4, q[1])


job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
