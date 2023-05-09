from flask_app import app
from flask import Flask, redirect, request, session, flash
from flask_app.models.project_model import Project
from flask_app.models.part_model import Part

@app.route('/create_project', methods=["POST"])
def create_project():
    if 'id' not in session:
        return redirect('/create_project')
    else:
        data = {
            'project_name' : request.form['project_name'],
            'description' : request.form['description'],
            'users_id' : session['id']
        }
        if Project.validations(data) == False:
            return redirect ('/create_project')
        project_id = Project.create_project(data)
        print(project_id)
        return redirect(f'/edit_project/{project_id}')

@app.route('/delete_project/<int:project_id>')
def delete_project(project_id):
    if 'id' not in session:
        return redirect('/')
    else:
        Project.delete_project({ 'project_id': project_id })
        flash('Project has been deleted!''project')
        return redirect('/profile_page')
    


