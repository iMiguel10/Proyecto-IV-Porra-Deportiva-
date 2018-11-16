from flask import Flask, jsonify
import funcionesbasicas

app = Flask(__name__)

# Ruta despliegue del servicio
@app.route('/') 
def inicio():
	return jsonify(status="OK")

# Ruta para el hito 4 (Contenedor Docker)
@app.route('/status') 
def inicio():
	return jsonify(status="OK")

@app.route('/jornada/<n>')
def partidos(n):
	p=funcionesbasicas.Partidos()
	datos=p.getPartidos(n)
	return jsonify(partidos=datos)
    
@app.route('/partido/<n>/jornada/<jornada>')
def partido(jornada,n):
	p=funcionesbasicas.Partidos()
	datos=p.getPartido(int(n),int(jornada))
	return jsonify(partido=datos)

@app.route('/apuesta/<usuario>')
def apuesta(usuario):
	p=funcionesbasicas.Apuestas()
	datos=p.getApuestas(usuario)
	return jsonify(apuestas=datos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)