import cudaq
import numpy as np

cudaq.register_operation("i", np.array([[1, 0], [0, 1]]))
cudaq.register_operation("csrswap", np.array([[1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0],[0,0,0,0,0,0.5 * (1 + 1j),0.5 * (1 - 1j),0],[0,0,0,0,0,0.5 * (1 - 1j),0.5 * (1 + 1j),0],[0,0,0,0,0,0,0,1]]))

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(3)
  i(q[0])
  x(q[0])
  y(q[0])
  z(q[0])
  h(q[0])

  # srn
  h(q[0])
  u3(0, 0, np.pi / 2, q[0])
  h(q[0])
  

  # srndg
  h(q[0])
  u3(0, 0, -np.pi / 2, q[0])
  h(q[0])
  
  s(q[0])
  t(q[0])

  # r8
  u3(0, 0, np.pi / 8, q[0])
  
  rx(-2.4522873150317515, q[0])
  ry(-0.8230054351172829, q[0])
  rz(-0.721964051391391, q[0])

  # u1
  u3(0, 0, -0.43066855201756526, q[0])
  

  # u2
  u3(np.pi / 2, 2.592797810960824, 0.5111537159291752, q[0])
  
  u3(-2.6866081144080782, 0.8503837523656363, 0.9496083262543298, q[0])
  s(q[0])
  t(q[0])
  sdg(q[0])
  tdg(q[0])

  # gpi
  u3(np.pi, -1.4255817494482401, np.pi - -1.4255817494482401, q[0])
  

  # gpi2
  u3(np.pi / 2, 1.1344820948531975 - (np.pi / 2), (np.pi / 2) - 1.1344820948531975, q[0])
  

  # vz
  rz(-2.0290277644863393, q[0])
  
  cx(q[0], q[1])
  cy(q[0], q[1])
  cz(q[0], q[1])
  ch(q[0], q[1])

  # csrn
  h(q[1])
  
  # cu1
  u3.ctrl(0, 0, np.pi / 2, [q[0]], q[1])
  
  h(q[1])
  
  swap(q[0], q[1])

  # srswap
  u3(np.pi / 2, np.pi / 2, -1 * np.pi, q[0])
  u3(np.pi / 2, -1 * np.pi / 2, np.pi, q[1])
  cx(q[0], q[1])
  u3(np.pi / 4, -1 * np.pi / 2, -1 * np.pi / 2, q[0])
  u3(np.pi / 2, 0, 7 * np.pi / 4, q[1])
  cx(q[0], q[1])
  u3(np.pi / 4, -1 * np.pi, -1 * np.pi / 2, q[0])
  u3(np.pi / 2, np.pi, np.pi / 2, q[1])
  cx(q[0], q[1])
  u3(np.pi / 2, 0, -3 * np.pi / 2, q[0])
  u3(np.pi / 2, np.pi / 2, 0, q[1])
  

  # iswap
  u3(np.pi / 2, -1 * np.pi / 2, -1 * np.pi, q[0])
  u3(np.pi / 2, -1 * np.pi / 2, np.pi, q[1])
  cx(q[0], q[1])
  u3(np.pi / 2, 0, 3 * np.pi / 2, q[0])
  u3(np.pi / 2, 3 * np.pi / 2, 0, q[1])
  cx(q[0], q[1])
  u3(np.pi / 2, 0, 0, q[0])
  u3(np.pi, np.pi / 4, -1 * np.pi / 4, q[1])
  
  xx(0.6493842217860086, q[0], q[1])
  yy(-1.3596805297028691, q[0], q[1])
  zz(2.8768998605185647, q[0], q[1])

  # xy
  rz(3 * np.pi / 4, q[0])
  rz(-3 * np.pi / 4, q[1])
  rx(np.pi / 2, q[0])
  rx(np.pi / 2, q[1])
  cz(q[0], q[1])
  rz(-1 * np.pi / 2, q[0])
  rz(np.pi / 2, q[1])
  rx(np.pi / 2, q[0])
  rx(np.pi / 2, q[1])
  rz(2.7463195704599936 / 2, q[0])
  rz(2.7463195704599936 / 2, q[1])
  rx(-1 * np.pi / 2, q[0])
  rx(-1 * np.pi / 2, q[1])
  cz(q[0], q[1])
  rz(-1 * np.pi / 2, q[0])
  rz(-1 * np.pi / 2, q[1])
  rx(np.pi / 2, q[0])
  rx(-1 * np.pi / 2, q[1])
  rz(np.pi / 4, q[0])
  rz(3 * np.pi / 4, q[1])
  
  ms(-2.9565772286362133, 0.9051623980385868, q[0], q[1])
  cs(q[0], q[1])
  ct(q[0], q[1])

  # cr8
  
  # cu1
  u3.ctrl(0, 0, np.pi / 8, [q[0]], q[1])
  
  
  crx(-0.9375412312498308, q[0], q[1])
  cry(-0.08058252005457645, q[0], q[1])
  crz(0.3531826317821056, q[0], q[1])

  # cu1
  u3.ctrl(0, 0, 2.364691146335632, [q[0]], q[1])
  

  # cu2
  u3.ctrl(np.pi / 2, 1.3039932052205492, 2.6610590045655966, [q[0]], q[1])
  
  u3.ctrl(2.4438418503577237, 0.12036689657265498, 1.22113022887996, [q[0]], q[1])
  cs(q[0], q[1])
  ct(q[0], q[1])

  # csdg
  u3.ctrl(0, 0, -np.pi / 2, [q[0]], q[1])
  

  # ctdg
  u3.ctrl(0, 0, -np.pi / 4, [q[0]], q[1])
  
  x.ctrl([q[0], q[1]], q[2])
  swap.ctrl([q[0]], q[1], q[2])
  csrswap(q[0], q[1], q[2])
  reset(q[0])
  mz(q[0])
  mz(q[1])
  mz(q[2])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
