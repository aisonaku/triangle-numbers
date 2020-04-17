help:
	@echo "install           install package"
	@echo "install_dev     install package within pipenv"
	@echo "shell             activate virtualenv"
	@echo "install_test      install package for tests"

install_dev:
	pipenv install --skip-lock -e '.[dev,test]'

install_test:
	pip install '.test'

install:
	pip install .

shell:
	pipenv shell