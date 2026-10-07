from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "Believe you can and you're halfway there.",
    "The harder you work, the greater the reward.",
    "Don't watch the clock; do what it does. Keep going.",
    "Dream it. Wish it. Do it.",
    "Push yourself, because no one else will."
]

@app.route('/')
def home():
    quote = random.choice(quotes)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
