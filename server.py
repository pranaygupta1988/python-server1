from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["Get"])
def root():
    return "<h1>Welcome to Python Flask Application</h1>"

@app.route("/version", methods=["Get"])
def version():
    return "<h1>Version 1.6</h1>"

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)
