# python_package_sample

## install

- Install using pip.

```shell
% pip install git+https://github.com/nokonoko1203/python_package_sample.git
```

- using pipenv

```shell
% pipenv install git+https://github.com/nokonoko1203/python_package_sample.git#egg=python_package_sample
```

## usage

```python
from python_package_sample import sample_function

def main():
    print(sample_function())


if __name__ == '__main__':
    main()
```

## for develop

### setup

```shell
% export PIPENV_IGNORE_VIRTUALENVS=1
% export PIPENV_VENV_IN_PROJECT=true
% pipenv install
```

### test

```shell
% pipenv run python -m unittest discover tests
run a test of sample_function
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```
