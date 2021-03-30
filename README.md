# PBRaiders Vanilla BDD library

Behavioral driven development library for [PBRaiders Vanilla](https://github.com/pbraiders/vanilla) using [pytest-bdd](https://github.com/pytest-dev/pytest-bdd) and [pytest-splinter](https://github.com/pytest-dev/pytest-splinter)

## Table of Contents

- [Requirements](#requirements) | [Installation](#installation) | [Running the tests](#running) | [Documentation](#documentation) | [Contributing](#contributing) | [License](#license)

## Requirements

- pbraiders: latest vanilla
- python: ^3.8
- python3-pip: ^20.1
- python3-venv: ^3.8
- python modules: selenium, pytest, pytest-bdd, pytest-splinter
- web drivers: chromium-chromedriver or/and firefox-geckodriver

## Installation

*On Ubuntu Desktop 20.10*


### Installing PBRaiders

Install the latest [PBRaiders vanilla version](https://github.com/pbraiders/vanilla) using the [documentation](https://github.com/pbraiders/vanilla/blob/master/doc/install/install.fr_FR.md)

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
apt-get install python3 python3-pip python3-venv
```

### Installing Python modules

This project uses [venv](https://docs.python.org/3.8/tutorial/venv.html) to manage packages in an virtual environment.
To set up the project on your local machine:

1. Clone it from this GitHub repository.
2. Run: `python3 -m venv .venv` from the command line in the project's root directory to create the virtual environment.
3. Run: `source .venv/bin/activate` to activate the virtual environment.
4. Run: `pip install -r requirements.txt` to install all the necessary packages.

## Running the tests

Update the website [configuration file](tests/config.json)

Once the virtual environment activated, the command used to run the tests is `python -m pytest`.
Also, there is a provision to run the tests by providing the tag names.
It can be achieved by appending `-k` and the tag name. e.g. `python -m pytest -k adm`

This framework uses pytest-html plugin to generate html reports for the test runs.
To generate a report, run the command pipenv run python -m pytest -k automated --html=report.html

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
