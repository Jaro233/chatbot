from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the GPT-Neo pipeline
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-125M')

@app.route("/")
def index():
    return app.send_static_file('index.html')

@app.route("/chat", methods=["POST"])
def chat_with_dialgpt():
    user_input = request.json["input"]
    
    # Generate response using GPT-Neo
    responses = generator(user_input, max_length=50, num_return_sequences=1)
    gpt_response = responses[0]['generated_text']
    
    # Cleaning up the response to remove the input part (if needed)
    clean_response = gpt_response[len(user_input):].strip()
    
    return jsonify({"response": clean_response})
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
