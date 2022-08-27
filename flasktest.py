from flask import Flask,request
from flask_restful import Api,Resource
import json
app = Flask(__name__)
api = Api(app)
class Hello(Resource):
    def get(self):
        return json.dumps({"response":"hello hita baby"})
class Helloname(Resource):
    def get(self,name):
        return json.dumps({"response":f"hello{name}"})
class Employee(Resource):
    def get(self):
        print(request.method)
        input_args = request.args
        print(input_args)
        name = input_args.get('name')
        age = input_args.get("age")
        location = input_args.get("location","delhi")
        print(request.method)
        input_args = request.args
        return json.dumps({"response":f"hello {name},your age {age} you are from  {location}"})

#sending arguments in body
api.add_resource(Hello,'/')
api.add_resource(Helloname,'/<name>')
api.add_resource(Employee,'/Employee')



if __name__=='__main__':
    app.run(debug=True)
