import json, nose
from nose.tools import *
from run import app
import logging

test_app = app.test_client()
logger = logging.getLogger("test.debug")

def test_get_challenges_empty():
        
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenges']), 0)
    

def test_post_challenges():

    first_challenge = dict(title = "Coding challenge", start_date = "2017-01-23", end_date = "2017-01-26")
    second_challenge = dict(title = "Eating challenge", start_date = "2017-01-26", end_date = "2017-01-27")
    
    rv = test_app.post('/challenges/', data = json.dumps(first_challenge), content_type='application/json')
    resp = json.loads(rv.data)
    eq_(rv.status_code, 201)
    eq_(len(resp), 1)
    eq_(len(resp['challenge']['days']), 4)
    
    rv = test_app.post('/challenges/', data = json.dumps(second_challenge), content_type='application/json')
    resp = json.loads(rv.data)
    eq_(rv.status_code, 201)
    eq_(len(resp), 1)
    eq_(len(resp['challenge']['days']), 2)
    
def test_get_challenges():
        
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenges']), 2)
    
def test_get_one_challenge():
        
    rv = test_app.get('/challenges/1/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenge']), 1)
    
def test_delete_one_challenge():
        
    rv = test_app.delete('/challenges/1/')
    eq_(rv.status_code, 204)
    
def test_get_challenges_length_1():
        
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenges']), 1)