import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(1)
  u3(2.2280239390326413, -2.6835813463878475, -2.7058560853257885, q[0])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
