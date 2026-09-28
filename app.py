from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

camera_status = {
    "enabled": True
}

@app.route('/')
def home():
    return "Smart Surveillance System Backend is Running!"

@app.route('/api/camera/status', methods=['GET'])
def get_camera_status():
    return jsonify(camera_status)

@app.route('/api/camera/control', methods=['POST'])
def control_camera():
    data = request.get_json()
    
    if "enabled" in data:
        camera_status["enabled"] = bool(data["enabled"])
        state_str = "Enabled" if camera_status["enabled"] else "Disabled"
        return jsonify({
            "success": True,
            "message": f"Camera module has been successfully {state_str}.",
            "camera_status": camera_status["enabled"]
        })
    
    return jsonify({"success": False, "error": "Invalid data provided."}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)