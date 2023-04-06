from flask import Flask, request

app = Flask(__name__)

@app.route('/callback')
def callback():
    username = request.args.get('username')
    return 'Received username: {}'.format(username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)