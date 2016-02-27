COMPOSE=docker-compose --project-name flashbang

all: build-all web-up

build-all:
	$(COMPOSE) build

web-up:
	$(COMPOSE) up -d web

logs:
	$(COMPOSE) logs

backup:
	docker cp flashbang_web_1:/usr/src/app/data flashbang
