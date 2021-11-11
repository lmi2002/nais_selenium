# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# Remove old virtualenv if it exists
rm -rf .virtualenv

cd nais_selenium

# Create virtualenv
python3.6 -m venv .virtualenv


# Upgrade pip and tools
./.virtualenv/bin/python3.6 -m pip install --upgrade pip setuptools wheel

# 2 Step
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
# set -ex

# Install requirements.txt
./.virtualenv/bin/python3.6 -m pip install -r ./requirements

# 3 Step
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# 4 Step
# Run test
cd ./tests
../.virtualenv/bin/python3.6 -m pytest -m first