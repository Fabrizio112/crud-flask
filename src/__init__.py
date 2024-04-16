from flask import Flask,render_template,jsonify,request,flash,url_for,redirect
from .utils.extensions import db,ma

from .models.User import User,user_schema,users_schema

def create_app_crud():
    app=Flask(__name__)
    app.secret_key="1234"
    app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:1234@localhost/crud_flask"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def index():
        users=User.query.all()
        results=users_schema.dump(users)
        return render_template('index.html',users=users)

    @app.route("/form",methods=["GET","POST"])
    def form():
        if request.method=="POST":
            email_enviado=request.form["email"]
            usuario_email=User.query.filter_by(email=email_enviado).first()
            if usuario_email == None:
                usuario_a_crear=User(id=0,name=request.form["name"],surname=request.form["surname"],email=email_enviado)
                db.session.add(usuario_a_crear)
                db.session.commit()
                return redirect(url_for("index"))
            else:
                flash("Email ya utilizado")
                return render_template("form.html",add=True)
        return render_template("form.html",add=True)
    
    @app.route("/form/<id>",methods=["GET","POST"])
    def form_id(id):
        user=User.query.get(id)
        if request.method=="POST":
            user.name=request.form["name"]
            user.surname=request.form["surname"]
            user.email=request.form["email"]
            db.session.commit()
            return redirect(url_for("index"))
        return render_template("form.html",edit=True,user=user)
    
    @app.route("/delete/<id>",methods=["DELETE"])
    def delete_user(id):
        print("Borrado crack")
        usuario_a_eliminar=User.query.get(id)
        db.session.delete(usuario_a_eliminar)
        db.session.commit()
        return "Usuario Eliminado"


        


    return app
    