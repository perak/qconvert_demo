import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  u3.ctrl(-2.554803775126938, 0.07538532764859829, 1.3869906544679287, [q[0]], q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
