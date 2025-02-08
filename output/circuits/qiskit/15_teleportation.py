from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(3, 'q')
c0 = ClassicalRegister(1, 'c0')
c1 = ClassicalRegister(1, 'c1')

qc.add_register(q)
qc.add_register(c0)
qc.add_register(c1)

qc.rx(0.785398, q[0])
qc.h(q[1])
qc.cx(q[1], q[2])
qc.cx(q[0], q[1])
qc.h(q[0])
qc.measure(q[1], c1[0])
qc.x(q[2]).c_if(c1, 1)
qc.measure(q[0], c0[0])
qc.z(q[2]).c_if(c0, 1)

job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
