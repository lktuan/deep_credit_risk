from setuptools import setup, find_packages

setup(
    name="dcr",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'dcr': ['*.csv'],  # This ensures dcr.csv is included
    }
)