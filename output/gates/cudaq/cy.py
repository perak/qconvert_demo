import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  cy(q[0], q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
