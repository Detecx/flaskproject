import requests

host = 'http://128.1.12.88:5000/sum3/'
'''
r = requests.post(host,json=  {'a':1,'b':2})
assert r.json() == {'sum':3}
'''
'''
r = requests.post(host,json= {'data':[ 1, 2, 3 ]})

assert r.json() == {'sum':6}
'''
r = requests.post(host,json= {'a':1,'b':2, 'c':3})
assert r.json() == {'sum':6}






