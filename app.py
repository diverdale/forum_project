from src import app
from flask import render_template
from flask_login import current_user


@app.route('/')
def index():
    print(f'current user: {current_user.user_username}')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
