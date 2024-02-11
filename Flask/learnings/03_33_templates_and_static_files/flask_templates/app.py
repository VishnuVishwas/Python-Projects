from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    # variable
    name = "Vishnu"

    # control structures
    fruits = ['Apple', 'Banana', 'Mango']
    
    return render_template('index.html', name=name, fruits=fruits)

if __name__ == '__main__':
    app.run(debug=True)