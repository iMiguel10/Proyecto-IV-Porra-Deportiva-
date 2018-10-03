#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import funcionesbasicas

class FuncionesBasicasTest(unittest.TestCase):

    test = funcionesbasicas.FuncionesBasicas()

    def testPartidos(self):
        self.assertEqual(self.test.getPartidos("Cadena"),False,"La jornada debe ser entero")
        self.assertEqual(self.test.getPartidos(2),[unicode('Real Madrid FC - Sevilla FC',"utf-8"),unicode('Atlético de Madrid - FC Barcelona',"utf-8"),unicode('Leganés - Betis',"utf-8")],"La jornada es correcta")

    def testPartido(self):
        self.assertEqual(self.test.getPartido(0,"cadena"),False,"La jornada debe ser entero")
        self.assertEqual(self.test.getPartido("cadena",3),False,"El partido debe ser entero")
        self.assertEqual(self.test.getPartido(1,2),unicode('Atlético de Madrid - FC Barcelona',"utf-8"),"El partido es correcto")

    def testApuestas(self):
        self.assertEqual(self.test.getApuestas("cadena"),False,"Usuario no encontrado")
        self.assertEqual(self.test.getApuestas("luis14"),[{u'Real Madrid FC - FC Barcelona': u'4-0'}, {u'Atl\xe9tico de Madrid - Betis': u'1-1'}, {u'Sevilla FC - Athletic de Bilbao': u'3-2'}],"Apuestas del usuario luis14 son correctas")



if __name__ == '__main__':
    unittest.main()