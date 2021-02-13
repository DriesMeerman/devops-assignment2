import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util
from swagger_server.services import student_service

studentId=0

def add_student(body):  # noqa: E501
    """Add a new student

     # noqa: E501

    :param body: Student object that needs to be added
    :type body: dict | bytes

    :rtype: int
    """
    if connexion.request.is_json:
        student = Student.from_dict(connexion.request.get_json())  # noqa: E501
        # print(student)
        result = student_service.add_student(student)
        return result

    return 'input no bueono', 400


def delete_student(student_id):  # noqa: E501
    """delete_student

     # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int

    :rtype: Student
    """
    return student_service.delete_student(student_id)


def get_student_by_id(student_id, subject=None):  # noqa: E501
    """Find student by ID

    Returns a single student # noqa: E501

    :param student_id: ID of student to return
    :type student_id: int
    :param subject: The subject name
    :type subject: str

    :rtype: Student
    """
    return student_service.get_student_by_id(student_id, subject)
