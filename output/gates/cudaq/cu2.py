import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)

  # cu2
  u3.ctrl(np.pi / 2, 1.531863483854199, -1.394430892639087, [q[0]], q[1])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
