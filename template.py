from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index/<name>')
def index(name='Danilo'):
	age = 19
	my_list = [1,2,3,4,5,6,7] 
	return render_template('index.html', nombre=name, age=age, list=my_list)

if __name__ == '__main__':
 app.run(debug = True) 