COMPOSE=docker-compose --project-name kanji

all: build-all kanji-up

build-all:
	$(COMPOSE) build

kanji-up:
	$(COMPOSE) up -d kanji
