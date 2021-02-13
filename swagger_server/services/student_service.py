import json
import logging
import os
import tempfile

from tinydb import TinyDB, Query
from tinydb.middlewares import CachingMiddleware
from functools import reduce
import uuid

from swagger_server.models import Student

db_dir_path = tempfile.gettempdir()
db_file_path = os.path.join(db_dir_path, "students.json")
print('DB: ' + db_file_path)
student_db = TinyDB(db_file_path)


def add_student(student):
    queries = []
    query = Query()
    queries.append(query.first_name == student.first_name)
    queries.append(query.last_name == student.last_name)
    query = reduce(lambda a, b: a & b, queries)
    res = student_db.search(query)
    if res:
        return 'already exists' + res.doc_id, 409

    doc_id = student_db.insert(student.to_dict())
    student.student_id = doc_id
    return doc_id, 200


def get_student_by_id(student_id, subject):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return student, 404
    student = Student.from_dict(student)
    if not subject:
        return student, 200
    return student



def delete_student(student_id):
    student = student_db.get(doc_id=int(student_id))
    if not student:
        return student, 400

    student_db.remove(doc_ids=[int(student_id)])
    return student_id, 200
