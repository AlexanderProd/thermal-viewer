<!-- AUTO-GENERATED-CONTENT:START (STARTER) -->
<h1 align="center">
  <img alt="Logo" src="ressources/icon.png" height="100px" />
  <br/>
  ThermalViewer
</h1>

## Description

ThermalViewer is a PyQt6-based application for viewing the video feed of a connected Thermal Imaging camera via USB UVC connection. It allows you to change filters, save still images and record videos.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:

```bash
git clone [your-repository-url]
cd thermal-viewer
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

Note: Some dependencies like `flirpy` are installed directly from GitHub. Make sure you have git installed on your system.

## Running the Application

To run the application in development mode:

```bash
python src/main.py
```

## Building the Application

ThermalViewer can be built into a standalone executable using PyInstaller:

1. Make sure you have all dependencies installed
2. Run the build script:

```bash
chmod +x build.sh  # On Unix systems, make the script executable
./build.sh         # On Unix systems
# OR
sh build.sh       # Alternative method
# OR on Windows:
pyinstaller --onefile --icon=ressources/icon.ico --name=ThermalViewer src/main.py
```

The built executable will be available in the `dist` directory.

## Dependencies

Key dependencies include:

- PyQt6 - GUI framework
- OpenCV - Image processing
- flirpy - FLIR thermal image processing
- matplotlib - Plotting and visualization
- numpy - Numerical computations

For a complete list of dependencies, see `requirements.txt`.

## License

[Add your license information here]
