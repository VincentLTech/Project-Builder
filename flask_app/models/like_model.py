from flask_app.config.mysqlconnection import connectToMySQL
db = '3d_prints_db'

class Like:
    def __init__(self, data):
        self.likes = data['likes']
        self.project_id = data['project_id']
        self.users_id = data['users_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO projects_has_likes (projects_id, users_id) VALUES (%(projects_id)s, %(users_id)s)"
        return connectToMySQL(db).query_db(query, data)
    
    @staticmethod
    def count_likes(projects_id):
        query = "SELECT COUNT(*) as count FROM projects_has_likes WHERE projects_id = %(projects_id)s;"
        data = { 'projects_id': projects_id }
        result = connectToMySQL(db).query_db(query, data)
        return result[0]['count']
    
    @staticmethod
    def has_liked(data):
        query = "SELECT COUNT(*) as count FROM projects_has_likes WHERE users_id = %(users_id)s AND projects_id = %(projects_id)s;"
        result = connectToMySQL(db).query_db(query, data)
        return result[0]['count'] >= 1

    @staticmethod
    def unlike(data):
        query = "DELETE FROM projects_has_likes WHERE users_id = %(users_id)s AND projects_id = %(projects_id)s;"
        return connectToMySQL(db).query_db(query, data)