# Machine learning biotite thermometer
This repository contains the single-crystal biotite thermometer presented in "Calibration, validation, and evaluation of machine learning thermobarometers in metamorphic petrology: an application to biotite and outlook for future strategy" by Hartmeier et al. (2025).

# Installation
The machine learning biotite thermometer requires Python `>3.10`. Makes sure you have installed python beforehand. We recommend the installation via [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main).

To use the thermometer you can download this repository (or ```git clone https://github.com/Philipsite/ml-biotite-thermobarometry.git```) into any directory on your machine.

Once downloaded, open a terminal and navigate into the director where you saved the `ml-biotite-thermobarometry` repository by typing:
```
cd <PATH_NAME/ml-bt-thermometer
```
Run the installation script [install.sh](install.zsh) to install all required dependencies:
```
chmod +x install.zsh
./install.zsh
```

# Usage

The machine learning thermometer comes as interactive [jupyter notebook](ml_bt_thermometer.ipynb). If you have no previous experience with jupyter notebook, run [run.sh](run.zsh) to start up the notebook use the following terminal commands:
```
chmod +x run.zsh
./run.zsh
```
Then follow the steps in the jupyter notebook.
