#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

echo "Starting the build process..."

# Install Python (if not installed)
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found, installing..."
    apt-get update && apt-get install -y python3 python3-pip
else
    echo "Python3 is already installed."
fi


# Use pip3 if pip is not available
pip_cmd=$(command -v pip || command -v pip3)
echo "Using pip command: $pip_cmd"

# Install dependencies
echo "Installing dependencies..."
$pip_cmd install -r requirements.txt || { echo "Dependency installation failed"; exit 1; }

# Set the STATIC_ROOT directory to match Vercel's expected output
export STATIC_ROOT=staticfiles_build

# Create the output directory
mkdir -p $STATIC_ROOT

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput || { echo "Static files collection failed"; exit 1; }

echo "Build process completed successfully."
