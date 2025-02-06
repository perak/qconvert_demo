import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)

  # iswap
  u3(np.pi / 2, -1 * np.pi / 2, -1 * np.pi, q[0])
  u3(np.pi / 2, -1 * np.pi / 2, np.pi, q[1])
  cx(q[0], q[1])
  u3(np.pi / 2, 0, 3 * np.pi / 2, q[0])
  u3(np.pi / 2, 3 * np.pi / 2, 0, q[1])
  cx(q[0], q[1])
  u3(np.pi / 2, 0, 0, q[0])
  u3(np.pi, np.pi / 4, -1 * np.pi / 4, q[1])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
