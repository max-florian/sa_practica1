from flask import Flask
app = Flask(__name__)

@app.route("/")
    
def hello():
    return "Hello Practica 1 de Software Avanzado xd!"

if __name__ == "__main__":
    app.run()