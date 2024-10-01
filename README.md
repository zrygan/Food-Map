# Food-Map

## Before Using

You can skip the text below (only if you're on windows), just simply run `init.bat` in the command prompt.

### Using `venv`
(optional) set up a Python virtual environment first. To set this up run the following code:

Initialize python virtual environment as venv

```
python -m venv venv
```

Activate the virtual environment

```
venv\Scripts\activate
```

Your terminal should now look like

```
(venv) C:\Users\..
```

### Installing dependencies

The dependencies of this project are:

* [NetworkX](https://networkx.org/)
* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)

To install these, run the following command:

> If the you have the virtual environment remember to be inside `venv`.

```
pip install -r requirements.txt
```