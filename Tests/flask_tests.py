'''
A starter file for testing a Flask app
Run with:
python -m unittest flask_tests.py
'''

from app import *
import unittest

class TestSOMETHING(unittest.TestCase):
    def test_route_homepage(self):
        #sets up a special test app
        self.app = app.test_client() 
        #test app returns TestResponse object
        response = self.app.get('/', follow_redirects=True) 
        #TestResponse has webpage in .data
        self.assertEqual(b'Hello, this is the homepage of LLM Energy Route Assignment', response.data) 

    def test_route_column(self): 
        '''docstring comment'''
        self.app = app.test_client() 
        load_data()
        response = self.app.get('/0/model_parameters_billion/', follow_redirects=True) 
        self.assertEqual(b"['model_parameters_billion', '175', '1800', '540', '176', '671', '405', '2000', '70', '20', '550', 'Not disclosed', '11', '619', '1500', '0.55', '70', '1200', '180', '7.3', '47', '72', '34', '2700', '280', '175', '7', '7']", response.data) 

    def test_route_nonexistent_column(self):
        '''docstring comment'''
        self.app = app.test_client() 
        load_data()
        response = self.app.get('/0/not_real_column/', follow_redirects=True)
        self.assertEqual(b"[]\n", response.data) 

    def test_route_row(self): 
        '''docstring comment'''
        self.app = app.test_client() 
        load_data()
        response = self.app.get('/T5/', follow_redirects=True) 
        self.assertEqual(b"['T5', '11', '500', 'TPUv3', '512', '480', 'US Central (Iowa)', '1.12', '450', '545', '123900', '46700']", response.data) 

    def test_route_nonexistent_row(self): 
        '''docstring comment'''
        self.app = app.test_client() 
        load_data()
        response = self.app.get('/not_real_LLM_name/', follow_redirects=True) 
        self.assertEqual(b"Page not found error: 404 Not Found: Row not found", response.data)