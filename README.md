# Keynote for: "Deep Credit Risk — Machine Learning in Python" by Daniel Roesch and Harald Scheule

My note and coding along with this book. Follow the below steps to run codes:

## 1 Create and activate environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows) - it depends on your OS
.venv\Scripts\activate
```

## 2 Make sure your Jupyter notebook uses this env

```bash
# Install ipykernel in your virtual environment
pip install ipykernel

# Create a kernel for your virtual environment
python -m ipykernel install --user --name=dcr_env
```

## 3 Install packages

```bash
# install the dcr
pip install -e .

# install other dependencies
pip install -r .\requirements.txt
```

When running the notebook, remember to choose `dcr_env` under the Jupyter kernel.