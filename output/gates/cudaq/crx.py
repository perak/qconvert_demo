import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  crx(0.07976133670952157, q[0], q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
