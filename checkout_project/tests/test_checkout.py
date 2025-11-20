# tests/test_checkout.py
import requests
import multiprocessing
import time
from app.checkout_service import app

def run_server():
    app.run(port=5000)

def test_checkout_total():
    # 启动服务
    p = multiprocessing.Process(target=run_server)
    p.start()
    time.sleep(1)

    # 发送系统级请求
    data = {"items": [{"price": 20, "quantity": 3}]}
    res = requests.post("http://127.0.0.1:5000/checkout", json=data)

    assert res.status_code == 200
    assert res.json()["total"] == 60

    # 关闭服务
    p.terminate()
