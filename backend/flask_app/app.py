from flask import flask, jsonify
app = Flask(__name__)
@app.get("/api/hello")
def hello():
return jsonify({"message":"hello from flask!"})
if __name__=="__name__";
app.run(host="0.0.0.0", port=5000)
