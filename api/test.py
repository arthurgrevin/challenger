import json
import nose
from nose.tools import *
from api import app

test_app = app.test_client()

def test_get_challenges_empty():
        
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenge']), 0)
    

def test_post_challenges():

    first_challenge = dict(title="Coding challenge")
    second_challenge = dict(title="Eating challenge")
    
    rv = test_app.post('/challenges/', data = first_challenge)
    eq_(rv.status_code, 201)
    rv = test_app.post('/challenges/', data = second_challenge)
    eq_(rv.status_code, 201)
    
def test_get_challenges():
        
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenge']), 2)
    
def test_get_one_challenge():
        
    rv = test_app.get('/challenges/1')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenge']), 1)
    
def test_delete_one_challenge():
        
    rv = test_app.delete('/challenges/1')
    eq_(rv.status_code, 204)
    
def test_get_challenges_length_1():
        
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)    
    eq_(rv.status_code, 200)
    eq_(len(resp['challenge']), 1)