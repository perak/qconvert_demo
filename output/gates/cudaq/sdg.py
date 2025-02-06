import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)
  sdg(q[0])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
