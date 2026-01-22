from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    titulo="IDGS-802-Flask"
    lista=['Python', 'Flask', 'Jinja2', 'HTML5', 'CSS3', 'JavaScript']
    return render_template('index.html', titulo=titulo, lista=lista)

'''

'''
@app.route('/formularios')
def formularios():
    return render_template('formularios.html')
'''
'''
@app.route('/reportes')
def reportes():
    return render_template('reportes.html')


# toda ruta debe tener un nombre único
@app.route('/hola')
def hola():
    return "Hola, Mundo!"
'''

'''
# ruta que recibe un parametro en la url
@app.route('/user/<string:user>')
# dentro del parentesis va la variable a utilizar
def user(user):
    return f"Hola, {user}"
'''

'''
@app.route('/numero/<int:n>')
# dentro del parentesis va la variable a utilizar
def numero(n):
    return "Numero:{}",format(n)
'''

'''

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return "ID: {} nombre:{}".format(id, username)
'''

'''
@app.route('/suma/<float:n1>/<float:n2>')
def func(n1, n2):
    return "la usma es: {}".format(n1+n2)
'''

'''
@app.route('/default/')
@app.route('/default/<string:param>')
def func2(param):
    return f"<h1>!Hola {param}!</h1>"
'''

'''
@app.route('/operas')
def operas():
    return ''' 
    <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>

        <label for="name">paterno:</label>
        <input type="text" id="paterno" name="paterno"><br><br>
    </form>
        ''' 


@app.route("/operaBas", methods=["GET","POST"])
def operas1():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    res= {float(n1)+float(n2)} 
    return render_template("operaBas.html", n1=n1, n2=n2, res=res )





@app.route("/resultado", methods=["GET","POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    return f"La suma es: {float(n1)+float(n2)}"






if __name__ == '__main__':
    app.run(debug=True)
