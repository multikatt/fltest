from flask import Flask
from socket import gethostname, gethostbyname

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello from %s || %s' % (gethostname(),
                                    gethostbyname(gethostname()))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
