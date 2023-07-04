install:
	pip3 install --upgrade pip && pip3 install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C $$(git ls-files '*.py')

all: install format lint
