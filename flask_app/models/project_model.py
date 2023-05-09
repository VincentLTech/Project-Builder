from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


db = '3d_prints_db'

class Project:
    def __init__(self,data):
        self.id = data ['id']
        self.project_name = data ['project_name']
        self.description = data ['description']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.user_id = ['user_id']

    @classmethod
    def create_project(cls, data):
        query = '''
        INSERT INTO projects
        (project_name, description, created_at, updated_at ,users_id)
        VALUES (%(project_name)s, %(description)s, NOW(), NOW(), %(users_id)s)
        '''
        result = connectToMySQL(db).query_db(query, data)
        data['id'] = result
        return result
    
    @classmethod
    def get_project_by_users_id(cls, user_id):
        query = '''SELECT * FROM projects WHERE users_id = %(user_id)s'''
        results = connectToMySQL(db).query_db(query, user_id)
        projects = []
        for result in results:
            projects.append(cls(result))
        return projects

    @classmethod
    def get_project_by_id(cls, id):
        query = "SELECT * FROM projects WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, id)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    
    @classmethod
    def get_project_by_part_project_id(cls, id):
        query = "SELECT * FROM projects WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, id)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_users_and_projects(cls):
        query = '''
        SELECT users.username, projects.*, COUNT(projects_has_likes.projects_id) AS num_likes
        FROM users
        LEFT JOIN projects ON users.id = projects.users_id
        LEFT JOIN projects_has_likes ON projects.id = projects_has_likes.projects_id
        GROUP BY users.id, projects.id
        ORDER BY projects.created_At DESC;
        '''
        results = connectToMySQL(db).query_db(query)
        print(results)
        return results

    @classmethod
    def get_users_projects_and_likes(cls):
        query = '''
        SELECT users.username, projects.*, COUNT(projects_has_likes.projects_id) AS num_likes
        FROM users
        LEFT JOIN projects ON users.id = projects.users_id
        LEFT JOIN projects_has_likes ON projects.id = projects_has_likes.projects_id
        GROUP BY users.id, projects.id
        ORDER BY num_likes DESC;
        '''
        return connectToMySQL(db).query_db(query)   

    @classmethod
    def delete_project(cls, project_id):
        query = "DELETE FROM parts WHERE project_id = %(project_id)s;"
        connectToMySQL(db).query_db(query, project_id)
        query = "DELETE FROM projects WHERE id = %(project_id)s;"
        return connectToMySQL(db).query_db(query, project_id)

    @staticmethod
    def validations(data):
        is_valid = True
        if len(data['project_name']) < 2:
            flash('project name must be a minimum of 2 characters',"project")
            is_valid = False
        if len(data['description']) < 2:
            flash('Description feild must have at least 2 characters',"project")
            is_valid = False
        return is_valid