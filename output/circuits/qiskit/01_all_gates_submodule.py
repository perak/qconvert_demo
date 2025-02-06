from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from qiskit_ionq import GPIGate, GPI2Gate, MSGate
from qiskit import transpile
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

def sub(qc, a, b, c):
  qc.id(a)
  qc.x(a)
  qc.y(a)
  qc.z(a)
  qc.h(a)
  qc.sx(a)
  qc.sxdg(a)

# r2
  qc.s(a)


# r4
  qc.t(a)


# r8
  qc.p(np.pi / 8, a)

  qc.rx(-2.4522873150317515, a)
  qc.ry(-0.8230054351172829, a)
  qc.rz(-0.721964051391391, a)
  qc.p(-0.43066855201756526, a)

# u2
  qc.u(np.pi / 2, 2.592797810960824, 0.5111537159291752, a)

  qc.u(-2.6866081144080782, 0.8503837523656363, 0.9496083262543298, a)
  qc.s(a)
  qc.t(a)
  qc.sdg(a)
  qc.tdg(a)

# gpi
  qc.u(np.pi, -1.4255817494482401, np.pi - -1.4255817494482401, a)


# gpi2
  qc.u(np.pi / 2, 1.1344820948531975 - (np.pi / 2), (np.pi / 2) - 1.1344820948531975, a)


# vz
  qc.rz(-2.0290277644863393, a)

  qc.cx(a, b)
  qc.cy(a, b)
  qc.cz(a, b)
  qc.ch(a, b)
  qc.csx(a, b)
  qc.swap(a, b)

# srswap
  qc.u(np.pi / 2, np.pi / 2, -1 * np.pi, a)
  qc.u(np.pi / 2, -1 * np.pi / 2, np.pi, b)
  qc.cx(a, b)
  qc.u(np.pi / 4, -1 * np.pi / 2, -1 * np.pi / 2, a)
  qc.u(np.pi / 2, 0, 7 * np.pi / 4, b)
  qc.cx(a, b)
  qc.u(np.pi / 4, -1 * np.pi, -1 * np.pi / 2, a)
  qc.u(np.pi / 2, np.pi, np.pi / 2, b)
  qc.cx(a, b)
  qc.u(np.pi / 2, 0, -3 * np.pi / 2, a)
  qc.u(np.pi / 2, np.pi / 2, 0, b)


# iswap
  qc.u(np.pi / 2, -1 * np.pi / 2, -1 * np.pi, a)
  qc.u(np.pi / 2, -1 * np.pi / 2, np.pi, b)
  qc.cx(a, b)
  qc.u(np.pi / 2, 0, 3 * np.pi / 2, a)
  qc.u(np.pi / 2, 3 * np.pi / 2, 0, b)
  qc.cx(a, b)
  qc.u(np.pi / 2, 0, 0, a)
  qc.u(np.pi, np.pi / 4, -1 * np.pi / 4, b)

  qc.rxx(0.6493842217860086, a, b)
  qc.ryy(-1.3596805297028691, a, b)
  qc.rzz(2.8768998605185647, a, b)

# xy
  qc.rz(3 * np.pi / 4, a)
  qc.rz(-3 * np.pi / 4, b)
  qc.rx(np.pi / 2, a)
  qc.rx(np.pi / 2, b)
  qc.cz(a, b)
  qc.rz(-1 * np.pi / 2, a)
  qc.rz(np.pi / 2, b)
  qc.rx(np.pi / 2, a)
  qc.rx(np.pi / 2, b)
  qc.rz(2.7463195704599936 / 2, a)
  qc.rz(2.7463195704599936 / 2, b)
  qc.rx(-1 * np.pi / 2, a)
  qc.rx(-1 * np.pi / 2, b)
  qc.cz(a, b)
  qc.rz(-1 * np.pi / 2, a)
  qc.rz(-1 * np.pi / 2, b)
  qc.rx(np.pi / 2, a)
  qc.rx(-1 * np.pi / 2, b)
  qc.rz(np.pi / 4, a)
  qc.rz(3 * np.pi / 4, b)

  qc.append(MSGate((-2.9565772286362133) / (2*np.pi), (0.9051623980385868) / (2*np.pi)), [a, b])

# cr2
  qc.cp(np.pi / 2, a, b)


# cr4
  qc.cp(np.pi / 4, a, b)


# cr8
  qc.cp(np.pi / 8, a, b)


# crx
  qc.cu(-0.9375412312498308, -1 * np.pi / 2, np.pi / 2, 0, a, b)


# cry
  qc.u(-0.08058252005457645 / 2, 0, 0, b)
  qc.cx(a, b)
  qc.u(-1 * -0.08058252005457645 / 2, 0, 0, b)
  qc.cx(a, b)

  qc.crz(0.3531826317821056, a, b)
  qc.cp(2.364691146335632, a, b)

# cu2
  qc.cu(np.pi / 2, 1.3039932052205492, 2.6610590045655966, 0, a, b)

  qc.cu(2.4438418503577237, 0.12036689657265498, 1.22113022887996, 0, a, b)

# cs
  qc.cp(np.pi / 2, a, b)


# ct
  qc.cp(np.pi / 4, a, b)


# csdg
  qc.cp(-1 * np.pi / 2, a, b)


# ctdg
  qc.cp(-1 * np.pi / 4, a, b)

  qc.ccx(a, b, c)
  qc.cswap(a, b, c)
  qc.csrswap(a, b, c)
  qc.reset(a)

qc = QuantumCircuit()

q = QuantumRegister(3, 'q')
c = ClassicalRegister(3, 'c')

qc.add_register(q)
qc.add_register(c)

sub(qc, q[0], q[1], q[2])
qc.measure(q[0], c[0])
qc.measure(q[1], c[1])
qc.measure(q[2], c[2])

qc = transpile(qc, backend)
job = execute(qc, backend=backend, shots=shots)
job_result = job.result()
print(job_result.get_counts(qc))
