from flask import Flask
from flask_restful import Api, Resource, reqparse

import data_generator as datagen




app = Flask(__name__)
api = Api(app)




users = [datagen.generate_person() for x in range(5)]
print("\nNow users info is:")
for user in users:
    print(datagen.print_person(user))
print()




class User(Resource):

    def get(self, name):
        '''The get method is used to retrieve a particular user details by specifying the name'''
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404



    def post(self, name):
        '''The post method is used to create a new user'''
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("surname")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "surname": args["surname"]
        }
        users.append(user)
        return user, 201



    def put(self, name):
        '''The put method is used to update details of user, or create a new one if it is not existed yet'''
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("surname")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["surname"] = args["surname"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "surname": args["surname"]
        }
        users.append(user)
        return user, 201



    def delete(self, name):
        '''The delete method is used to delete user that is no longer relevant'''
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200 
      


api.add_resource(User, "/User/<string:name>")
addr = '0.0.0.0'

@app.route("/")
def hello():
    html = "<h3>Hello, developer</h3>" \
           "<b>It works</b><br/>" \
           "<b>Now you can use api through interface {interface}</b><br/>" \
           "As example, try to get http://{interface}/User/any_user_name_from_console"
    return html.format(interface=addr)

app.run(host=addr, port=80)