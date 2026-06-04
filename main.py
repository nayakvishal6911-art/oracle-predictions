from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>🔮 Oracle - AI Prediction App</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Google AdSense Code -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-1701635001084534"
         crossorigin="anonymous"></script>
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
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
        
        h1 {
            color: #667eea;
            font-size: 32px;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: #667eea;
            font-size: 16px;
            margin-bottom: 30px;
        }
        
        input, select, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 2px solid #667eea;
            border-radius: 8px;
            font-size: 16px;
        }
        
        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            cursor: pointer;
            border: none;
            font-weight: bold;
            transition: transform 0.2s;
        }
        
        button:hover {
            transform: scale(1.05);
        }
        
        button:active {
            transform: scale(0.95);
        }
        
        .prediction-box {
            background: linear-gradient(135deg, #fff9e6 0%, #ffe6f0 100%);
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
            min-height: 80px;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
        }
        
        .prediction-text {
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
        
        .subtitle-prediction {
            font-size: 14px;
            color: #666;
            margin-top: 10px;
        }
        
        .ad-container {
            margin: 20px 0;
            background: #f5f5f5;
            padding: 10px;
            border-radius: 8px;
            min-height: 280px;
            text-align: center;
        }
        
        .ad-text {
            color: #999;
            font-size: 12px;
            padding: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔮 Oracle</h1>
        <p class="subtitle">Ask the cosmos for guidance</p>
        
        <form method="POST" action="/predict">
            <input type="text" name="name" placeholder="Enter your name" required>
            
            <select name="prediction_type" required>
                <option value="">Select Prediction Type</option>
                <option value="lucky">Lucky Numbers</option>
                <option value="money">Money</option>
                <option value="trend">Trend</option>
                <option value="personality">Personality</option>
                <option value="love">Love</option>
            </select>
            
            <button type="submit">⚡ Reveal My Prediction</button>
        </form>
        
        {% if prediction %}
        <div class="prediction-box">
            <div>
                <div class="prediction-text">{{ prediction }}</div>
                <div class="subtitle-prediction">{{ message }}</div>
            </div>
        </div>
        {% endif %}
        
        <!-- Google AdSense Ad Space -->
        <div class="ad-container">
            <ins class="adsbygoogle"
                 style="display:block"
                 data-ad-client="ca-pub-1701635001084534"
                 data-ad-slot="1234567890"
                 data-ad-format="auto"
                 data-full-width-responsive="true"></ins>
            <script>
                 (adsbygoogle = window.adsbygoogle || []).push({});
            </script>
            <div class="ad-text">Advertisement</div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    message = None
    
    if request.method == 'POST':
        name = request.form.get('name', '')
        prediction_type = request.form.get('prediction_type', '')
        
        if name and prediction_type:
            if prediction_type == 'lucky':
                numbers = [random.randint(1, 99) for _ in range(5)]
                prediction = f"🍀 Lucky Numbers: {', '.join(map(str, numbers))}"
                message = "Play these numbers!"
            
            elif prediction_type == 'money':
                amount = random.randint(100, 99999)
                prediction = f"💰 Money Prediction: ₹{amount:,} in your path"
                message = "Fortune awaits!"
            
            elif prediction_type == 'trend':
                trends = ["📈 GROWTH coming soon!", "📉 Patience needed", "🌟 Success ahead!", "⚡ Change incoming"]
                prediction = random.choice(trends)
                message = "Trust the universe"
            
            elif prediction_type == 'personality':
                traits = ["Confident 💪", "Creative 🎨", "Wise 🧠", "Charismatic ✨", "Kind 💚"]
                prediction = f"Your trait: {random.choice(traits)}"
                message = "Embrace it!"
            
            elif prediction_type == 'love':
                compatibility = random.randint(1, 100)
                prediction = f"💕 Love compatibility: {compatibility}%"
                message = "Follow your heart!"
    
    return render_template_string(HTML, prediction=prediction, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=False)
