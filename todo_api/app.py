from flask import Flask, render_template

import models

from resources.todos import todos_api


app = Flask(__name__)
app.register_blueprint(todos_api)
app.secret_key = 'super secret key'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    models.initialize()
    app.run(debug=True, port=8000)
