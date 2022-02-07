from flask import Flask, render_template, jsonify, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/aircadia')
def aaa():
    return "Hello, AirCADia!"


if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(debug=True)