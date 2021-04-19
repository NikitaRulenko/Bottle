from bottle import get, put, post, delete,  response, route, static_file
import json


data_set = [{'id':'1','name':'Sam','address':'Ranchi','Dept':'HR'},
            {'id':'2','name':'Sarah','address':'Ranchi','Dept':'MGR'},
            {'id':'3','name':'Arsh','address':'Delhi','Dept':'HR'}]


@get('/data/show_all')
def show_all():
    response.content_type = 'application/json'
    return json.dumps(data_set)

@get('/data/show_row/<id>')
def show_by_id(id):
    result_row = [row for row in data_set if row['id'] == id]
    return{'result':result_row[0]}

# @get('/data/q_update/<id>/<name>/<address>/<dept>')
# def q_update_row(id, name, address, dept):
#     result_row = [row for row in data_set if row['id'] == id]
#     data_set.insert(result_row[0])
#     return 'DONE'

@post('/data/add_row')
def add_item():
    return None

@put('/data/edit_row/<id>')
def edit_item(id):
    return None

@route('/data/delete_row/<id>')
def delete_item(id):
    result_row = [row for row in data_set if row['id'] == id]
    data_set.remove(result_row[0])
    return 'Done'

@route('data/quick/add_row?id=<id>&name=<name>&address=<address>&dept=<dept>')
def q_add_row(id, name, address, dept):
    result_row = {'id':id,'name':name,'address':address,'dept':dept}
    data_set.append(result_row)
    return 'DONE'

@route('/download/<filename>')
def download(filename):
    return static_file(filename, root='/', download=filename)


# @delete('/employee/<name>')
# def remove_emp(name):
#     the_emp = [emp for emp in employee if emp['name'] == name]
#     employee.remove(the_emp[0])
#     return {'employees': employee}

# @post('/employee')
# def add_emp():
#     new_emp = {'name': request.json.get('name'), 'address': request.json.get('address'),
#                'Dept': request.json.get('Dept')}
#     employee.append(new_emp)
#     return {'employees': employee}