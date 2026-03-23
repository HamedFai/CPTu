<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <title>CPTu Marine Analyzer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.31.0/build/stlite.css" />
  </head>
  <body>
    <div id="root"></div>
    <script src="https://cdn.jsdelivr.net/npm/@stlite/mountable@0.31.0/build/stlite.js"></script>
    <script>
      stlite.mount({
        requirements: ["pandas", "plotly"],
        entrypoint: "app.py",
        files: {
          "app.py": `
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def parse_cpt(content):
    data = []
    start = False
    for line in content.splitlines():
        if line.startswith('#'):
            start = True
            continue
        if start and '=' in line:
            # Parsing the Key=Value structure found in your marine CPT files
            row = {p.split('=')[0].strip(): float(p.split('=')[1].strip()) 
                   for p in line.split(',') if '=' in p}
            if row:
                data.append(row)
    
    df = pd.DataFrame(data)
    if not df.empty:
        # 1. Friction Ratio (%)
        # QC is typically in MPa, FS is in kPa. 
        # Rf = (fs / qc) * 100
        df['Rf'] = (df['FS'] / (df['QC'] * 1000)) * 100
        
        # 2. Pore Pressure Ratio (Bq)
        # Assuming hydrostatic pressure u0 = Depth * 9.81 (standard for marine)
        u0 = df['D'] * 9.81
        df['Bq'] = (df['U'] - u0) / (df['QC'] * 1000 - u0)
        
        # Cleaning numerical artifacts
        df.replace([float('inf'), float('-inf')], 0, inplace=True)
        df.fillna(0, inplace=True)
    return df

st.set_page_config(page_title="CPTu Marine Analyzer", layout="wide")

st.title("⚓ Marine Geotechnical CPTu Analyzer")
st.markdown("Upload your **.cpt** file to generate profiles for tip resistance, sleeve friction, pore pressure, and derived ratios.")

uploaded_file = st.file_uploader("Upload CPT file", type=['cpt', 'txt'])

if uploaded_file:
    content = uploaded_file.getvalue().decode('utf-8', errors='ignore')
    df = parse_cpt(content)
    
    if not df.empty:
        # Create a 5-column plot layout
        fig = make_subplots(
            rows=1, cols=5, 
            shared_yaxes=True,
            subplot_titles=("qc (MPa)", "fs (kPa)", "u2 (kPa)", "Rf (%)", "Bq"),
            horizontal_spacing=0.03
        )

        # Plotting the 5 parameters
        fig.add_trace(go.Scatter(x=df['QC'], y=df['D'], name='qc', line=dict(color='#1f77b4')), row=1, col=1)
        fig.add_trace(go.Scatter(x=df['FS'], y=df['D'], name='fs', line=dict(color='#ff7f0e')), row=1, col=2)
        fig.add_trace(go.Scatter(x=df['U'], y=df['D'], name='u2', line=dict(color='#2ca02c')), row=1, col=3)
        fig.add_trace(go.Scatter(x=df['Rf'], y=df['D'], name='Rf', line=dict(color='#d62728')), row=1, col=4)
        fig.add_trace(go.Scatter(x=df['Bq'], y=df['D'], name='Bq', line=dict(color='#9467bd')), row=1, col=5)

        # Global Formatting
        fig.update_yaxes(autorange="reversed", title_text="Depth (m)")
        fig.update_layout(height=850, template="plotly_white", showlegend=False)
        
        # Setting practical limits for ratios
        fig.update_xaxes(range=[0, 8], row=1, col=4)   # Rf focus on 0-8%
        fig.update_xaxes(range=[-0.2, 1.2], row=1, col=5) # Bq focus on 0-1.0
        
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("View Calculated Data Table"):
            st.dataframe(df)
    else:
        st.error("No data found. Ensure the file contains a '#' section with D, QC, FS, and U values.")
`
        },
      }, document.getElementById("root"));
    </script>
  </body>
</html>
