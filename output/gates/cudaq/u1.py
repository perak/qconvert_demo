import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)

  # u1
  u3(0, 0, -1.7626454156696476, q[0])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
