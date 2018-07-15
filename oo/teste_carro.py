from unittest import TestCase

from oo.carro import Motor, Direcao, Carro


class CarroTestCase(TestCase):
    def teste_direcao(self):
        direcao = Direcao()
        direcao.girar_a_esquerda()
        self.assertEqual(None, direcao.girar_a_esquerda())

        direcao.girar_a_direita()
        self.assertEqual(None, direcao.girar_a_direita())

    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)
