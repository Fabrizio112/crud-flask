from ..utils.extensions import db,ma

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    surname=db.Column(db.String(100))
    email=db.Column(db.String(200))
    def __str__(self,id,name,surname,email):
        self.id=id
        self.name=name
        self.surname=surname
        self.email=email

class UserSchema(ma.Schema):
    class Meta:
        fields=('id','name','surname','email')

user_schema=UserSchema()
users_schema=UserSchema(many=True)