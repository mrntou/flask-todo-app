from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, login_required
from TODO import app, login_manager, db
from TODO.models import User, Todo
from TODO.forms import TodoForm, LoginForm






@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data, force=True)
        else:
            flash('Wrong username or password', category='warning')

    return render_template('login.html', form=form)




@app.route('/', methods=['GET','POST'])
def index():
    form = TodoForm()
    todos = Todo.query.order_by(Todo.id.desc()).all()
    if form.validate_on_submit():
        todo = Todo(
            title=form.title.data,

        )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('index.html', form=form, todos=todos)


@app.route('/todo/complete/<int:todo_id>')
def complete_todo(todo_id):
    complete = request.args.get('complete')
    todo = Todo.query.get_or_404(todo_id)
    if complete == 'true':
        todo.complete = True
    if complete  == 'false':
        todo.complete = False
    db.session.commit()
    
    return redirect(url_for('index'))


@app.route('/todo/delete/<int:todo_id>', methods=['GET', 'POST'])
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/todo/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    form = TodoForm()
    if form.validate_on_submit():
        todo.title = form.title.data
        db.session.commit()
        return redirect(url_for('index'))

    if request.method == 'GET':
        form.title.data = todo.title


    return render_template('edit_todo.html', todo=todo, form=form)