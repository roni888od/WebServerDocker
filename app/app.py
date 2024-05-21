from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to My Simple Web App</h1>'

@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')
    return f'<h1>Hello, {name}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)