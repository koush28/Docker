from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from Flask app on Kubernetes!")

@app.route("/health")
def health():
    return jsonify(status="UP")

if __name__ == "__main__":
    # Run on port 5001 (same as your Kubernetes manifest)
    app.run(host="0.0.0.0", port=5001)
