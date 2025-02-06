import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def bell(q_0: cudaq.qubit, q_1: cudaq.qubit):
  h(q_0)
  cx(q_0, q_1)

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  bell(q[0], q[1])
  mz(q[0])
  mz(q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
