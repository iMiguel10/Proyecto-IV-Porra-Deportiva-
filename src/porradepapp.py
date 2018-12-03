from flask import Flask, jsonify, request
import funcionesbasicas

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
	p=funcionesbasicas.Partidos()
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
	p=funcionesbasicas.Partidos()
	datos=[]
	if request.method == 'GET':
		datos=p.getPartido(int(n),int(jornada))

	return jsonify(partido=datos)

@app.route('/apuesta/<usuario>', methods = ['GET'])
def apuesta(usuario):
	p=funcionesbasicas.Apuestas()
	datos=p.getApuestas(usuario)
	return jsonify(apuestas=datos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)