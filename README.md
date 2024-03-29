# quant-analyser

quant-analyser is a comprehensive financial data analysis tool designed to provide real-time and historical data on A-shares, Hong Kong stocks, and US stocks. It is capable of calculating various technical indicators such as Moving Average (MA), Exponential Moving Average (EMA), Relative Strength Index (RSI), Bias, and Moving Average Convergence Divergence (MACD).

### Mirrors

https://mirrors.aliyun.com/pypi/simple/
https://pypi.python.org/pypi/


#### ta-lib

```shell 
tar -xzf ta-lib-0.4.0-src.tar.gz
cd ta-lib/
./configure --prefix=/usr
make
sudo make install
c```

#### pymongoarrow

For python3.6, using: pymongoarrow==0.2.0
unable support py.string, datetime

python3.9 pymongoarrow==0.4.0


### Getting Started

```shell script
# python 3.10+ required

# Clone the repository
git clone xxx

# cd into project root
cd quant-analyser

# createing virtual environments
python3 -m venv .venv

# activate venv
source .venv/bin/activate

# install poetry inside virtual environments
pip install poetry

# install all dependencies
poetry install --no-root

```

### Using Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. Poetry offers a lockfile to ensure repeatable installs, and can build your project for distribution.

```shell script
# For example: the add command adds required packages to your pyproject.toml and installs them.
poetry add psycopg2=2.9.1
```

## Testing

In order to test and lint the project locally you need to install the poetry dependencies outlined in the pyproject.toml file.

If you have Poetry installed then it's as easy as running `poetry shell` to activate the virtual environment first and then `poetry install --no-root` to get all the dependencies.

This starter template has an example test which covers its only endpoint. To run the test, ensure you are
in the same directory as the `tox.ini` file and run `tox` from the command line. It will also perform code
linting and formatting as long as the pre-commit hooks were installed. We'll talk about that next.

# Code Formatting & Linting

To activate pre-commit formatting and linting all you need to do is run `pre-commit install` from the root of your local git repository. Now
every time you try to make a commit, the code will be formatted and linted for errors first.
