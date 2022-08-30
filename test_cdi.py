import unittest
import cdi

class TestCdi(unittest.TestCase):

    def test_calculo_rendimento_poupanca(self):
        self.assertAlmostEqual(cdi.calculo_rendimento_poupanca(0.086), 0.0617)
        self.assertAlmostEqual(cdi.calculo_rendimento_poupanca(0.05), 0.05*.7)

    def test_year2month(self):
        self.assertAlmostEqual(cdi.year2month(0.12),0.94887929)

    def test_day2year(self):
        self.assertAlmostEqual(cdi.day2year(0.000657),18,2)
    
    def test_jc(self):
        self.assertAlmostEqual(cdi.jc(0.1,1,1),0.1,2)
        self.assertAlmostEqual(cdi.jc(0.005,10,1),0.0511401,2)

    def test_doublePrincipal(self):
        self.assertAlmostEqual(cdi.doublePrincipal(0.007576),91.84,2)

if __name__ == "__main__":
    unittest.main()
