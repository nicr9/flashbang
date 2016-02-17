COMPOSE=docker-compose --project-name flashbang

all: build-all flashbang-up

build-all:
	$(COMPOSE) build

flashbang-up:
	$(COMPOSE) up -d flashbang

logs:
	$(COMPOSE) logs
