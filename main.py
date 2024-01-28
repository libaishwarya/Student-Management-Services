from ipaddress import ip_address
from time import sleep
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# In-memory array to store student data
students = []

# Get the port from the environment variable, default to 5000
port = int(os.environ.get('FLASK_PORT', 5000))

@app.route('/students', methods=['GET'])
def get_students():
    print("test")
    return jsonify({'students': students})

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student:
        return jsonify({'student': student})
    else:
        return jsonify({'message': 'Student not found'}), 404

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    if 'name' not in data or 'marks' not in data:
        return jsonify({'message': 'Name and marks are required'}), 400

    student_id = len(students) + 1
    new_student = {
        'id': student_id,
        'name': data['name'],
        'marks': data['marks']
    }

    students.append(new_student)
    return jsonify({'message': 'Student added successfully', 'student': new_student}), 201

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)

    if not student:
        return jsonify({'message': 'Student not found'}), 404

    data = request.get_json()
    student['name'] = data.get('name', student['name'])
    student['marks'] = data.get('marks', student['marks'])

    return jsonify({'message': 'Student updated successfully', 'student': student})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=port, host="0.0.0.0")
