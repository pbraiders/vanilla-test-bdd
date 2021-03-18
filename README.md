# PBRaiders Vanilla BDD library

Behavioral driven development library for [PBRaiders Vanilla](https://github.com/pbraiders/vanilla) using [pytest-bdd](https://github.com/pytest-dev/pytest-bdd)

## Table of Contents

- [Requirements](#requirements) | [Installation](#installation) | [Documentation](#documentation) | [Contributing](#contributing) | [License](#license)

## Requirements

- python: ^3.8
- python3-pip: ^20.1
- python modules: pipenv, selenium, pytest, pytest-bdd, pytest-splinter
- web drivers: chromium-chromedriver or/and firefox-geckodriver

## Installation

*On Ubuntu Desktop 20.04*

### Installing Web Drivers

A driver is required to interact with the specified browser. Each browser has a particular
Selenium WebDriver associated with it, so you need to install any one of the drivers
provided; for example, geckodriver is a Selenium WebDriver that only operates with
Mozilla Firefox.

Run:

```bash
apt-get install chromium-chromedriver firefox-geckodriver
```

### Installing Python

This project requires an up-to-date version of Python 3. Run:

```bash
apt-get install python3 python3-pip
```

### Installing Python modules

This project uses pipenv to manage packages in an virtual environment.

Install pipenv using Pipx:

```bash
pip install --user pipx
pipx install pipenv
```

or install pipenv without pipx:

```bash
pipx install --user pipenv
```

### Setup

To set up this project on your local machine:

1. Clone it from this GitHub repository.
2. Run pipenv install from the command line in the project's root directory.
3. ...

## Documentation

- [Python](https://docs.python.org/3.8/)
- [pip](https://pip.pypa.io/en/stable/)
- [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-pipenv)
- [pytest](https://docs.pytest.org/en/stable/contents.html)
- [pytest-bdd](https://pytest-bdd.readthedocs.io/en/stable/)

## Contributing

Thanks you for taking the time to contribute. Please fork the repository and make changes as you'd like.

If you have any ideas, just open an [issue](https://github.com/pbraiders/vanilla-test-bdd/issues) and tell me what you think. Pull requests are also warmly welcome.

If you encounter any **bugs**, please open an [issue](https://github.com/pbraiders/vanilla-test-bdd/issues).

Be sure to include a title and clear description,as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.

## License

**PBRaiders Vanilla BDD library** is open-source and is licensed under the [MIT License](https://github.com/pbraiders/vanilla-test-bdd/blob/master/LICENSE).
