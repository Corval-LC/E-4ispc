import unittest
from Lavavajillas import Lavavajillas

class TestLavavajillas(unittest.TestCase):
    def setUp(self):
        self.lavavajillas = Lavavajillas()

    def test_iniciar_ciclo(self):
        self.assertEqual(self.lavavajillas.iniciar_ciclo(), "El lavavajillas está apagado")
        self.lavavajillas.encendido = True
        self.assertEqual(self.lavavajillas.iniciar_ciclo(), "No hay detergente")
        self.lavavajillas.anadir_detergente(50)
        self.assertEqual(self.lavavajillas.iniciar_ciclo(), "Ciclo de lavado iniciado")

    def test_anadir_detergente(self):
        self.assertEqual(self.lavavajillas.anadir_detergente(50), "Nivel de detergente actual: 50%")
        self.assertEqual(self.lavavajillas.anadir_detergente(60), "Nivel de detergente actual: 100%")
        self.assertEqual(self.lavavajillas.anadir_detergente(-10), "Cantidad inválida")

    def test_ajustar_temperatura(self):
        self.assertEqual(self.lavavajillas.ajustar_temperatura(50), "Temperatura ajustada a 50°C")
        self.assertEqual(self.lavavajillas.ajustar_temperatura(80), "Temperatura fuera de rango")

if __name__ == '__main__':
    unittest.main()
