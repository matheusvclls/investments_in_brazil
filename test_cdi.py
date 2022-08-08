import unittest
import cdi

class TestCdi(unittest.TestCase):

    def test_calculo_rendimento_poupanca(self):
        self.assertAlmostEqual(cdi.calculo_rendimento_poupanca(0.086), 0.0617)
        self.assertAlmostEqual(cdi.calculo_rendimento_poupanca(0.05), 0.05*.7)

if __name__ == "__main__":
    unittest.main()
