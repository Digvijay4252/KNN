from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

model = joblib.load('model.pkl')
outcome_map = joblib.load('outcome_map.pkl')
outcome_map_rev = {v: k for k, v in outcome_map.items()}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':     
        try:
            inputs = [
                float(request.form['pregnancies']),
                float(request.form['glucose']),
                float(request.form['bp']),
                float(request.form['skin']),
                float(request.form['insulin']),
                float(request.form['bmi']),
                float(request.form['dpf']),
                float(request.form['age']),
            ]
            pred_num = model.predict([inputs])[0]
            prediction = outcome_map_rev.get(pred_num, "Unknown")
        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
