# Keynote for: "Deep Credit Risk — Machine Learning in Python" by Daniel Roesch and Harald Scheule

My note and coding along with this book. Follow the below steps after cloning this repository to run codes:

## Setup

### 1 Create and activate environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows) - it depends on your OS
.venv\Scripts\activate
```

### 2 Make sure your Jupyter notebook uses this env

```bash
# Install ipykernel in your virtual environment
pip install ipykernel

# Create a kernel for your virtual environment
python -m ipykernel install --user --name=dcr_env  --display-name "DCR Environment"
```

### 3 Install packages

```bash
# install the dcr
pip install -e .

# install other dependencies
pip install -r .\requirements.txt
```

When running the notebook, remember to choose "**DCR Environment**" under available kernel.

## Note

The `dcr.py` and `dcr.csv` all credit to the author of the book, these files can be downloaded from the book's website: <https://www.deepcreditrisk.com>. I just replaced the `data` definition in the code with:

```python
import os

# Get the directory where dcr.py is located
module_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(module_dir, 'dcr.csv')
data = pd.read_csv(csv_path)
```