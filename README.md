# Test NLP Environment

Running the tests in this repo will provide an understanding of the capabilities of the current environment, with specific regards to GPU device.

Topics of tests include:

* basic python
* cuda gpu
* pytorch
* spacy

Check test method docstrings for specifics on what is being tested.  Currently, 5 tests should fail if no GPU device is available.


## Development

```
pip install pipenv
pipenv install
pipenv shell
pytest
```

Generate requirements with: `pipenv run pip freeze > requirements.txt`


## Operation

```
pip install -r path/to/requirements.txt
pytest
```