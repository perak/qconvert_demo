import cudaq
from quantastica.encoder_decoder import encode_input, decode_output
import numpy as np

shots = 1024

@cudaq.kernel
def majority(q_0: cudaq.qubit, q_1: cudaq.qubit, q_2: cudaq.qubit):
  cx(q_2, q_1)
  cx(q_2, q_0)
  x.ctrl([q_0, q_1], q_2)

@cudaq.kernel
def unmaj(q_0: cudaq.qubit, q_1: cudaq.qubit, q_2: cudaq.qubit):
  x.ctrl([q_0, q_1], q_2)
  cx(q_2, q_0)
  cx(q_0, q_1)

def quantum_adder(a, b):
  input_encoding = {
      "type": "basis",
      "qubitOffset": 1,
      "colDefs": [
          {
              "name": "a",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 15,
              "bits": 4
          },
          {
              "name": "b",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 15,
              "bits": 4
          }
      ]
  }

  output_decoding = {
      "type": "basis",
      "qubitOffset": 5,
      "colDefs": [
          {
              "name": "c",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 31,
              "bits": 5
          }
      ]
  }

  @cudaq.kernel
  def circuit():
    q = cudaq.qvector(10)
    input_data_row = { "a": a, "b": b }
    input_qasm = encode_input(input_data_row, input_encoding)
    # !!! CREATE KERNEL FROM QASM: NOT SUPPORTED YET.
    majority(q[0], q[5], q[1])
    majority(q[1], q[6], q[2])
    majority(q[2], q[7], q[3])
    majority(q[3], q[8], q[4])
    cx(q[4], q[9])
    unmaj(q[3], q[8], q[4])
    unmaj(q[2], q[7], q[3])
    unmaj(q[1], q[6], q[2])
    unmaj(q[0], q[5], q[1])
    mz(q[5])
    mz(q[6])
    mz(q[7])
    mz(q[8])
    mz(q[9])

    mz()

  counts = cudaq.sample(circuit, shots_count=shots)
  output_data_row = decode_output(counts, output_decoding, unpack_values=True)
  return output_data_row
