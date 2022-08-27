from flask_restful import Api,Resource,fields,marshal_with
required_fields = {
  "name" = fields.String,
  "age" = fields.age,
  "location" = fields.String}
class Employee(Resource):
  @marshal_with(requried_fileds)
  def get(self):
    try
