# Machine learning biotite thermometer
This repository contains the single-crystal biotite thermometer presented in "Calibration, validation, and evaluation of machine learning thermobarometers in metamorphic petrology: an application to biotite and outlook for future strategy" by Hartmeier et al. (2025).

# Installation
The machine learning biotite thermometer requires Python `>3.10`. Makes sure you have installed python beforehand. If you are using macOS your machine should have a preinstalled version of python 3. If you need to install python, we recommend the installation via [miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main).

To use the thermometer you can download this repository (or ```git clone https://github.com/Philipsite/ml-bt-thermometer.git```) into any directory on your machine.

## macOS and Linux-based systems
Once downloaded, open a terminal and navigate into the directory where you saved the `ml-bt-thermometer` repository by typing:
```
cd "<PATH_NAME>/ml-bt-thermometer"
```
***NOTE**: The quotation marks around the PATH NAME make sure that paths with special characters or space will not cause a problem. Replace PATH NAME by the path where you saved the repository. E.g., `/Users/philip/Research/thermobarometry`*

Run the installation script [install.sh](install.zsh) to install all required dependencies:
```
chmod +x install.zsh
./install.zsh
```

## Windows
Once downloaded, open the directory in the file explorer. Start the installation of all required dependencies by double-clicking [install.bat](install.bat).

# Usage

The machine learning thermometer comes as interactive [jupyter notebook](ml_bt_thermometer.ipynb).

## macOS and Linux-based systems
Run [run.sh](run.zsh) to start up the notebook use the following terminal commands.

Navigate into the directory where you saved the `ml-bt-thermometer` repository by typing:
```
cd "<PATH_NAME>/ml-bt-thermometer"
```

```
chmod +x run.zsh
./run.zsh
```

## Windows
Double-click [run.bat](run.bat) to start up the notebook.
