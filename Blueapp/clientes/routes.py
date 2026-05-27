from flask import request,render_template,redirect,url_for,Blueprint

from Blueapp import db
from Blueapp.clientes.models import Cliente

bp_cliente = Blueprint('bp_cliente',__name__,template_folder='templates')

@bp_cliente.route("/")
def index():
    clientes = Cliente.query.all()
    return render_template("cliente/index.html", clientes=clientes)

@bp_cliente.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'GET':
        return render_template('cliente/create.html')

    elif request.method == 'POST':

        nombre = request.form.get('nombre')
        telefono = request.form.get('telefono')

        cliente = Cliente(
            nombre=nombre,
            telefono=telefono
        )

        db.session.add(cliente)
        db.session.commit()

        return redirect(url_for('bp_cliente.index'))
    
@bp_cliente.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    cliente = Cliente.query.get_or_404(id)

    if request.method == 'POST':

        cliente.nombre = request.form['nombre']
        cliente.telefono = request.form['telefono']

        db.session.commit()

        return redirect('/clientes/')

    return render_template(
        'cliente/edit.html',
        cliente=cliente
    )


# ELIMINAR
@bp_cliente.route('/delete/<int:id>')
def delete(id):

    cliente = Cliente.query.get_or_404(id)

    db.session.delete(cliente)

    db.session.commit()

    return redirect('/clientes/')
