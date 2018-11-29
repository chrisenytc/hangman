setup:
	@pip install --upgrade setuptools wheel twine
.PHONY: setup

build:
	@python setup.py sdist bdist_wheel
.PHONY: build

release:
	@twine upload dist/*
.PHONY: release
