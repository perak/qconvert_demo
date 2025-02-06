import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)
  ry(2.2616237226970117, q[0])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
