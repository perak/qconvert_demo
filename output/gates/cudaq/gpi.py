import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # gpi
  u3(np.pi, 1.9536774250959432, np.pi - 1.9536774250959432, q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
