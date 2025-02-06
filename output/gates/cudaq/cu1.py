import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)

  # cu1
  u3.ctrl(0, 0, 1.5970061256170043, [q[0]], q[1])
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
