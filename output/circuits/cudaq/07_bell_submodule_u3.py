import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def bell(q_0: cudaq.qubit, q_1: cudaq.qubit):
  u3(1.570796326794896, 1.570796326794897, 2.968731284043518, q_0)
  crx(3.141592653589794, q_0, q_1)

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  bell(q[0], q[1])
  mz(q[0])
  mz(q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
