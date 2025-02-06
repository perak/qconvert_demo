import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  u3(1.570796326794896, 1.570796326794897, 2.968731284043518, q[0])
  crx(3.141592653589794, q[0], q[1])
  mz(q[0])
  mz(q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
