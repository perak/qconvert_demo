from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import execute, Aer
from quantastica.encoder_decoder import encode_input, decode_output
import numpy as np

backend = Aer.get_backend("qasm_simulator")

shots = 1024

def majority(qc, a, b, c):
  qc.cx(c, b)
  qc.cx(c, a)
  qc.ccx(a, b, c)

def unmaj(qc, a, b, c):
  qc.ccx(a, b, c)
  qc.cx(c, a)
  qc.cx(a, b)

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

  qc = QuantumCircuit()

  q = QuantumRegister(10, 'q')
  ans = ClassicalRegister(5, 'ans')

  qc.add_register(q)
  qc.add_register(ans)

  input_data_row = { "a": a, "b": b }
  input_qasm = encode_input(input_data_row, input_encoding)
  input_qc = QuantumCircuit()
  input_qc = input_qc.from_qasm_str(input_qasm)
  qc = qc.compose(input_qc)
  qc.barrier()

  majority(qc, q[0], q[5], q[1])
  majority(qc, q[1], q[6], q[2])
  majority(qc, q[2], q[7], q[3])
  majority(qc, q[3], q[8], q[4])
  qc.cx(q[4], q[9])
  unmaj(qc, q[3], q[8], q[4])
  unmaj(qc, q[2], q[7], q[3])
  unmaj(qc, q[1], q[6], q[2])
  unmaj(qc, q[0], q[5], q[1])
  qc.measure(q[5], ans[0])
  qc.measure(q[6], ans[1])
  qc.measure(q[7], ans[2])
  qc.measure(q[8], ans[3])
  qc.measure(q[9], ans[4])

  qc.measure_all(q)

  job = execute(qc, backend=backend, shots=shots)
  job_result = job.result()
  counts = job_result.get_counts(qc)

  output_data_row = decode_output(counts, output_decoding, unpack_values=True)
  return output_data_row
