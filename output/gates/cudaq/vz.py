import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # vz
  rz(1.654024592863446, q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
