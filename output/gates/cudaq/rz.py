import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)
  rz(1.1876383429161939, q[0])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
