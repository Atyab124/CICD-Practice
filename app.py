from flask import Flask, request, jsonify

app = Flask(__name__)

def parse_args():
    try:
        x = float(request.args.get("x", "0"))
        y = float(request.args.get("y", "0"))
        return x, y
    except ValueError:
        return None

@app.route("/add")
def add():
    params = parse_args()
    if not params:
        return jsonify(error="invalid input"), 400
    x, y = params
    return jsonify(result=x + y)

@app.route("/sub")
def sub():
    params = parse_args()
    if not params:
        return jsonify(error="invalid input"), 400
    x, y = params
    return jsonify(result=x - y)

@app.route("/mul")
def mul():
    params = parse_args()
    if not params:
        return jsonify(error="invalid input"), 400
    x, y = params
    return jsonify(result=x * y)

@app.route("/div")
def div():
    params = parse_args()
    if not params:
        return jsonify(error="invalid input"), 400
    x, y = params
    if y == 0:
        return jsonify(error="division by zero"), 400
    return jsonify(result=x / y)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
