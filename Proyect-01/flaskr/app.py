from flaskr import create_app
from .modelos import db, Cancion
from .modelos import db, Usuario
from .modelos import db, Album


app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

# prueba

with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete='Juan Pablo')
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

    u = Usuario(nombre_usuario='Santiago Rincon', contraseña='ndjsada')
    db.session.add(u)
    db.session.commit()
    print(Usuario.query.all())

    a = Album(titulo='Bien o mal', año=2022, descripcion='Album 1 de 2022', medio='Disco')
    db.session.add(a)
    db.session.commit()
    print(Album.query.all())
