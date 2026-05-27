from Blueapp import db


class Pedido(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(50),nullable=False)
    monto = db.Column(db.Float(10.2),nullable = False)
    
    def __repr__(self):
        return f"<PEDIDO: {self.fecha} - {self.monto}>"    

    producto_id = db.Column(
        db.Integer,
        db.ForeignKey('productos.id'),
        nullable=False
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey('clientes.id'),
        nullable=False
    )