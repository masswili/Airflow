import os
from flask import Flask

app = Flask(__name__)

# Mendapatkan nilai argumen APP_NAME dan APP_PORT dari environment variable
app_name = os.getenv('APP_NAME', 'my-python-app')
app_port = os.getenv('APP_PORT', '8080')

@app.route('/')
def hello_world():
    return f'Hello, {app_name}!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(app_port))