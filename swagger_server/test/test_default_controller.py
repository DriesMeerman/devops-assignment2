# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.student import Student  # noqa: E501
from swagger_server.test import BaseTestCase
from swagger_server.services import student_service
import uuid

student_id = -1

class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""


    def test_add_student(self):
        """Test case for add_student

        Add a new student
        """
        body = Student(first_name=str(uuid.uuid4()), last_name='beratna', grades={"subject_example": 8})
        response = self.client.open(
            '/service-api/student',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        data = response.data.decode('utf-8')
        self.assert200(response,
                       'Response body is : ' + data)
        TestDefaultController.student_id = data

    def test_get_student_by_id(self):
        """Test case for get_student_by_id

        Find student by ID
        """
        query_string = [('subject', 'subject_example')]
        response = self.client.open(
            '/service-api/student/{student_id}'.format(student_id=TestDefaultController.student_id),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_hdelete_student(self):
        """Test case for delete_student
            renamed to enforce ordering

        """
        url ='/service-api/student/{student_id}'.format(student_id=TestDefaultController.student_id)
        response = self.client.open(
            url,
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    import unittest
    unittest.main()
