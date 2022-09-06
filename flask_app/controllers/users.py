from flask import render_template, request, redirect, flash

from flask_app import app

from flask_app.models.user import User


@app.route('/')
def index():
    return redirect("/users")

@app.route('/users')
def users():                                                        #retrieving the info from mysql
    return render_template("read.html", users = User.get_all())

@app.route('/users/add')
def add():
    return render_template("create.html")

@app.route('/users/create',methods=['POST'])                #rerouting page to another page 
def create():
    if not User.validate_user(request.form):
        return redirect('/users/add')
    data = {
        "first_name": request.form["first_name"],            #this is the infomation that is being saved 
        "last_name": request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)                                       #data is saved and displayed to redirected page
    return redirect("/users")

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('edituser.html', user=User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        'id': id
    }
    return render_template('show_user.html', user=User.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/delet/<int:id>')
def delet(id):
    data ={
        'id': id
    }
    User.delet(data)
    return redirect('/users')

