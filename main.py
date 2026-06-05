from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
    <title>Oracle - AI Prediction</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1701635001084534"
         crossorigin="anonymous"></script>
    <style>
        body {
            font-family: Arial;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }
        h1 { color: #667eea; margin: 0 0 10px 0; }
        p { color: #667eea; margin: 0 0 20px 0; }
        input, select, button {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 2px solid #667eea;
            border-radius: 8px;
            font-size: 16px;
        }
        button {
            background: #667eea;
            color: white;
            cursor: pointer;
            border: none;
            font-weight: bold;
        }
        .result {
            background: #fff9e6;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            font-size: 18px;
            font-weight: bold;
        }
        .ad { margin: 20px 0; min-height: 100px; background: #f5f5f5; padding: 10px; border-radius: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Oracle</h1>
        <p>Ask the cosmos for guidance</p>
        
        <form method="POST">
            <input type="text" name="name" placeholder="Enter your name" required>
            <select name="type" required>
                <option value="">Select Prediction Type</option>
                <option value="lucky">Lucky Numbers</option>
                <option value="money">Money</option>
                <option value="trend">Trend</option>
                <option value="love">Love</option>
            </select>
            <button type="submit">⚡ Reveal My Prediction</button>
        </form>
        
        {% if result %}
        <div class="result">{{ result }}<br><small>{{ msg }}</small></div>
        {% endif %}
        
        <div class="ad">
            <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-1701635001084534" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
            <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>
        </div>
    </div>
</body>
</html>"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    msg = None
    
    if request.method == 'POST':
        name = request.form.get('name')
        ptype = request.form.get('type')
        
        if ptype == 'lucky':
            nums = [random.randint(1, 99) for _ in range(5)]
            result = f"🍀 Lucky: {', '.join(map(str, nums))}"
            msg = "Play these!"
        elif ptype == 'money':
            result = f"💰 ₹{random.randint(100, 99999):,} coming"
            msg = "Fortune awaits!"
        elif ptype == 'trend':
            result = random.choice(["📈 Growth!", "🌟 Success!", "⚡ Change!"])
            msg = "Trust it"
        elif ptype == 'love':
            result = f"💕 {random.randint(1, 100)}% compatible"
            msg = "Follow heart!"
    
    return render_template_string(HTML, result=result, msg=msg)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
