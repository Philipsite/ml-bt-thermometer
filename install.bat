echo Setting up a Python virtual environment...
python -m venv .venv
echo Virtual environment created.

echo Installing dependencies...
:: Activate virtual environment
call .venv\Scripts\activate.bat
:: Upgrade pip
pip install --upgrade pip
:: Install required packages
pip install -r requirements.txt
echo Dependencies installed.
