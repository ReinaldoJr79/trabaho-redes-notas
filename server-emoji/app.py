from flask import Flask, jsonify
import random

app = Flask(__name__)

# Lista de emojis
emojis = ["📝", "📓", "🗒️", "📜", "🖋️", "📌", "✏️", "📋", "🗂️", "🗃️"]

@app.route('/emoji-aleatorio', methods=['GET'])
def emoji_aleatorio():
    emoji = random.choice(emojis)
    return jsonify({"emoji": emoji})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
