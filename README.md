# Testnet address
`WE34ZFE6ZKF4PC7FFNQFOSB7NLC4K6IWVVOGOS5CXMESVMFGUJH6L6WJGQ`

# App ID 
`469360340`

# Playground 

This project has been generated using AlgoKit to help you quickly get started with a basic playground for experimenting with Beaker smart contracts against a [LocalNet](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/features/localnet.md) network.

See below for default getting started instructions.

# Setup

## Quick start

1. Ensure you have AlgoKit installed and run `algokit bootstrap all` in this directory
2. Open this directory in Visual Studio Code. Make sure you're using python venv.
3. Run the [build script](./playground/realtorteal/build.py) `python3 playground/realtorteal/build.py`
4. Start algokit localnet `algokit localnet start`
5. It will: start LocalNet use `algokit explore` to open the dashboard, use the contract.json and teal files from artifacts folder. 

## Detailed instructions

### Initial setup

1. Clone this repository locally
2. Install pre-requisites:
   - Install `AlgoKit` - [Link](https://github.com/algorandfoundation/algokit-cli#install): Ensure you can execute `algokit --version`.
   - Bootstrap your local environment; run `algokit bootstrap all` within this folder, which will:
     - Install `Poetry` - [Link](https://python-poetry.org/docs/#installation): The minimum required version is `1.2`. Ensure you can execute `poetry -V` and get `1.2`+
     - Run `poetry install` in the root directory, which will set up a `.venv` folder with a Python virtual environment and also install all Python dependencies
3. Open the project and start debugging / developing via:
   - VS Code
     1. Open the repository root in VS Code
     2. Install recommended extensions
        > **Note**
        > If using Windows: Before running for the first time you will need to select the Python Interpreter.
        1. Open the command palette (Cmd/Ctrl + Shift + P)
        2. Search for `Python: Select Interpreter`
        3. Select `./.venv/Scripts/python.exe`
   - IDEA (e.g. PyCharm)
     1. Open the repository root in the IDE
     2. It should automatically detect it's a Poetry project and set up a Python interpreter and virtual environment.
     3. Hit Shift+F9 (or whatever you have debug mapped to) and it should start running with breakpoint debugging.
   - Other
     1. Open the repository root in your text editor of choice
     2. In a terminal run `poetry shell`
     3. Run the [build script](./playground/realtorteal/build.py) `python3 playground/realtorteal/build.py` through your debugger of choice

### Subsequently

1. If you update to the latest source code and there are new dependencies you will need to run `algokit bootstrap all` again
2. Follow step 3 above

## Tools

The following tools are used in this project:

- [Algorand](https://www.algorand.com/) - Layer 1 Blockchain; [Developer portal](https://developer.algorand.org/), [Why Algorand?](https://developer.algorand.org/docs/get-started/basics/why_algorand/)
- [AlgoKit](https://github.com/algorandfoundation/algokit-cli) - One-stop shop tool for developers building on the Algorand network; [docs](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/algokit.md), [intro tutorial](https://github.com/algorandfoundation/algokit-cli/blob/main/docs/tutorials/intro.md)
- [Beaker](https://github.com/algorand-devrel/beaker) - Smart contract development framework for PyTeal; [docs](https://beaker.algo.xyz), [examples](https://github.com/algorand-devrel/beaker/tree/master/examples)
- [PyTEAL](https://github.com/algorand/pyteal) - Python language binding for Algorand smart contracts; [docs](https://pyteal.readthedocs.io/en/stable/)
- [AlgoKit Utils](https://github.com/algorandfoundation/algokit-utils-py) - A set of core Algorand utilities that make it easier to build solutions on Algorand.
- [Poetry](https://python-poetry.org/): Python packaging and dependency management.
