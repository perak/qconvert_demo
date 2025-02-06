import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # r8
  u3(0, 0, np.pi / 8, q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
