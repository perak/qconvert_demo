import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # srndg
  h(q[0])
  u3(0, 0, -np.pi / 2, q[0])
  h(q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
