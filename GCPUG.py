from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/setting')
def tag():
    tag_dict = dict(request.args)['tag']
    print(tag_dict)
    return str(tag_dict)


@app.route('/realtime')
def real_time():
    code_str = request.args.get('code')
    print(code_str)
    return code_str


if __name__ == '__main__':
    app.run(host='0.0.0.0')
