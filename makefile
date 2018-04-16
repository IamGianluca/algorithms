build:
	pip install -r requirements.txt
	pip install -e .


tests:
	pytest --cov ml ./ml/tests
