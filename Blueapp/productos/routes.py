from flask import request, render_template, redirect, url_for, Blueprint

from Blueapp import db
from Blueapp.productos.models import Producto

bp_producto = Blueprint(
    'bp_producto',
    __name__,
    template_folder='templates'
)

@bp_producto.route("/")
def index():

    productos = Producto.query.all()

    return render_template(
        "producto/index.html",
        productos=productos
    )


@bp_producto.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'POST':

        nombre = request.form.get('nombre')
        precio = request.form.get('precio')
        stock = request.form.get('stock')

        # CREAR OBJETO
        producto = Producto(
            nombre=nombre,
            precio=precio,
            stock=stock
        )

        # GUARDAR EN BD
        db.session.add(producto)
        db.session.commit()

        return redirect(url_for('bp_producto.index'))

    return render_template('producto/create.html')

@bp_producto.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    producto = Producto.query.get_or_404(id)

    if request.method == 'POST':

        producto.nombre = request.form['nombre']
        producto.precio = request.form['precio']
        producto.stock = request.form['stock']

        db.session.commit()

        return redirect('/producto/')

    return render_template(
        'producto/edit.html',
        producto=producto
    )
@bp_producto.route('/delete/<int:id>')
def delete(id):

    producto = Producto.query.get_or_404(id)

    db.session.delete(producto)

    db.session.commit()

    return redirect('/producto/')