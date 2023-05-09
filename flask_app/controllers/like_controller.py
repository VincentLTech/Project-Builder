from flask import render_template,redirect,request,session,flash
from flask_app.models.like_model import Like
from flask_app.models.user_model import User
from flask_app.models.part_model import Part
from flask_app.models.profile_model import Profile
from flask_app.models.project_model import Project
from flask_app import app

@app.route('/like/<int:project_id>')
def like_project(project_id):
    data = {
            'users_id' : session['id'],
            'projects_id' : project_id 
        }
    if Like.has_liked(data) == True:
        flash('You have already liked this project.',"part")
        return redirect(f'/view_project/{project_id}')
    else:
        Like.save(data)
        flash('you liked this project',"part")
        return redirect(f'/view_project/{project_id}')

@app.route('/unlike/<int:project_id>')
def unlike_project(project_id):
    data = {
        'users_id' : session['id'],
        'projects_id' : project_id 
    }
    Like.unlike(data)
    flash('you unliked this project',"part")
    return redirect(f'/view_project/{project_id}')