# Thank you very much for this opportunity!
## Requirements

1. Please make sure your operating system has Python3@latest installed.

2. Prior to running the application, please make sure to run the following command in order to install all necessary dependencies listed in the requirements.txt file:

```zsh
pip install -r requirements.txt
```

## How to run
### Start Application

1. Run the application by typing the following command in your terminal:

```zsh
python3 main.py
```

By running this command we `log the output to the terminal`, and in addition to this write our output to a folder called `output/`. The `output/` folder gives access to multiple files, which are the respective Sort outputs in addition to a master file containing all outputs.

### Tests

1. In order to run our tests, please make sure the requirements text is installed as we are using py.test to run the tests.

```zsh 
python3 -m pytest --no-header -v
```

2.  In order to run the specified tests we can instead run the following command:

```zsh
python3 -m pytest tests/<x>_Sort_test.py --no-header -v
```

where `<x>` is any of the listed:

- `first` for the First Sort
- `second` for the Second Sort
- `third` for the Third Sort

## Suggestions