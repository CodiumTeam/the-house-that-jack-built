# To check if Makefile has correct syntax (all must be tabs (^I), no spaces)
# cat -e -t -v Makefile
.PHONY: tests docker-tests
tests:
	./vendor/bin/phpunit

docker-tests:
	@docker run --rm -v "${PWD}:/code" -w /code php:8.0 make tests

