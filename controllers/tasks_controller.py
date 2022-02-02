from flask import Flask, render_template, Blueprint, request, redirect


import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

from models.task import Task

tasks_blueprint = Blueprint('tasks', __name__)

#shows all tasks
@tasks_blueprint.route('/tasks', methods=['GET'])
def tasks():
    tasks = task_repository.select_all()
    return render_template('tasks/index.html', tasks=tasks)

#NEW
@tasks_blueprint.route ('/tasks/new', methods=['GET'])
def new_task():
    users = user_repository.select_all()
    return render_template('tasks/new.html', all_users = users)

#CREATE
@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    
    description = request.form['description']
    user_id = request.form['user_id']
    duration = request.form['duration']
    completed = request.form['completed']
    user = user_repository.select(user_id)
    task = Task(description, user, duration, completed,)
    task_repository.save(task)
    return redirect('/tasks')
    
#DELETE 
@tasks_blueprint.route('/tasks/<id>/delete', methods=['POST'])
def delete_task(id):
    task_repository.delete(id)
    return redirect('/tasks')

#SHOW
@tasks_blueprint.route('/tasks/<id>/', methods=['GET'])
def show_task(id):
    task = task_repository.select(id)
    return render_template('tasks/show.html', task=task)


#UPDATE EDIT
@tasks_blueprint.route('/tasks/<id>/edit')
def edit_task(id):
    users = user_repository.select_all()
    task = task_repository.select(id)

    return render_template('tasks/edit.html', users=users, task=task)

#UPDATE POST
@tasks_blueprint.route('/tasks/<id>', methods=['POST'])
def update_task(id):
    description = request.form['description']
    user_id = request.form['user_id']
    duration = request.form['duration']
    completed = request.form['completed']
    user = user_repository.select(user_id)
    task = Task(description, user, duration, completed, id)
    task_repository.update(task)
    return redirect('/tasks')