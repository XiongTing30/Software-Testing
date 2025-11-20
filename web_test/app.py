from flask import Flask, request, jsonify

app = Flask(__name__)

# 模拟用户数据库
users = {
    "testuser": "123456",
    "alice": "password123"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "用户不存在"}), 400
    if users[username] != password:
        return jsonify({"error": "密码错误"}), 400
    return jsonify({"status": "登录成功"}), 200

if __name__ == "__main__":
    app.run(port=5000)
