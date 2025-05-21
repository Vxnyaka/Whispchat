from flask import Flask, request

app = Flask(__name__)

@app.route('/chat/<room>', methods=['GET', 'POST'])
def chat(room):
    messages = ["User1: Hello", "User2: Hi there!"]  # Example messages

    # Simple HTML right inside the route
    return f'''
    <!DOCTYPE html>
    <html>
    <head><title>Chat Room {room}</title></head>
    <body>
        <h1 style="color: red;">THIS IS A TEST CHANGE</h1>
        <h2>Room: {room}</h2>
        <div>
            {"<br>".join(messages)}
        </div>
    </body>
    </html>
    '''
