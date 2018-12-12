from flask import Flask, jsonify, request
import funcionesbasicasDB

app = Flask(__name__)

# Ruta despliegue del servicio
@app.route('/', methods = ['GET']) 
def inicio():
	return jsonify(status="OK")

# Ruta para el hito 4 (Contenedor Docker)
@app.route('/status', methods = ['GET']) 
def status():
	return jsonify(status="OK")

# Si usas el método delete borra el último partido de la jornada
@app.route('/jornada/<n>', methods = ['GET','DELETE','PUT'])
def partidos(n):
	p=funcionesbasicasDB.Partidos()
	datos=[]
	if request.method == 'PUT':
		json_data = request.get_json()
		partido = json_data['partido']
		datos=p.setPartido(int(n),partido)
	if request.method == 'DELETE':
		datos=p.delPartido(int(n))
	if request.method == 'GET':
		datos=p.getPartidos(int(n))

	return jsonify(partidos=datos)
    
@app.route('/partido/<n>/jornada/<jornada>', methods = ['GET'])
def partido(jornada,n):
	p=funcionesbasicasDB.Partidos()
	datos=[]
	if request.method == 'GET':
		datos=p.getPartido(int(n),int(jornada))

	return jsonify(partido=datos)

# Si usas el método delete borra la última apuesta del usuario
# Método post añade una apuesta a un usuario o añade un usuario con esa apuesta
@app.route('/apuesta/<usuario>', methods = ['GET','DELETE','POST'])
def apuesta(usuario):
	p=funcionesbasicasDB.Apuestas()
	datos = []
	if request.method == 'DELETE':
		datos=p.delApuesta(usuario)
	if request.method == 'GET':
		datos=p.getApuestas(usuario)
	if request.method == 'POST':
		json_data = request.get_json()
		partido = json_data['partido']
		resultado = json_data['resultado']
		datos=p.setApuestas(usuario,partido,resultado)
	
	return jsonify(apuestas=datos)

# Función que te muestra todos los apostantes
@app.route('/apostantes', methods = ['GET'])
def apostantes():
	p=funcionesbasicasDB.Apuestas()
	datos = []
	if request.method == 'GET':
		datos=p.getApostantes()
	
	return jsonify(apostantes=datos)

# Función que elimina un apostante
@app.route('/apostante/<usuario>', methods = ['DELETE'])
def delApostante(usuario):
	p=funcionesbasicasDB.Apuestas()
	datos = []
	if request.method == 'DELETE':
		datos=p.delApostante(usuario)
	
	return jsonify(apostante=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)