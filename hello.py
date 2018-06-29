from flask import Flask, render_template
from flask_assets import Bundle, Environment

app = Flask(__name__)

js = Bundle('home.js', 'add.js', 'subtract.js', output='gen/main.js', filters='jsmin')

assets = Environment(app)

assets.register('main_js', js)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
