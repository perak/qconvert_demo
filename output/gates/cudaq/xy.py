import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)

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
  rz(-1.9399957263832133 / 2, q[0])
  rz(-1.9399957263832133 / 2, q[1])
  rx(-1 * np.pi / 2, q[0])
  rx(-1 * np.pi / 2, q[1])
  cz(q[0], q[1])
  rz(-1 * np.pi / 2, q[0])
  rz(-1 * np.pi / 2, q[1])
  rx(np.pi / 2, q[0])
  rx(-1 * np.pi / 2, q[1])
  rz(np.pi / 4, q[0])
  rz(3 * np.pi / 4, q[1])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
