from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from quantastica.encoder_decoder import encode_input, decode_output
import numpy as np

backend = Aer.get_backend("qasm_simulator")

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

  qc = QuantumCircuit()

  q = QuantumRegister(4, 'q')

  qc.add_register(q)

  input_data_row = { "a": a, "b": b }
  input_qasm = encode_input(input_data_row, input_encoding)
  input_qc = QuantumCircuit()
  input_qc = input_qc.from_qasm_str(input_qasm)
  qc = qc.compose(input_qc)
  qc.barrier()

  qc.x(q[0])
  qc.x(q[1])
  qc.x(q[2])
  qc.x(q[3])

  qc.measure_all(q)

  job = execute(qc, backend=backend, shots=shots)
  job_result = job.result()
  counts = job_result.get_counts(qc)

  output_data_row = decode_output(counts, output_decoding, unpack_values=True)
  return output_data_row
