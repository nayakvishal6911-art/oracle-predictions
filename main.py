from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🔮 Oracle - AI Prediction App</title>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 90%;
            text-align: center;
        }
        h1 { color: #667eea; font-size: 32px; }
        input, select, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 2px solid #667eea;
            border-radius: 8px;
            font-size: 16px;
            box-sizing: border-box;
        }
        button {
            background: #667eea;
            color: white;
            cursor: pointer;
            font-weight: bold;
            border: none;
        }
        button:hover { background: #764ba2; }
        .result {
            background: #fffde7;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Oracle</h1>
        <p>Ask the cosmos for guidance</p>
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <select name="prediction_type" required>
                <option value="">Select Prediction Type</option>
                <option value="lucky">🍀 Lucky Numbers</option>
                <option value="money">💰 Money Prediction</option>
                <option value="trend">📈 Future Trend</option>
                <option value="personality">🎭 Personality</option>
                <option value="love">💕 Love Prediction</option>
            </select>
            <button type="submit">⚡ Reveal My Prediction</button>
        </form>
        {% if result %}
            <div class="result">{{ result }}<br><br>{{ details }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    details = None
    
    if request.method == 'POST':
        name = request.form.get('name', '')
        prediction_type = request.form.get('prediction_type')
        
        if prediction_type == 'lucky':
            number = random.randint(1, 99)
            result = f"🔮 {name}, your lucky number is: {number}"
            details = "This number brings good fortune!"
        elif prediction_type == 'money':
            amount = random.randint(100, 10000)
            result = f"💰 {name}, predicted earnings: ${amount}"
            details = "Invest wisely!"
        elif prediction_type == 'trend':
            trend = random.choice(['📈 Rising', '➡️ Stable', '📉 Declining'])
            result = f"{trend} - {name}'s future is good!"
            details = "Plan accordingly."
        elif prediction_type == 'personality':
            ptype = random.choice(['Creative 🎨', 'Logical 🧠', 'Social 👥', 'Leader 👑'])
            result = f"🎭 Your personality: {ptype}"
            details = "Embrace your strengths!"
        elif prediction_type == 'love':
            score = random.randint(1, 100)
            result = f"💕 Love compatibility: {score}%"
            details = "Follow your heart!"
    
    return render_template_string(HTML, result=result, details=details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
