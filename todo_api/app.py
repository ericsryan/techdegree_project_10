from flask import Flask

import models

from resources.todos import todos_api


app = Flask(__name__)
app.register_blueprint(todos_api)


@app.route('/')
def index():
    return "Welcome to a TODO API!"


if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=8000)
