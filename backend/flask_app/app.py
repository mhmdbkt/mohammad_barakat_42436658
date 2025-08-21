from flask import Flask, jsonify

# create flask app
app = Flask(__name__)

# simple test route
@app.get("/api/hello")
def hello():
    return jsonify({"message": "Hello from Flask!"})

# run the app
if __name__ == "__main__":   # ✅ must have double underscores
    app.run(host="0.0.0.0", port=5000, debug=True)
