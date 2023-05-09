import os
from flask_app import app
from flask import Flask, redirect, request, session, flash, url_for
from werkzeug.utils import secure_filename
from flask_app.models.part_model import Part
from flask_app.models.project_model import Project
from flask_app.models.user_model import User
from flask_app.models.profile_model import Profile

app.config['UPLOAD_FOLDER'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static/uploads/'))

@app.route('/Upload_part/<int:project_id>', methods=['POST'])
def upload_part(project_id):
    if 'id' not in session:
        return redirect('/')
    else:
        partfile = request.files['part']
        part_filename = secure_filename(partfile.filename)
        partfile_path = os.path.join(app.config['UPLOAD_FOLDER'], part_filename)
        partfile.save(partfile_path)
        
        partpic = request.files['screenshot']
        partpic_filename = secure_filename(partpic.filename)
        partpic_path = os.path.join(app.config['UPLOAD_FOLDER'], partpic_filename)
        partpic.save(partpic_path)
        
        data = {
            'part': f'uploads/{part_filename}',
            'part_name': request.form['part_name'],
            'screenshot' : f'uploads/{partpic_filename}',
            'project_id': project_id
        }
        Part.create_part(data)
        flash('Part uploaded successfully!', 'part')
        return redirect(f'/edit_project/{project_id}')

@app.route('/delete_part/<int:part_id>')
def delete_part(part_id):
    if 'id' not in session:
        return redirect('/')
    part = Part.get_one_part({'id': part_id})
    Project.get_project_by_id({'id': part.project_id})
    Part.delete_part(part_id)
    flash("Part deleted successfully.","part")
    return redirect(f'/edit_project/{part.project_id}')
