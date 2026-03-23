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
            row = {p.split('=')[0].strip(): float(p.split('=')[1].strip()) for p in line.split(',') if '=' in p}
            data.append(row)
    
    df = pd.DataFrame(data)
    if not df.empty:
        # 1. Friction Ratio (%) - Note: FS is in kPa, QC is in MPa (multiply by 1000)
        df['Rf'] = (df['FS'] / (df['QC'] * 1000)) * 100
        
        # 2. Pore Pressure Ratio (Bq) - Simplified estimate
        # Assumes hydrostatic u0 = Depth * 9.81 for marine environments
        u0 = df['D'] * 9.81
        df['Bq'] = (df['U'] - u0) / (df['QC'] * 1000 - u0)
        
        # Clean up infinite values from division by zero
        df.replace([float('inf'), float('-inf')], 0, inplace=True)
    return df

st.set_page_config(layout="wide")
st.title("⚓ Advanced Marine CPTu Analyzer")

file = st.file_uploader("Upload .cpt file", type=['cpt'])

if file:
    df = parse_cpt(file.getvalue().decode('utf-8', errors='ignore'))
    
    # Create 5 subplots for full geotechnical profile
    fig = make_subplots(
        rows=1, cols=5, 
        shared_yaxes=True, 
        subplot_titles=("qc (MPa)", "fs (kPa)", "u2 (kPa)", "Rf (%)", "Bq"),
        horizontal_spacing=0.03
    )
    
    # Primary Channels
    fig.add_trace(go.Scatter(x=df['QC'], y=df['D'], name='qc', line=dict(color='blue')), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['FS'], y=df['D'], name='fs', line=dict(color='orange')), row=1, col=2)
    fig.add_trace(go.Scatter(x=df['U'], y=df['D'], name='u2', line=dict(color='green')), row=1, col=3)
    
    # Derived Parameters
    fig.add_trace(go.Scatter(x=df['Rf'], y=df['D'], name='Rf', line=dict(color='red')), row=1, col=4)
    fig.add_trace(go.Scatter(x=df['Bq'], y=df['D'], name='Bq', line=dict(color='purple')), row=1, col=5)
    
    fig.update_yaxes(autorange="reversed", title="Depth (m)")
    fig.update_layout(height=800, template="plotly_white", showlegend=False)
    
    # Set axis limits for Rf and Bq to keep plots readable
    fig.update_xaxes(range=[0, 10], row=1, col=4) # Rf usually 0-10%
    fig.update_xaxes(range=[-0.2, 1.2], row=1, col=5) # Bq usually 0-1.0
    
    st.plotly_chart(fig, use_container_width=True)
    st.write("### Processed Data Table", df.head(20))
