from flask import request,render_template,redirect,Blueprint

from Blueapp import db
from Blueapp.pedidos.models import Pedido
from Blueapp.productos.models import Producto
from Blueapp.clientes.models import Cliente

bp_pedido = Blueprint('bp_pedido',__name__,template_folder='templates')

@bp_pedido.route("/")
def index():
    pedidos = Pedido.query.all()
    return render_template("pedido/index.html", pedidos=pedidos)

@bp_pedido.route('/create', methods=['GET', 'POST'])
def create():

    productos = Producto.query.all()
    clientes = Cliente.query.all()

    if request.method == 'POST':

        pedido = Pedido(
            fecha=request.form['fecha'],
            monto=request.form['monto'],
            producto_id=request.form['producto_id'],
            cliente_id=request.form['cliente_id']
        )

        db.session.add(pedido)
        db.session.commit()

        return redirect('/pedidos/')

    return render_template(
        'pedido/create.html',
        productos=productos,
        clientes=clientes
    )
# EDITAR
@bp_pedido.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    pedido = Pedido.query.get_or_404(id)

    productos = Producto.query.all()
    clientes = Cliente.query.all()

    if request.method == 'POST':

        pedido.fecha = request.form['fecha']
        pedido.monto = request.form['monto']
        pedido.producto_id = request.form['producto_id']
        pedido.cliente_id = request.form['cliente_id']

        db.session.commit()

        return redirect('/pedidos/')

    return render_template(
        'pedido/edit.html',
        pedido=pedido,
        productos=productos,
        clientes=clientes
    )


# ELIMINAR
@bp_pedido.route('/delete/<int:id>')
def delete(id):

    pedido = Pedido.query.get_or_404(id)

    db.session.delete(pedido)

    db.session.commit()

    return redirect('/pedidos/')