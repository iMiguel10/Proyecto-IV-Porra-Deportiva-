#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
#import pymongo

class Partidos:

	def __init__(self):

		# Archivos JSON
		with open('../src/datos.json', 'r') as file:
			self.data = json.load(file)

		"""
		# BD Mongo
		client = pymongo.MongoClient()
		db = client.porra         # base de datos
		self.jornadas = db.jornadas    # colección
		self.apuestas = db.apuestas    # colección
		"""

	# Función que nos develve una lista con los partidos de una jornada
	def getPartidos(self,jornada):	
		partidos = []
		try:
			jornada = abs(int(jornada))
			# print(f"Jornada {jornada}")
		
			for i in self.data[jornada-1]["partidos"]:
				partidos.append(i["equipos"])
		
			"""
			# BD Mongo
			j = self.jornadas.find({"numero":jornada})
			partidos = j["partidos"]
			"""
		except:
			partidos = False
		
		return partidos

	# Función que nos develve un partido de una jornada
	def getPartido(self, partido, jornada):
		partidos = self.getPartidos(jornada)
		if partidos:
			try:
				return partidos[partido]
			except:
				return False
		else: return False

	# Función que crea un partido en una jornada
	def setPartido(self, jornada, partido):
		#print(len(self.data))
		if type(jornada) != int: return False
		if len(self.data) >= abs(jornada):
			try:
				jornada=abs(jornada)
				self.data[jornada-1]["partidos"].append({'equipos':partido})
				with open('../src/datos.json', 'w') as file:
					json.dump(self.data, file)
				return True
			except:
				return False
		else:
			return False

	# Función que borra el último partido de una jornada concreta
	def delPartido(self, jornada):
		#print(len(self.data))
		if type(jornada) != int: return False
		if len(self.data) >= abs(jornada):
			try:
				jornada=abs(jornada)
				self.data[jornada-1]["partidos"].pop(len(self.data[jornada-1]["partidos"])-1)
				with open('../src/datos.json', 'w') as file:
					json.dump(self.data, file)
				return True
			except:
				return False
		else:
			return False

class Apuestas:

	def __init__(self):
		with open('../src/apuestas.json', 'r') as file:
			self.ap = json.load(file)

	# Función que nos devuelve las apuestas de un usuario
	def getApuestas(self, usuario):
		apuestas = []
		for i in self.ap:
			if i["usuario"] == usuario:
				for j in i["apuesta"]:
					apuestas.append(j)
		if not apuestas: apuestas = False 
		return apuestas