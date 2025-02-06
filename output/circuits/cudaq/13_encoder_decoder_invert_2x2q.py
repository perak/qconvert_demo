import cudaq
from quantastica.encoder_decoder import encode_input, decode_output
import numpy as np

shots = 1024

def my_function(a, b):
  input_encoding = {
      "type": "basis",
      "qubitOffset": 0,
      "colDefs": [
          {
              "name": "a",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 3,
              "bits": 2
          },
          {
              "name": "b",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 3,
              "bits": 2
          }
      ]
  }

  output_decoding = {
      "type": "basis",
      "qubitOffset": 0,
      "colDefs": [
          {
              "name": "c",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 3,
              "bits": 2
          },
          {
              "name": "d",
              "structure": "scalar",
              "dimensions": [],
              "type": "integer",
              "min": 0,
              "max": 3,
              "bits": 2
          }
      ]
  }

  @cudaq.kernel
  def circuit():
    q = cudaq.qvector(4)
    input_data_row = { "a": a, "b": b }
    input_qasm = encode_input(input_data_row, input_encoding)
    # !!! CREATE KERNEL FROM QASM: NOT SUPPORTED YET.
    x(q[0])
    x(q[1])
    x(q[2])
    x(q[3])

    mz()

  counts = cudaq.sample(circuit, shots_count=shots)
  output_data_row = decode_output(counts, output_decoding, unpack_values=True)
  return output_data_row
