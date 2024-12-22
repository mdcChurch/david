from flask import Blueprint

# Blueprint 정의
recommend_bp = Blueprint("recommend", __name__)

# 엔드포인트 등록
from . import controllers
