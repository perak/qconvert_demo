import cudaq
import numpy as np

cudaq.register_operation("i", np.array([[1, 0], [0, 1]]))
cudaq.register_operation("csrswap", np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0.5 * (1 + 1j),0.5 * (1 - 1j),0],[0,0,0,0,0,0.5 * (1 - 1j),0.5 * (1 + 1j),0],[0,0,0,0,0,0,0,1]]))

shots = 1024

@cudaq.kernel
def sub(q_0: cudaq.qubit, q_1: cudaq.qubit, q_2: cudaq.qubit):
  i(q_0)
  x(q_0)
  y(q_0)
  z(q_0)
  h(q_0)

  # srn
  h(q_0)
  u3(0, 0, np.pi / 2, q_0)
  h(q_0)
  

  # srndg
  h(q_0)
  u3(0, 0, -np.pi / 2, q_0)
  h(q_0)
  
  s(q_0)
  t(q_0)

  # r8
  u3(0, 0, np.pi / 8, q_0)
  
  rx(-2.4522873150317515, q_0)
  ry(-0.8230054351172829, q_0)
  rz(-0.721964051391391, q_0)

  # u1
  u3(0, 0, -0.43066855201756526, q_0)
  

  # u2
  u3(np.pi / 2, 2.592797810960824, 0.5111537159291752, q_0)
  
  u3(-2.6866081144080782, 0.8503837523656363, 0.9496083262543298, q_0)
  s(q_0)
  t(q_0)
  sdg(q_0)
  tdg(q_0)

  # gpi
  u3(np.pi, -1.4255817494482401, np.pi - -1.4255817494482401, q_0)
  

  # gpi2
  u3(np.pi / 2, 1.1344820948531975 - (np.pi / 2), (np.pi / 2) - 1.1344820948531975, q_0)
  

  # vz
  rz(-2.0290277644863393, q_0)
  
  cx(q_0, q_1)
  cy(q_0, q_1)
  cz(q_0, q_1)
  ch(q_0, q_1)

  # csrn
  h(q_1)
  
  # cu1
  u3.ctrl(0, 0, np.pi / 2, [q_0], q_1)
  
  h(q_1)
  
  swap(q_0, q_1)

  # srswap
  u3(np.pi / 2, np.pi / 2, -1 * np.pi, q_0)
  u3(np.pi / 2, -1 * np.pi / 2, np.pi, q_1)
  cx(q_0, q_1)
  u3(np.pi / 4, -1 * np.pi / 2, -1 * np.pi / 2, q_0)
  u3(np.pi / 2, 0, 7 * np.pi / 4, q_1)
  cx(q_0, q_1)
  u3(np.pi / 4, -1 * np.pi, -1 * np.pi / 2, q_0)
  u3(np.pi / 2, np.pi, np.pi / 2, q_1)
  cx(q_0, q_1)
  u3(np.pi / 2, 0, -3 * np.pi / 2, q_0)
  u3(np.pi / 2, np.pi / 2, 0, q_1)
  

  # iswap
  u3(np.pi / 2, -1 * np.pi / 2, -1 * np.pi, q_0)
  u3(np.pi / 2, -1 * np.pi / 2, np.pi, q_1)
  cx(q_0, q_1)
  u3(np.pi / 2, 0, 3 * np.pi / 2, q_0)
  u3(np.pi / 2, 3 * np.pi / 2, 0, q_1)
  cx(q_0, q_1)
  u3(np.pi / 2, 0, 0, q_0)
  u3(np.pi, np.pi / 4, -1 * np.pi / 4, q_1)
  
  xx(0.6493842217860086, q_0, q_1)
  yy(-1.3596805297028691, q_0, q_1)
  zz(2.8768998605185647, q_0, q_1)

  # xy
  rz(3 * np.pi / 4, q_0)
  rz(-3 * np.pi / 4, q_1)
  rx(np.pi / 2, q_0)
  rx(np.pi / 2, q_1)
  cz(q_0, q_1)
  rz(-1 * np.pi / 2, q_0)
  rz(np.pi / 2, q_1)
  rx(np.pi / 2, q_0)
  rx(np.pi / 2, q_1)
  rz(2.7463195704599936 / 2, q_0)
  rz(2.7463195704599936 / 2, q_1)
  rx(-1 * np.pi / 2, q_0)
  rx(-1 * np.pi / 2, q_1)
  cz(q_0, q_1)
  rz(-1 * np.pi / 2, q_0)
  rz(-1 * np.pi / 2, q_1)
  rx(np.pi / 2, q_0)
  rx(-1 * np.pi / 2, q_1)
  rz(np.pi / 4, q_0)
  rz(3 * np.pi / 4, q_1)
  
  ms(-2.9565772286362133, 0.9051623980385868, q_0, q_1)
  cs(q_0, q_1)
  ct(q_0, q_1)

  # cr8
  
  # cu1
  u3.ctrl(0, 0, np.pi / 8, [q_0], q_1)
  
  
  crx(-0.9375412312498308, q_0, q_1)
  cry(-0.08058252005457645, q_0, q_1)
  crz(0.3531826317821056, q_0, q_1)

  # cu1
  u3.ctrl(0, 0, 2.364691146335632, [q_0], q_1)
  

  # cu2
  u3.ctrl(np.pi / 2, 1.3039932052205492, 2.6610590045655966, [q_0], q_1)
  
  u3.ctrl(2.4438418503577237, 0.12036689657265498, 1.22113022887996, [q_0], q_1)
  cs(q_0, q_1)
  ct(q_0, q_1)

  # csdg
  u3.ctrl(0, 0, -np.pi / 2, [q_0], q_1)
  

  # ctdg
  u3.ctrl(0, 0, -np.pi / 4, [q_0], q_1)
  
  x.ctrl([q_0, q_1], q_2)
  swap.ctrl([q_0], q_1, q_2)
  csrswap(q_0, q_1, q_2)
  reset(q_0)

@cudaq.kernel
def circuit():
  q = cudaq.qvector(3)
  sub(q[0], q[1], q[2])
  mz(q[0])
  mz(q[1])
  mz(q[2])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
