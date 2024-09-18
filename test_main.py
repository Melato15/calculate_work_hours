import unittest
from main import CalcularHorasTrabalhadas

class TestHorasTrabalhadas(unittest.TestCase):
    
  def test_calculo_horas_trabalhadas(self):
    self.assertEqual(CalcularHorasTrabalhadas('0900', '1700', '0100'), '7 horas e 0 minutos')

    self.assertEqual(CalcularHorasTrabalhadas('1700', '0900', '0100'), '7 horas e 0 minutos')

    self.assertEqual(CalcularHorasTrabalhadas('0900', '1700', '0000'), '8 horas e 0 minutos')

    self.assertEqual(CalcularHorasTrabalhadas('0900', '1700', '0800'), '0 horas e 0 minutos')

    self.assertEqual(CalcularHorasTrabalhadas('0900', '1300', '0015'), '4 horas e 15 minutos')

if __name__ == '__main__':
    unittest.main()
