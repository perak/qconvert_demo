import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # u2
  u3(np.pi / 2, 2.854068541068436, -1.2300736671220556, q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
