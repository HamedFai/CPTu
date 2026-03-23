# Marine CPTu Data Analyzer

An interactive, browser-based tool for visualizing Piezocone Penetration Test (CPTu) data specifically formatted for marine sediment assessment. 

**No installation required.** This application runs entirely in your web browser using WebAssembly (via stlite/Pyodide).

## Live Demo
[https://hamedfai.github.io/CPTu/](https://hamedfai.github.io/CPTu/)

## Features
* **Zero Setup:** No Python or library installation needed on the user's machine.
* **Geotechnical Visualization:** Professional six-panel profile plus an automated Stratigraphy log.
    * **qc (MPa):** Cone Tip Resistance
    * **fs (kPa):** Sleeve Friction
    * **u2 (kPa):** Pore Water Pressure
    * **Rf (%):** Friction Ratio
    * **Bq:** Pore Pressure Ratio
* **7th Edition SBT Classification:** Automated Soil Behavior Type logging based on the latest Robertson & Cabal (2022) criteria.
* **Marine Optimized:** Handles standard .cpt file headers and data structures (comma-separated # sections).
* **Textbook Quality:** High-resolution plotting with top-mounted X-axes and mirrored boundaries (boxed subplots), optimized for PDF reporting.

## Literature References
The processing logic and classification boundaries used in this tool are based on the following geotechnical standards:

* **Robertson, P. K., & Cabal, K. L. (2022).** *Guide to Cone Penetration Testing, 7th Edition.* Gregg Drilling LLC.
* **Robertson, P. K. (2010).** *Estimating in-situ soil type from CPT: a discussion.* Canadian Geotechnical Journal, 47(1), 102-109.
* **Lunne, T., Robertson, P. K., & Powell, J. J. (1997).** *Cone Penetration Testing in Geotechnical Practice.* Blackie Academic & Professional.

## Supported Data Format
The processor is designed to parse .cpt files with the following structure:
* **Header:** Metadata lines starting with symbols like `$`, `£`, or `!`.
* **Data Section:** Begins with `#` and contains comma-separated values in `Key=Value` format (e.g., `D=6.700,QC=0.274,FS=1.80,U=138.57`).

## How to Use
1. Open [https://hamedfai.github.io/CPTu/](https://hamedfai.github.io/CPTu/).
2. Click the **"Upload .cpt file"** button.
3. Select your `.cpt` or `.txt` file from your local machine.
4. View the generated profiles. 
5. **To Export for Reports:** Use your browser's Print function (**Ctrl+P** or **Cmd+P**) and select **Save as PDF**. It is recommended to use **Landscape** orientation and ensure "Background Graphics" is enabled in the print settings.

## Developer Setup (Local)
If you wish to modify the code and run it locally:
1. Clone the repository:
    ```bash
    git clone [https://github.com/hamedfai/CPTu.git](https://github.com/hamedfai/CPTu.git)
    ```
2. Open `index.html` in any modern web browser. 
   *Note: Due to browser security policies, you may need to run a simple local server (e.g., `python -m http.server 8000`) to view the application locally.*

---
*Developed for Educational Purposes Only.*
