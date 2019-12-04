from flask import (
    redirect, render_template, url_for,
    Blueprint, escape, request
    )
from project import db
from project.models.model1 import Model1


main_blueprint = Blueprint(
    "main",
    __name__,
    static_url_path="/static",
    static_folder="./static",
    template_folder="templates",
)


@main_blueprint.route("/")
def index():
    mymodel = Model1.query.all()
    return render_template("main/index.html", names=mymodel)


@main_blueprint.route("/add", methods=["POST"])
def add():
    name = escape(request.form["name"])
    surname = escape(request.form["surname"])
    print(name, surname)
    user = Model1(name=name[:9], surname=surname)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("main.index"))


@main_blueprint.route("/delete", methods=["POST"])
def delete():

    ids = escape(request.form["id"])
    if isinstance(ids, list):
        for id in ids:
            try:
                id = int(id)
            except TypeError:
                raise TypeError("Only integers are allowed for id")
            user = Model1.query.get(id)
            db.session.delete(user)
            db.session.commit()
    return redirect(url_for("main.index"))
