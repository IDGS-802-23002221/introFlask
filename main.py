from flask import Flask, render_template, request
 # mensajes de ruta a la vista
from flask import flash
from flask_wtf.csrf import CSRFProtect
from cine import procesar
from forms import CineForm
import forms 

app = Flask(__name__)

app.secret_key='Clave secreta'
csrf=CSRFProtect()



@app.route('/')
def index():
    titulo="IDGS-802-Flask"
    lista=['Python', 'Flask', 'Jinja2', 'HTML5', 'CSS3', 'JavaScript']
    return render_template('index.html', titulo=titulo, lista=lista)

'''

'''

@app.route("/usuarios", methods=["POST", "GET"])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    
    usuarios_class=forms.UserForm(request.form) # vincula los campos de la clase con los campos de la vista

    if request.method=='POST' and usuarios_class.validate(): # si se enviaron por post pero tambien no tienen errores, los recibe, si no, no los deja pasar
        mat= usuarios_class.matricula.data # 
        nom= usuarios_class.nombre.data # 
        apa= usuarios_class.apaterno.data # 
        ama= usuarios_class.amaterno.data # 
        email= usuarios_class.correo.data # 

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)

    return render_template("usuarios.html", form=usuarios_class,
                           mat=mat, nom=nom, apa=apa, ama=ama, email=email)



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

# suma
@app.route("/operaBas", methods=["GET","POST"])
def operas1():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == "POST":
        n1=request.form.get("n1")
        n2=request.form.get("n2")
        res= float(n1)+float(n2)

        return render_template("operaBas.html", n1=n1, n2=n2, res=res )
    
    return render_template("operaBas.html", n1=n1, n2=n2, res=res )

# division
@app.route("/operaBas", methods=["GET","POST"])
def operas2():
    n1 = 0
    n2 = 0
    res = 0
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    res= {float(n1)/float(n2)} 
    return render_template("operaBas.html", n1=n1, n2=n2, res=res )
# resta
@app.route("/operaBas", methods=["GET","POST"])
def operas3():
    n1 = 0
    n2 = 0
    res = 0
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    res= {float(n1)-float(n2)} 
    return render_template("operaBas.html", n1=n1, n2=n2, res=res )

# multiplicacion
@app.route("/operaBas", methods=["GET","POST"])
def operas4():
    n1 = 0
    n2 = 0
    res = 0
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    res= {float(n1)/float(n2)} 
    return render_template("operaBas.html", n1=n1, n2=n2, res=res )




@app.route("/resultado", methods=["GET","POST"])
def resultado():
    n1=request.form.get("n1")
    n2=request.form.get("n2")
    return f"La suma es: {float(n1)+float(n2)}"


@app.route('/alumnos',methods=["GET","POST"])
def alumnos():

    return render_template('alumnos.html')


@app.route('/distanciaDosPuntos', methods=["GET", "POST"])
def distancia():
    distancia = None

    if request.method == "POST":
        x1 = float(request.form.get("x1"))
        y1 = float(request.form.get("y1"))
        x2 = float(request.form.get("x2"))
        y2 = float(request.form.get("y2"))

        distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    return render_template('distanciaDosPuntos.html', distancia=distancia)

@app.route("/cine", methods=["GET", "POST"])
def cine():
    form_Class = forms.CineForm(request.form)

    resultado = None
    nombre = None

    if request.method == "POST"  and form_Class.validate():
        nombre = form_Class.nombre.data
        cantB = form_Class.cantB.data
        cantP = form_Class.cantP.data
        formPago = form_Class.tarjeta.data

        resultado = procesar(formPago, cantB, cantP)

    return render_template(
        "cine.html",
        form=form_Class,
        resultado=resultado,
        nombre=nombre, 
    )


    form = CineForm(request.form)

    # DIAGNÓSTICO - AGREGAR ESTAS LÍNEAS
    print("=" * 50)
    print(f"Método: {request.method}")
    print(f"Form data: {request.form}")
    print(f"CSRF en form data: {'csrf_token' in request.form}")
    if 'csrf_token' in request.form:
        print(f"Valor CSRF recibido: {request.form['csrf_token']}")
    print("=" * 50)
    # FIN DIAGNÓSTICO

    resultado = None
    nombre = None

    if request.method == "POST" and form.validate():
        nombre = form.nombre.data
        cantB = form.cantB.data
        cantP = form.cantP.data
        formPago = form.tarjeta.data

        resultado = procesar(formPago, cantB, cantP)

    return render_template(
        "cine.html",
        form=form,
        resultado=resultado,
        nombre=nombre, 
    )

if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)
