from flask import Flask, render_template, send_from_directory
from urllib.parse import quote
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Music/<path:filename>')
def music_files(filename):
    return send_from_directory(os.path.join(app.root_path, 'Music'), filename)

if __name__ == '__main__':
    app.run(debug=True)





