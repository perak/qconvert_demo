import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # gpi2
  u3(np.pi / 2, -0.5898269553487046 - (np.pi / 2), (np.pi / 2) - -0.5898269553487046, q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
