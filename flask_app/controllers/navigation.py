from flask import render_template,redirect,request,session,flash
from flask_app.models.like_model import Like
from flask_app.models.user_model import User
from flask_app.models.part_model import Part
from flask_app.models.profile_model import Profile
from flask_app.models.project_model import Project
from flask_app import app


@app.route('/')
def show_home_page():
    return render_template('home_page.html')

@app.route('/login')
def show_login_page():
    return render_template ('/login.html')

@app.route('/register')
def show_register_page():
    return render_template('/register.html')

@app.route('/profile_page')
def show_profile_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        project = Project.get_project_by_users_id({'user_id': session['id']})
        profile = Profile.get_users_profile({'user_id': session['id']})
        user = User.get_one_user({'id':session['id']})
        return render_template('/profile_page.html', user=user, profile=profile, project=project)

@app.route('/create_project')
def show_create_project_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        user = User.get_one_user({'id':session['id']})
        return render_template('/create_project.html', user = user)

@app.route('/edit_project/<int:project_id>')
def edit_project(project_id):
    if 'id' not in session:
        return redirect('/')
    else:
        user = User.get_one_user({'id':session['id']})
        id = project_id 
        project = Project.get_project_by_id({'id': id})
        parts = Part.get_parts_by_project_id({'project_id': project_id})
        return render_template('edit_project.html', project=project, parts=parts, user=user)

@app.route('/create_profile')
def show_edit_profile_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        return render_template('/create_profile.html')

@app.route('/update_profile')
def show_update_profile_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        profile = Profile.get_users_profile({'user_id': session['id']})
        return render_template('/edit_profile.html', profile = profile)

@app.route('/depot')
def show_depot_page():
    if 'id' not in session:
        return redirect ('/')
    else:
        user = User.get_one_user({'id':session['id']})
        projects = Project.get_users_and_projects()
        print(projects)
        return render_template('/depot_page.html', projects=projects, user=user)

@app.route('/depot_by_likes')
def show_depot_page_by_likes():
    if 'id' not in session:
        return redirect ('/')
    else:
        user = User.get_one_user({'id':session['id']})
        projects = Project.get_users_projects_and_likes()
        print(projects)
        return render_template('/depot_page.html', projects=projects, user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/view_project/<int:project_id>')
def view_project_page(project_id):
    if 'id' not in session:
        return redirect ('/')
    else:
        data = {
            'projects_id':project_id,
            'users_id': session['id']
        }
        project = Project.get_project_by_id({'id':project_id})
        parts = Part.get_parts_by_project_id({'project_id': project_id})
        user = User.get_one_user({'id':session['id']})
        likes = Like.count_likes(project.id)
        has_liked = Like.has_liked(data)
        return render_template('/view_project.html', user=user, project=project, parts=parts, likes=likes, has_liked = has_liked, project_id=project_id)
    

@app.route('/search')
def search():
    sort = request.args.get('sort_by')
    if sort == 'recent':
        return redirect('/depot')
    else:
        return redirect('/depot_by_likes')