import json
import nose
from nose.tools import *
from api import app

def check_content_type(headers):
    eq_(headers['Content-Type'], 'application/json')

test_app = app.test_client()
rv = test_app.get('/challenges/')
#check_content_type(rv.headers)
resp = json.loads(rv.data)

# make sure we get a response
eq_(rv.status_code, 200)

# make sure there are no users
eq_(len(resp['challenge']), 0)