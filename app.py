# Task-5
# Portfolio Website with Flask
# Author: Bineesha K P
# Date: 01-07-2025
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    response = f"Thank you, {name}! Your message has been received."
    return render_template('index.html', message=response)

if __name__ == '__main__':
    app.run(debug=True)
