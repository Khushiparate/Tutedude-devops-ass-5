from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from the Node.js frontend

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    name      = data.get('name', '').strip()
    email     = data.get('email', '').strip()
    student_id = data.get('student_id', '').strip()
    course    = data.get('course', '').strip()
    message   = data.get('message', '').strip()

    # Basic validation
    if not name or not email or not student_id or not course:
        return jsonify({"error": "All required fields must be filled"}), 400

    print(f"[FORM SUBMITTED] Name: {name} | Email: {email} | "
          f"Student ID: {student_id} | Course: {course} | Message: {message}")

    return jsonify({
        "success": True,
        "message": f"Hello {name}! Your form has been submitted successfully.",
        "data": {
            "name": name,
            "email": email,
            "student_id": student_id,
            "course": course,
            "message": message
        }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
