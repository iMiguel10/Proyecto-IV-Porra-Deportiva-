#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pymongo

class Partidos:

	def __init__(self):

		# BD Mongo "mongodb+srv://prueba:i3FMWub6otusvSjp@cluster0-yij5h.azure.mongodb.net/admin"
		client = pymongo.MongoClient("mongodb+srv://porra:porraIV@cluster0-yij5h.azure.mongodb.net/porradeportiva")
		db = client.porradeportiva
		self.jornadas = db.jornadas    # colección

	# Función que nos develve una lista con los partidos de una jornada
	def getPartidos(self,jornada):	
		partidos = []
		
		try:
			# Con esto comprobamos que es un número entero
			jornada = abs(int(jornada)) 
			# Lo devolvemos a string
			jornada = str(jornada)
	
			j = self.jornadas.find({'numero':jornada})
			for p in j[0]["partidos"]:
				partidos.append(p["equipos"])
		
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
		if self.jornadas.find().count() >= abs(jornada):
			try:
				# Con esto comprobamos que es un número entero
				jornada = abs(int(jornada)) 
				# Lo devolvemos a string
				jornada = str(jornada)

				j = self.jornadas.find({'numero':jornada})
				p = j[0]["partidos"]
				p.append({'equipos':partido})
				self.jornadas.update({'numero':jornada},{'numero':jornada,'partidos':p})
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
				# Con esto comprobamos que es un número entero
				jornada = abs(int(jornada)) 
				# Lo devolvemos a string
				jornada = str(jornada)

				j = self.jornadas.find({'numero':jornada})
				p = j[0]["partidos"]
				p.pop()
				self.jornadas.update({'numero':jornada},{'numero':jornada,'partidos':p})
				return True
			except:
				return False
		else:
			return False

class Apuestas:

	def __init__(self):

		# BD Mongo "mongodb+srv://prueba:i3FMWub6otusvSjp@cluster0-yij5h.azure.mongodb.net/admin"
		client = pymongo.MongoClient("mongodb+srv://porra:porraIV@cluster0-yij5h.azure.mongodb.net/porradeportiva")
		db = client.porradeportiva
		self.apuestas = db.apuestas    # colección


	# Función que nos devuelve las apuestas de un usuario
	def getApostantes(self,):
		
		usuarios = []
		u = self.apuestas.find()
		for a in u:
			usuarios.append(a["usuario"])

		return usuarios

	# Función que nos devuelve las apuestas de un usuario
	def getApuestas(self, usuario):
		
		apuestas = []
		try:
			u = self.apuestas.find({'usuario':usuario})
			for a in u[0]["apuestas"]:
				apuestas.append(a)

		except:
			apuestas = False 
		return apuestas


	# Función que nos devuelve las apuestas de un usuario
	def setApuestas(self, usuario, partido, resultado):

		try:
			apuestas = self.getApuestas(usuario)
			if apuestas:
				apuestas.append({partido:resultado})
				self.apuestas.update({'usuario':usuario},{'usuario':usuario,'apuestas':apuestas})
			else:
				apuestas = []
				apuestas.append({partido:resultado})
				self.apuestas.insert({'usuario':usuario, 'apuestas':apuestas}) 
			apuestas = True
		except:
			apuestas = False 
		return apuestas


	# Función que borra la última apuesta de un usuario
	def delApuesta(self, usuario):
		apuestas = []
		try:
			apuestas = self.getApuestas(usuario)
			# Si el usuario tiene apuestas
			if apuestas:
				apuestas.pop()
				self.apuestas.update({'usuario':usuario},{'usuario':usuario,'apuestas':apuestas})
				apuestas = True
			
			# El usuario no tiene apuestas pero se realiza bien la operación
			else:
				apuestas = True

		except:
			apuestas = False 
		return apuestas