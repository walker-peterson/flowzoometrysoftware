from setuptools import setup, find_packages

setup(
    name="flyseg",
    version="2.2.1",
    packages=find_packages(),          # setup.py
    install_requires=[],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "flyseg-predict = flyseg.scripts.prediction:main",
            "flyseg-clean-model = flyseg.scripts.nnunet_config:clean_model_cache",
        ]
    },
)
