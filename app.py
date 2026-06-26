from flask import Flask, jsonify
import datetime
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Docker + Kubernetes Deployment Successful!",
        "app": "flask-k8s",
        "version": "1.0.0"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "Healthy",
        "app": "flask-k8s",
        "timestamp": str(datetime.datetime.now())
    })

@app.route("/info")
def info():
    return jsonify({
        "app": "flask-k8s",
        "description": "Python Flask app deployed on Kubernetes",
        "author": os.getenv("AUTHOR_NAME", "Your Name"),
        "environment": os.getenv("ENV", "development"),
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
