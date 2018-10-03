#!/usr/bin/python
# -*- coding: utf-8 -*-

import json

class FuncionesBasicas:

	def __init__(self):
		with open('apuestas.json', 'r') as file:
			self.ap = json.load(file)

		with open('datos.json', 'r') as file:
			self.data = json.load(file)

	def getPartidos(self,jornada):	
		partidos = []
		try:
			jornada = abs(int(jornada))
			# print(f"Jornada {jornada}")
			for i in self.data[jornada-1]["partidos"]:
				partidos.append(i["equipos"])
		except:
			partidos = False

		return partidos


	def getPartido(self, partido, jornada):
		partidos = self.getPartidos(jornada)
		if partidos:
			try:
				return partidos[partido]
			except:
				return False
		else: return False

	def getApuestas(self, usuario):
		apuestas = []
		for i in self.ap:
			if i["usuario"] == usuario:
				for j in i["apuesta"]:
					apuestas.append(j)
		if not apuestas: apuestas = False 
		return apuestas
