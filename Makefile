build:
	@docker build -t python-ci .

pytest:
	@docker run \
		--name python-ci \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-it \
		-v $(PWD):/src \
		python-ci pytest .
