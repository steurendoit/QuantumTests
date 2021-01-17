import qiskit
from qiskit import IBMQ
from qiskit import Aer
from qiskit.tools.visualization import plot_histogram
import matplotlib as mpl
mpl.use("TkAgg")
import matplotlib.pyplot as plt

clear = False

if clear and not IBMQ.stored_account() is None:
    IBMQ.delete_account()
    print("Account cleared!")
token = "746644d897c000cb3df3ad4207ab3b892563771823df485921c9f6f5159b86fa0da28e1789e0f9da7a88b181a250e8be8bcd89881747518113174a88e00638be"
IBMQ.save_account(token, overwrite=True)
IBMQ.load_account()
print("IBMQ providers list")
print(IBMQ.providers())
provider = IBMQ.get_provider(hub="ibm-q")
print("\nand here available backends on IBM hq (sw emulator or IBM Q computer")
print((provider.backends()))
print("\nand here local backend given by Aer")
print(Aer.backends())
backend = provider.get_backend("ibmq_qasm_simulator")

q = qiskit.QuantumRegister(5)
c = qiskit.ClassicalRegister(5)
qc = qiskit.QuantumCircuit(q, c)
qc.measure_all()
job = qiskit.execute(qc, backend=backend)
plot_histogram(job.result().get_counts(qc))
plt.show()
