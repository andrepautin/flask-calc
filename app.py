from flask import Flask, request
app = Flask(__name__)
from operations import add, sub, mult, div

@app.route('/add')
def added():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return f"{result}"

@app.route('/sub')
def subtracted():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return f"{result}"
    


@app.route('/mult')
def multiplied():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return f"{result}"


@app.route('/div')
def divided():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a,b)
    return f"{result}"

OPERATIONS = {
"add": add, 
"sub": sub, 
"mult": mult, 
"div": div
}

@app.route('/math/<operation>')
def all(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = OPERATIONS[operation](a,b)
    return f"{result}"
