.PHONY: logs, stop
.SILENT:

run: clean stop down
	docker-compose up --build -d

logs:
	docker-compose logs -f

stop:
	docker-compose stop

down:
	docker-compose down --remove-orphans

clean:
	find . -name "*.pyc" -delete && \
	find . -name "__pycache__" -delete
