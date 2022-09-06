from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(userinfo):
        is_valid = True
        if len(userinfo['first_name'])<=0:
            flash('First name required')
            is_valid = False
        if len(userinfo['last_name'])<=0:
            flash('Last name required')
            is_valid = False
        if len(userinfo['email'])<=0:
            flash('Email required')
            is_valid = False
        print('worthy')
        return is_valid


    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):               #get all data from database and convert them instances
        query = "SELECT * FROM users;"      #sql query 
        results = connectToMySQL('users_schema').query_db(query)  #given of the sql schema
        users=[]
        for friend in results:
            users.append( cls(friend) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email ) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL('users_schema').query_db( query, data )
        #allows users to store information and add new users to the table
        
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATED users SET first_name= %(first_name)s,last_name= %(last_name)s,email= %(email)s, updated_at=NOW() WHERE id = %(id)s;" 
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def delet(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)


    




#query database + flask pipenv install flask PyMySQL