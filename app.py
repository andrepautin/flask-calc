from flask import Flask, request
app = Flask(__name__)

@app.route('/add')
def added():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{add(a, b)}"

@app.route('/sub')
def subtracted():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{sub(a, b)}"
    


@app.route('/mult')
def multiplied():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{mult(a, b)}"


@app.route('/div')
def divided():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"{div(a, b)}"

OPERATIONS = {"add": add, "sub": sub, "mult": mult, "div": div}

@app.route('/math/<operation>')
def all(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    operator = request.args.get(operation)
    return f"{operator(a, b)}"
