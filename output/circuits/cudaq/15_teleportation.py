import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def circuit():
  q = cudaq.qvector(3)
  rx(0.785398, q[0])
  h(q[1])
  cx(q[1], q[2])
  cx(q[0], q[1])
  h(q[0])
  mz(q[1])
  x(q[2]).c_if(c1, 1)
  mz(q[0])
  z(q[2]).c_if(c0, 1)

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
