.PHONY: default test coverage docker-test docker-coverage
default: docker-test

test:
	python3 -m unittest

coverage:
	coverage run --source=the_house_that_jack_built -m unittest
	coverage report
	coverage html
	@printf "To visualize the lines open the report at htmlcov/index.html\n"

docker-test:
	docker run --rm -v  C:\Users\503046872\Documents\CODE\the-house-that-jack-built\python:/kata codiumteam/tdd-training-python make test

docker-coverage:
	@docker run --rm -v ${PWD}:/kata codiumteam/tdd-training-python make coverage