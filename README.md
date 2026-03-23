## Marine CPTu Data Analyzer
An interactive, browser-based tool for visualizing Piezocone Penetration Test (CPTu) data specifically formatted for marine sediment assessment.

No installation required. This application runs entirely in your web browser using WebAssembly (via stlite/Pyodide).

### Live Demo
https://hamedfai.github.io/CPTu/

### Features
Zero Setup: No Python or library installation needed on the user's machine.

Geotechnical Visualization: Automatic generation of a five-panel profile:

- qc (MPa): Cone Tip Resistance

- fs (kPa): Sleeve Friction

- u2 (kPa): Pore Water Pressure

- Rf (%): Friction Ratio

- Bq: Pore Pressure Ratio

Marine Optimized: Handles standard .cpt file headers and data structures (comma-separated # sections).

Advanced Calculations: Automatically derives Rf and Bq (assuming hydrostatic water pressure) to assist in stratigraphic interpretation and soil behavior typing.

Interactive Plots: Powered by Plotly—zoom, pan, and hover to inspect data at specific depths.

### Supported Data Format
The processor is designed to parse .cpt files with the following structure:

Header: Metadata lines starting with symbols like $, £, or !.

Data Section: Begins with # and contains comma-separated values in Key=Value format (e.g., D=6.700,QC=0.274,FS=1.80,U=138.57).

### How to Use
- Open https://hamedfai.github.io/CPTu/.
- Click the "Upload .cpt file" button.
- Select your file from your local machine.
- View the generated profiles and the processed data table below the charts.

### Developer Setup (Local)
If you wish to modify the code and run it locally:

### Clone the repository:
Bash
git clone https://github.com/hamedfai/CPTu.git
Open index.html in any modern web browser.
Note: Some browsers may require a local server to run WebAssembly. You can use python -m http.server and visit localhost:8000.

Developed for Educational Purposes Only.
