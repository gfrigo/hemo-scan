.PHONY: dev build run stop logs

dev:
	uv run fastapi dev src/hemo_scan/main.py

build:
	docker build -t hemo-scan .

run: build
	docker run --rm -d --name hemo-scan -p 8000:8000 hemo-scan

stop:
	docker stop hemo-scan

logs:
	docker logs -f hemo-scan
