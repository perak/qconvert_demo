import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)

  # cr8
  
  # cu1
  u3.ctrl(0, 0, np.pi / 8, [q[0]], q[1])
  
  

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
