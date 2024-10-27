# Keynote for: "Deep Credit Risk — Machine Learning in Python" by Daniel Roesch and Harald Scheule

My note and coding along with this book

# Setup

## 1 Create and activate environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
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
pip install -e .

pip install -r .\requirements.txt
```