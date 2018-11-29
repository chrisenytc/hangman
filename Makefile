setup:
	@pip install --upgrade setuptools wheel twine
.PHONY: setup

build:
	@rm -rf build dist && python setup.py sdist bdist_wheel
.PHONY: build

release:
	@twine upload dist/*
.PHONY: release
