from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get("question", "")
    # Dummy response logic
    if "fever" in user_input.lower():
        return jsonify({"response": "You may have a viral infection. Drink fluids and rest. Consult a doctor if it persists."})
    return jsonify({"response": "Please provide more symptoms."})

if __name__ == "__main__":
    app.run(debug=True)
