# Script
# Step 1
# -e  Exit immediately if a command exits with a non-zero status.
# -x  Print commands and their arguments as they are executed.
set -ex

# Remove old virtualenv if it exists
rm -rf .virtualenv

# Create virtualenv
python3.6 -m venv .virtualenv

# Upgrade pip and tools
.virtualenv/bin/python3.6 -m pip install --upgrade pip setuptools wheel

# Step 2
# Install requirements
.virtualenv/bin/python3.6 -m pip install -r /var/selenium-test/nais_selenium/requirements.txt

# Step 3
# Run selenium tests
cwd=$(pwd)
cd /var/selenium-test/nais_selenium/tests
$cwd/.virtualenv/bin/python3.6 -m pytest -v -s --alluredir=$cwd/test-results test_jenkins.py