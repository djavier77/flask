from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hola Mundo.'

@app.route('/params')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'Este es un valor por default', num =  'S/N'):
	return 'El parametro es : {}, {} '.format(name,num)

if __name__ == '__main__':
 app.run(debug = True) 