from students import StudentDao, students
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
 
app = Flask(__name__)
api = Api(app)
 
class Student(Resource):
    def get(self):
        return jsonify(students=[e.serialize() for e in students])
    def post(self):
        data = request.get_json()
        students.append(StudentDao(
            data["sid"], data["first_name"], data["last_name"]))
        return jsonify(students=[e.serialize() for e in students])
    def put(self):
        data = request.get_json()
        student = next(
            (obj for obj in students if obj.sid == data["sid"]), None)
        if student != None:
            student.first_name = data["first_name"]
            student.last_name = data["last_name"]
        return jsonify(students=[e.serialize() for e in students])
    def delete(self):
        data = request.get_json()
        for student in students:
            if (student.sid == data["sid"]):
                students.remove(student)
        return jsonify(students=[e.serialize() for e in students])
 
api.add_resource(Student, '/student')
 
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=6000)