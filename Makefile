.PHONY: help lint test all format clean

help:
	@echo "可用命令:"
	@echo "  make lint     - 运行代码检查 (ruff + mypy)"
	@echo "  make test     - 运行测试"
	@echo "  make all      - 运行所有检查 (lint + test)"
	@echo "  make format   - 格式化代码"
	@echo "  make clean    - 清理生成的文件"
	@echo "  make run      - 启动开发服务器"

lint:
	ruff check .
	mypy .

test:
	pytest -v

all: lint test

format:
	ruff format .
	ruff check . --fix

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000