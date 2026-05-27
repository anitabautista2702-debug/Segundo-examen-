from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bd_TechBol.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    migrate.init_app(app,db)
    
    #1. Imnportacion del blueprint (para cada modulo)
    from Blueapp.clientes.routes import bp_cliente
    from Blueapp.core.routes import bp_core
    from Blueapp.pedidos.routes import bp_pedido
    from Blueapp.productos.routes import bp_producto
    
    #2. Registro el blueprint (para cada modulo)
    app.register_blueprint(bp_cliente,url_prefix="/clientes")
    app.register_blueprint(bp_core,url_prefix="/")
    app.register_blueprint(bp_pedido, url_prefix='/pedidos')
    app.register_blueprint(bp_producto, url_prefix='/producto')    
    
    return app