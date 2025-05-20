from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
rooms = {}  # In-memory room:password store

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        room = request.form['room']
        password = request.form['password']
        
        # Room creation or join logic
        if room in rooms:
            if rooms[room] != password:
                return "Incorrect password!", 403
        else:
            rooms[room] = password
        
        return redirect(url_for('chat', room=room))
    
    return render_template('index.html')

@app.route('/chat/<room>', methods=['GET', 'POST'])
def chat(room):
    message_file = f"messages_{room}.txt"
    
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']
        with open(message_file, 'a') as f:
            f.write(f"{username}: {message}\n")
    
    messages = []
    if os.path.exists(message_file):
        with open(message_file, 'r') as f:
            messages = f.readlines()
    
    return render_template('chat.html', messages=messages, room=room)
