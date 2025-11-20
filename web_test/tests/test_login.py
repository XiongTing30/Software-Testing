import requests
import multiprocessing
import time
from app import app

def run_server():
    app.run(port=5000)

def test_login():
    # 启动服务
    p = multiprocessing.Process(target=run_server)
    p.start()
    time.sleep(1)  # 等服务启动

    url = "http://127.0.0.1:5000/login"

    # 1. 用户不存在
    res = requests.post(url, json={"username": "bob", "password": "123"})
    assert res.status_code == 400
    assert "用户不存在" in res.json()["error"]

    # 2. 密码错误
    res = requests.post(url, json={"username": "testuser", "password": "wrong"})
    assert res.status_code == 400
    assert "密码错误" in res.json()["error"]

    # 3. 正确登录
    res = requests.post(url, json={"username": "testuser", "password": "123456"})
    assert res.status_code == 200
    assert res.json()["status"] == "登录成功"

    # 关闭服务
    p.terminate()
