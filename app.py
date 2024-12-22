from flask import Flask

from domain.recommend import recommend_bp
from domain.users import users_bp

app = Flask(__name__)

# Blueprint 등록
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(recommend_bp, url_prefix="/verse")

if __name__ == "__main__":
    app.run(debug=True)
