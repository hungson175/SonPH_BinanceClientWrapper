# SonPH_BinanceClientWrapper
## Description

This project, `SonPH_BinanceClientWrapper`, is a Python package designed to provide a simplified and efficient way to interact with the Binance API, particularly focusing on futures trading. By abstracting the complexities of the Binance futures API, this wrapper allows developers and traders to focus more on strategy implementation and less on technical details.

## Notes:
The code works only for Hedge-Mode  

```Go into Binance > Settings > Position Mode > Hedge Mode)```

This mode support opening both Long and Short positions of the same asset at the same time 

## Features

- Simplified functions to interact with Binance Futures API
- Seamless integration with existing Python trading frameworks
- Automated test suite for reliability and continuous integration
- Docker support for easy deployment and isolation
- Utility scripts for common tasks and maintenance
- Sample bot implementation to demonstrate usage

## Installation

Ensure that you have [Python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-22-04)/[Poetry](https://www.digitalocean.com/community/tutorials/how-to-install-poetry-to-manage-python-dependencies-on-ubuntu-22-04) installed on your system. If not, you can follow installing [Python]  

To set up the `SonPH_BinanceClientWrapper` for development or use, clone the repository and install the dependencies using Poetry:

```bash
git clone https://github.com/hungson175/SonPH_BinanceClientWrapper.git
cd SonPH_BinanceClientWrapper
poetry install
```

## Usage

Before running any scripts, make sure to set your API_KEY and SECRET_KEY in the `.env` file. You can use the provided `bot_sample.py` as a starting point for creating your own trading bot. To run the sample bot, use the following command:

```bash
poetry run python bot_sample.py
```

To run tests and ensure everything is set up correctly:

```bash
poetry run pytest
```
