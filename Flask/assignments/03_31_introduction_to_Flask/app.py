from flask import Flask

# Flask application instance
app = Flask(__name__)

# route for the root URL
@app.route('/')
def hello_world():            # view function 
    return 'Hello world'

if __name__ == '__main__':
    # enable debugging mode
    app.run(debug=True)