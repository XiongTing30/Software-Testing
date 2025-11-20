# file: run_tests_with_coverage.py

from coverage import Coverage
import pytest

def run_tests():
    # 创建 Coverage 对象
    cov = Coverage()
    cov.start()

    # 运行 pytest
    pytest.main(["-v"])

    # 停止覆盖率统计
    cov.stop()
    cov.save()

    # 生成 HTML 报告
    cov.html_report(directory='htmlcov')
    print("覆盖率报告已生成：htmlcov/index.html")

if __name__ == "__main__":
    run_tests()
