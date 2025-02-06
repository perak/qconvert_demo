import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(3)
  swap.ctrl([q[0]], q[1], q[2])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
