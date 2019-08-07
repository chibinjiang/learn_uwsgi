from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>Hello World</span>"


if __name__ == '__main__':
    app.run()

