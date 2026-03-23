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
            row = {p.split('=')[0]: float(p.split('=')[1]) for p in line.split(',') if '=' in p}
            data.append(row)
    return pd.DataFrame(data)

st.title("⚓ Marine CPTu Analyzer")
file = st.file_uploader("Upload .cpt file", type=['cpt'])

if file:
    df = parse_cpt(file.getvalue().decode('utf-8', errors='ignore'))
    fig = make_subplots(rows=1, cols=3, shared_yaxes=True, 
                        subplot_titles=("qc (MPa)", "fs (kPa)", "u2 (kPa)"))
    
    fig.add_trace(go.Scatter(x=df['QC'], y=df['D'], name='qc'), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['FS'], y=df['D'], name='fs'), row=1, col=2)
    fig.add_trace(go.Scatter(x=df['U'], y=df['D'], name='u2'), row=1, col=3)
    
    fig.update_yaxes(autorange="reversed", title="Depth (m)")
    fig.update_layout(height=700, template="plotly_white")
    st.plotly_chart(fig, use_container_width=True)
