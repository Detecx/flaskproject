from flask import Flask, request

app = Flask(__name__)


@app.route('/sum3/', methods=['POST'])
def hello_world():
    '''
    print(request.json)

    a = request.json['a']
    b = request.json['b']
    return {'sum': a+b}
    '''
    '''
    data = request.json['data']
    print({'sum':data})
    return {'sum':sum(data)}
    '''
    print(request.json)

    a = request.json['a']
    b = request.json['b']
    c = request.json['c']
    return {'sum': a + b + c}



app.run(host='128.1.12.88', port=5000)