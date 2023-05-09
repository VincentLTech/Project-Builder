from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
from flask_app import app

db = '3d_prints_db'

class Profile:
    def __init__(self,data):
        self.id = data ['id']
        self.Full_name = data ['Full_name']
        self.Pic = data['Pic']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']


    @classmethod
    def create_profile(cls, data):
        query = '''
        INSERT INTO profile
        (Full_name, Pic, description, users_id, created_at, updated_at)
        VALUES (%(Full_name)s, %(Pic)s, %(description)s, %(users_id)s, NOW(), NOW())
        '''
        return connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_users_profile(cls, user_id):
        query = '''
        SELECT * FROM profile
        WHERE users_id = %(user_id)s
        '''
        results = connectToMySQL(db).query_db(query, user_id)
        print(f"results: {results}")
        if results:
            return cls(results[0])
        else:
            return None
        
    @classmethod
    def get_users_profile_from_project_id(cls, project_id):
        query = '''
        SELECT * FROM projects
        WHERE project.id = %(project_id)s
        '''
        results = connectToMySQL(db).query_db(query, project_id)
        print(f"results: {results}")
        if results:
            return cls(results[0])
        else:
            return None
        
    @classmethod
    def update_users_profile(cls, user_data):
        query = "UPDATE profile SET Full_name = %(Full_name)s, description = %(description)s, Pic = %(Pic)s, updated_at = NOW() WHERE users_id = %(users_id)s;"
        return connectToMySQL(db).query_db(query, user_data)
    

    @staticmethod
    def validations(data):
        is_valid = True
        if len(data['Full_name']) < 2:
            flash('Full name must be a minimum of 2 characters',"profile")
            is_valid = False
        if len(data['description']) < 2:
            flash('Description feild must have at least 2 characters',"profile")
            is_valid = False
        return is_valid

