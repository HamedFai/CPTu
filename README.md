# Marine CPTu Data Analyzer

An interactive, browser-based tool for visualizing Piezocone Penetration Test (CPTu) data specifically formatted for marine sediment assessment. 

**No installation required.** This application runs entirely in your web browser using WebAssembly (via stlite/Pyodide).

## Live Demo
[REPLACE THIS WITH YOUR GITHUB PAGES URL]
*(e.g., https://yourusername.github.io/your-repo-name/)*

## 🛠 Features
* **Zero Setup:** No Python or library installation needed on the user's machine.
* **Geotechnical Visualization:** Automatic generation of three-panel subplots:
    * **QC (MPa):** Cone Tip Resistance
    * **FS (kPa):** Sleeve Friction
    * **U2 (kPa):** Pore Water Pressure
* **Marine Optimized:** Handles standard `.cpt` file headers and data structures (comma-separated `#` sections).
* **Interactive Plots:** Powered by Plotly—zoom, pan, and hover to inspect data at specific depths.

## Supported Data Format
The processor is designed to parse `.cpt` files with the following structure:
* **Header:** Metadata lines starting with symbols like `$`, `£`, or `!`.
* **Data Section:** Begins with `#` and contains comma-separated values in `Key=Value` format (e.g., `D=6.700,QC=0.274,FS=1.80,U=138.57`).

## How to Use
1.  Open the [Live Demo Link].
2.  Click the **"Upload .cpt file"** button.
3.  Select your file from your local machine.
4.  View the generated profiles and download the processed data table if needed.

## Developer Setup (Local)
If you wish to modify the code and run it locally:
1.  Clone the repository:
    ```bash
    git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
    ```
2.  Open `index.html` in any modern web browser. 
    *Note: Some browsers may require a local server to run WebAssembly. You can use `python -m http.server` and visit `localhost:8000`.*

---
*Developed for Educational Purposes Only.*
