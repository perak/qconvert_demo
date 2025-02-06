from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from qiskit_ionq import GPIGate, GPI2Gate, MSGate
from qiskit import transpile
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

qc = QuantumCircuit()

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')

qc.add_register(q)
qc.add_register(c)

qc.id(q[0])
qc.x(q[0])
qc.y(q[0])
qc.z(q[0])
qc.h(q[0])
qc.sx(q[0])
qc.sxdg(q[0])

# r2
qc.s(q[0])


# r4
qc.t(q[0])


# r8
qc.p(np.pi / 8, q[0])

qc.rx(-2.4522873150317515, q[0])
qc.ry(-0.8230054351172829, q[0])
qc.rz(-0.721964051391391, q[0])
qc.p(-0.43066855201756526, q[0])

# u2
qc.u(np.pi / 2, 2.592797810960824, 0.5111537159291752, q[0])

qc.u(-2.6866081144080782, 0.8503837523656363, 0.9496083262543298, q[0])
qc.s(q[0])
qc.t(q[0])
qc.sdg(q[0])
qc.tdg(q[0])

# gpi
qc.u(np.pi, -1.4255817494482401, np.pi - -1.4255817494482401, q[0])


# gpi2
qc.u(np.pi / 2, 1.1344820948531975 - (np.pi / 2), (np.pi / 2) - 1.1344820948531975, q[0])


# vz
qc.rz(-2.0290277644863393, q[0])

qc.cx(q[0], q[1])
qc.cy(q[0], q[1])
qc.cz(q[0], q[1])
qc.ch(q[0], q[1])
qc.csx(q[0], q[1])
qc.swap(q[0], q[1])

# srswap
qc.u(np.pi / 2, np.pi / 2, -1 * np.pi, q[0])
qc.u(np.pi / 2, -1 * np.pi / 2, np.pi, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 4, -1 * np.pi / 2, -1 * np.pi / 2, q[0])
qc.u(np.pi / 2, 0, 7 * np.pi / 4, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 4, -1 * np.pi, -1 * np.pi / 2, q[0])
qc.u(np.pi / 2, np.pi, np.pi / 2, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 2, 0, -3 * np.pi / 2, q[0])
qc.u(np.pi / 2, np.pi / 2, 0, q[1])


# iswap
qc.u(np.pi / 2, -1 * np.pi / 2, -1 * np.pi, q[0])
qc.u(np.pi / 2, -1 * np.pi / 2, np.pi, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 2, 0, 3 * np.pi / 2, q[0])
qc.u(np.pi / 2, 3 * np.pi / 2, 0, q[1])
qc.cx(q[0], q[1])
qc.u(np.pi / 2, 0, 0, q[0])
qc.u(np.pi, np.pi / 4, -1 * np.pi / 4, q[1])

qc.rxx(0.6493842217860086, q[0], q[1])
qc.ryy(-1.3596805297028691, q[0], q[1])
qc.rzz(2.8768998605185647, q[0], q[1])

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
qc.rz(2.7463195704599936 / 2, q[0])
qc.rz(2.7463195704599936 / 2, q[1])
qc.rx(-1 * np.pi / 2, q[0])
qc.rx(-1 * np.pi / 2, q[1])
qc.cz(q[0], q[1])
qc.rz(-1 * np.pi / 2, q[0])
qc.rz(-1 * np.pi / 2, q[1])
qc.rx(np.pi / 2, q[0])
qc.rx(-1 * np.pi / 2, q[1])
qc.rz(np.pi / 4, q[0])
qc.rz(3 * np.pi / 4, q[1])

qc.append(MSGate((-2.9565772286362133) / (2*np.pi), (0.9051623980385868) / (2*np.pi)), [0, 1])

# cr2
qc.cp(np.pi / 2, q[0], q[1])


# cr4
qc.cp(np.pi / 4, q[0], q[1])


# cr8
qc.cp(np.pi / 8, q[0], q[1])


# crx
qc.cu(-0.9375412312498308, -1 * np.pi / 2, np.pi / 2, 0, q[0], q[1])


# cry
qc.u(-0.08058252005457645 / 2, 0, 0, q[1])
qc.cx(q[0], q[1])
qc.u(-1 * -0.08058252005457645 / 2, 0, 0, q[1])
qc.cx(q[0], q[1])

qc.crz(0.3531826317821056, q[0], q[1])
qc.cp(2.364691146335632, q[0], q[1])

# cu2
qc.cu(np.pi / 2, 1.3039932052205492, 2.6610590045655966, 0, q[0], q[1])

qc.cu(2.4438418503577237, 0.12036689657265498, 1.22113022887996, 0, q[0], q[1])

# cs
qc.cp(np.pi / 2, q[0], q[1])


# ct
qc.cp(np.pi / 4, q[0], q[1])


# csdg
qc.cp(-1 * np.pi / 2, q[0], q[1])


# ctdg
qc.cp(-1 * np.pi / 4, q[0], q[1])

qc.ccx(q[0], q[1], q[2])
qc.cswap(q[0], q[1], q[2])
qc.csrswap(q[0], q[1], q[2])
qc.reset(q[0])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])

qc = transpile(qc, backend)
job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
