import cudaq
import numpy as np

shots = 1024

@cudaq.kernel
def sub(var0: float, var1: float, var2: float, var3: float, q_0: cudaq.qubit, q_1: cudaq.qubit):
  u3(var0, var1, var2, q_0)
  crx(var3, q_0, q_1)

@cudaq.kernel
def circuit():
  q = cudaq.qvector(2)
  sub(1.570796326794896, 1.570796326794897, 2.968731284043518, 3.141592653589794, q[0], q[1])
  mz(q[0])
  mz(q[1])

counts = cudaq.sample(circuit, shots_count=shots)
print(counts)
