import cudaq
import numpy as np

shots = 1024

params = [
  1.570796326794896, # var0
  1.570796326794897, # var1
  2.968731284043518, # var2
  3.141592653589794 # var3
]

@cudaq.kernel
def circuit(params: list[float]):
  q = cudaq.qvector(2)
  u3(params[0], params[1], params[2], q[0])
  crx(params[3], q[0], q[1])
  mz(q[0])
  mz(q[1])

counts = cudaq.sample(circuit, params, shots_count=shots)
print(counts)
