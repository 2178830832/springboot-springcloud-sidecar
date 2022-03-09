import json

from flask import Flask, Response, make_response, jsonify

app = Flask(__name__)


@app.route('/health')
def health():
    result = {'status': 'UP'}
    return Response(json.dumps(result), mimetype='application/json')


@app.route('/getUser')
def get_user():
    return Response(json.dumps({'username': 'python', 'password': 'python'}),
                    mimetype='application/json')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

