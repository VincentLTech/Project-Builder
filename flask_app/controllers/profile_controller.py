import os
from flask_app import app
from flask import Flask, redirect, request, session
from flask import send_from_directory
from werkzeug.utils import secure_filename
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile


app.config['UPLOAD_FOLDER'] = 'flask_app/static/uploads/'


@app.route('/create_profile', methods=["POST"])
def create_users_profile():
    if not Profile.validations(request.form):
        return redirect('/create_profile')
    if request.files['Pic'].filename == '':
        data = {
            'users_id': session['id'],
            'Full_name': request.form['Full_name'],
            'Pic' : None,
            'description': request.form['description']
        }
        Profile.create_profile(data)
    else:
        if 'Pic' in request.files:
            file = request.files['Pic']
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            data = {
                'users_id': session['id'],
                'Full_name': request.form['Full_name'],
                'Pic': f'uploads/{filename}',
                'description': request.form['description']
            }
        Profile.create_profile(data)
        print("create_users_profile finished!")
        Profile.update_users_profile(data)
    return redirect('/profile_page')


@app.route('/update_profile', methods=["POST"])
def update_users_profile():
    print(request.files['Pic'])
    if not Profile.validations(request.form):
        return redirect('/update_profile')
    if request.files['Pic'].filename == '':
        data = {
            'users_id': session['id'],
            'Full_name': request.form['Full_name'],
            'Pic' : None,
            'description': request.form['description']
        }
        Profile.update_users_profile(data)
    else:
        file = request.files['Pic']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        data = {
            'users_id': session['id'],
            'Full_name': request.form['Full_name'],
            'Pic': f'uploads/{filename}',
            'description': request.form['description']
        }
        Profile.update_users_profile(data)
    return redirect('/profile_page')

@app.route('/uploads/<filename>')
def serve_profile_pic(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)







