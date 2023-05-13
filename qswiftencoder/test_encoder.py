from unittest import TestCase
from qswiftencoder.encoder import QSwiftCircuitEncoder, QSwiftStringEncoder, TimeOperator, SwiftOperator
from qwrapper.operator import PauliObservable
from qwrapper.circuit import init_circuit


class TestQSwiftCircuitEncoder(TestCase):
    def test_encode(self):
        operators = []
        for _ in range(10):
            operators.append(TimeOperator(0))
        operators.append(SwiftOperator(0, 0))
        s_encoder = QSwiftStringEncoder()
        code = s_encoder.encode(2.2, operators)
        self.assertEquals("2.2 T0 T0 T0 T0 T0 T0 T0 T0 T0 T0 S0-0", code)

        paulis = [PauliObservable("XXXIIIII")]
        encoder = QSwiftCircuitEncoder(0, [1, 2, 3, 4, 5, 6, 7, 8], paulis, 0.1)

        qc = init_circuit(9, "qulacs")
        sign, qc = encoder.encode(qc, code)

        obs = PauliObservable("XZZZIIIII")
        self.assertEquals(0, obs.exact_value(qc))
