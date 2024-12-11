import sys
import os
import sys
sys.path.append('C:/Users/mishr/OneDrive/Desktop/web_protection_tool/protect')

from protect.middleware import ProtectionMiddleware

# Add the parent directory (your project directory) to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from protect.middleware import ProtectionMiddleware

from flask import Flask, request, render_template_string
from protect.middleware import ProtectionMiddleware

app = Flask(__name__)
app.wsgi_app = ProtectionMiddleware(app.wsgi_app)  # Apply middleware

@app.route('/')
def index():
    return render_template_string('<h1>Test Page</h1><form method="post"><input name="username"><input name="password"><input type="submit"></form>')

@app.route('/', methods=['POST'])
def form_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # Simulate the use of these values
    return f'Form submitted with Username: {username} and Password: {password}'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# if __name__ == '__main__':
#     app.run(debug=True)
