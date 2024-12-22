from flask import jsonify, request
from . import recommend_bp
from .services import get_recommended_verse


# GET: 사용자에 맞는 추천 성경 구절 반환
@recommend_bp.route("/", methods=["GET"])
def recommend_verse():
    # 요청에서 사용자 정보를 가져옴 (예: 이름, 관심사)
    user_info = request.args.get("user_info", "default_user")

    # 서비스 로직에서 추천 구절 가져오기
    verse = get_recommended_verse(user_info)

    return jsonify({"user": user_info, "recommended_verse": verse}), 200
