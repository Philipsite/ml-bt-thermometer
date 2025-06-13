echo "🔧 Setting up a Python virtual environment..."
python3 -m venv .venv
echo "✅ Virtual environment created."

echo "📦 Installing dependencies..."
# Activate virtual environment
source .venv/bin/activate
# Upgrade pip
pip install --upgrade pip
# Install required packages
pip install -r requirements.txt
echo "✅ Dependencies installed."
