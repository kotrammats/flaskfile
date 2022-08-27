from flask import Flask,request
from flask_restful import Api,Resource
import json
app = Flask(__name__)
api = Api(app)

#sending parameters in HTTP request
class Hello(Resource):
    def get(self):
        return json.dumps({"response":"hello hita baby"})
class Helloname(Resource):
    def get(self,name):
        return json.dumps({"response":f"hello{name}"})
class Employee(Resource):
    def get(self):
        try:
            print(request.method)
            input_args = request.args
            print(input_args)
            print(input_args['name'])
            print(input_args['age'])
            print(input_args['location'])
            return json.dumps({"response":f"hello"})
        except Exception as e:
            print(e)
            return json.dumps({"response":f"error occured"})


api.add_resource(Hello,'/')
api.add_resource(Helloname,'/<name>')
api.add_resource(Employee,'/Employee')



if __name__=='__main__':
    app.run(debug=True)
