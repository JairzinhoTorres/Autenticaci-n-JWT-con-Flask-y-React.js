from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class User(db.Model):
#     id = db.db.Column(db.db.Integer, primary_key=True)
#     email = db.db.Column(db.db.String(120), unique=True, nullable=False)
#     password = db.db.Column(db.db.String(80), unique=False, nullable=False)
#     is_active = db.db.Column(Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }



# ----------- tabla 1 Aca modificamos el USUARIO anterior de star wars-----------
class User(db.Model):
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    contraseña=db.Column(db.String(20), nullable=False)
    mail=db.Column(db.String(100), nullable=False)
    favoritos_user= db.relationship('Favoritos', backref='user', lazy=True)
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "mail": self.mail,
            # do not serialize the password, its a security breach
        }


# ----------- tabla 1 Aca modificamos el PERSONAJES anterior de star wars-----------
class Personajes(db.Model):
    # Here we define columns for the table address.context
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    apllido = db.Column(db.String(250), nullable=False)
    altura = db.Column(db.String(20))
    genero = db.Column(db.String(20))
    personajes_user= db.relationship('Favoritos', backref='personajes', lazy=True)

    def __repr__(self):
        return '<Personajes %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apllido": self.apllido,
            "altura": self.altura,
            "genero": self.genero,
            # do not serialize the password, its a security breach
        }

    # ----------- tabla 1 Aca modificamos el VEHICULOS anterior de star wars-----------
class Vehiculos(db.Model):
    # Here we define columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    modelo=db.Column(db.String(250))
    capacidad=db.Column(db.String(250))
    añoCreacion=db.Column(db.String(250))
    vehiculos_user= db.relationship('Favoritos', backref='vehiculos', lazy=True)

    def __repr__(self):
        return '<Vehiculos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "modelo": self.modelo,
            "capacidad": self.capacidad,
            "añoCreacion": self.añoCreacion,
            # do not serialize the password, its a security breach
        }    

#      # ----------- tabla 1 Aca modificamos el PLANETAS anterior de star wars-----------
    
class Planetas(db.Model):
    # Here we define columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250), nullable=False)
    poblacion=db.Column(db.String(250))
    bioma=db.Column(db.String(250))
    planetas_user= db.relationship('Favoritos', backref='planetas', lazy=True)

    def __repr__(self):
        return '<Planetas %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "poblacion": self.poblacion,
            "bioma": self.bioma,
            # do not serialize the password, its a security breach
        }   


#   # ----------- tabla 1 Aca modificamos el FAVORITOS anterior de star wars-----------
class Favoritos(db.Model):
    # Here we define columns for the table person
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    # agregar = db.Column(db.String(250), nullable=False) ----------------------ESTA NO ES LA FORMA DE TRAER UNA FUNCIONALIDAD
    # eliminar=db.Column(db.String(20), nullable=False) ----------------------ESTA NO ES LA FORMA DE TRAER UNA FUNCIONALIDAD
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    personajes_id = db.Column(db.Integer, db.ForeignKey('personajes.id'))  
    vehiculos_id = db.Column(db.Integer, db.ForeignKey('vehiculos.id'))  
    planetas_id = db.Column(db.Integer, db.ForeignKey('planetas.id'))              
    # person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
    #     nullable=False) DOCUMENTACION PARA COMPARAR
    # usuario = relationship(Usuario)
    # personajes_id = db.Column(db.Integer, ForeignKey('personajes.id'))
    # personajes = relationship(Personajes)
    # planetas_id = db.Column(db.Integer, ForeignKey('planetas.id'))
    # planetas = relationship(Planetas)
    # vehiculos_id = db.Column(db.Integer, ForeignKey('vehiculos.id'))
    # vehiculos = relationship(Vehiculos)

    def __repr__(self):
        return '<Favoritos %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personajes_id": self.personajes_id,
            "vehiculos_id": self.vehiculos_id,
            "favoritos_id": self.favoritos_id,
            "planetas_id": self.planetas_id,
            # "agregar": self.agregar,
            # "eliminar": self.eliminar,
            # do not serialize the password, its a security breach
        }   
    