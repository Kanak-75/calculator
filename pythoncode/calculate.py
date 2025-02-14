from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get("expression")

        # Safe evaluation using eval with restricted globals
        result = eval(expression, {"__builtins__": None}, {})

        return jsonify({"result": result})
    except Exception:
        return jsonify({"result": "Invalid Expression"}), 400

if __name__ == '__main__':
    app.run(debug=True)
