from flask import Flask

app = Flask(__name__)

@app.route("/sum/<x>/<y>")
def hello(x, y):
    sum = x+y
    return {"result":sum}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)