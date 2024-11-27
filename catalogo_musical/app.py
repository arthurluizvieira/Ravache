from flask import Flask, render_template, request, redirect, url_for
from models import db, Disc, Artist, Genre
from controllers import cadastrar_disc, listar_discos, editar_disc, excluir_disc

app = Flask(__name__)


#sqlALCHEMY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalogo_musical.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#MYSQL teste
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/catalogo_musical'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return listar_discos()

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    return cadastrar_disc(request)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    return editar_disc(request, id)

@app.route('/excluir/<int:id>')
def excluir(id):
    return excluir_disc(id)

if __name__ == "__main__":
    app.run(debug=True)
