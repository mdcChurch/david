from flask import jsonify, request
from . import users_bp

# Mock 데이터
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
]


# GET: 모든 사용자 가져오기
@users_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(users), 200


# POST: 새로운 사용자 추가
@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201
