import json
import nose
from nose.tools import *
from api import app



def test_challenges():
    test_app = app.test_client()
    
    
    ## 1 ## GET returns nothing
    
    rv = test_app.get('/challenges/')
    resp = json.loads(rv.data)
    eq_(rv.status_code, 200)
    eq_(len(resp['challenge']), 0)
    
    
    ## 2 ## POST creates a challenge
    #d = dict(title="Coding challenge", days=34)
    #rv = test_app.post('/challenges/', data=d)
    #eq_(rv.status_code, 201)
    
    
    ## 3 ## GET returns 1 challenge
    
    #rv = test_app.get('/challenges/')
    #resp = json.loads(rv.data)
    #eq_(rv.status_code, 200)
    #eq_(len(resp['challenge']), 1)
    #eq_(resp['challenge'][0], "Coding challenge")