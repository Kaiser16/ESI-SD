import json

from bottle import run, request, response, get, post, put

database = dict() # key: code, value: course

class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

@post('/AddCourse')
def add_course():
    #import pdb; pdb.set_trace()

    data = request.json

    code = data.get('code') # data['code']
    name = data.get('name')

    course = Course(code, name)

    database[code] = course

    response.headers['Content-Type'] = 'application/json'

    json_to_parse = {'code': code, 'name': name}

    return json.dumps(json_to_parse)

@get('/ListCourses')
def list_courses():
    #import pdb; pdb.set_trace()
    to_return = []

    for key, value in database.items():
        to_return.append({"code": key, "name": value.name})

    response.headers['Content-Type'] = 'application/jason'
    
    return json.dumps(to_return)

@put('/UpdateCourse/<course_code>')
def update_course(course_code):
    course = database[course_code]

    new_name = request.json.get('name')

    course.name = new_name
    
    response.headers['Content-Type'] = 'application/json'

    json_to_parse = {'code': course_code, 'name': new_name}

    return json.dumps(json_to_parse)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)