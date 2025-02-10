import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Use "matplotlib" or "plotly" as the plotting library
USE_PLOTLY = True  # Change to False to use Matplotlib

# File path
input_file = "signal.txt"

def plot_signal_matplotlib(row, row_index):
    """Plots a signal row using Matplotlib with zoom and pan support."""
    durations = list(map(int, row.strip().split(',')))
    signal, time = [], []
    current_time = 0

    for duration in durations:
        value = 1 if duration > 0 else 0
        signal.extend([value] * abs(duration))
        time.extend(range(current_time, current_time + abs(duration)))
        current_time += abs(duration)

    fig, ax = plt.subplots(figsize=(12, 4))

    ax.step(time, signal, where='post')
    ax.set_title(f"Signal Row {row_index} (Matplotlib Interactive)")
    ax.set_xlabel("Time (Arbitrary Units)")
    ax.set_ylabel("Signal")
    ax.set_ylim(-0.2, 1.2)

    plt.grid(True)  # Enable grid for better visibility
    plt.show()  # Interactive mode allows zoom & pan

def plot_signal_plotly(row, row_index):
    """Plots a signal row using Plotly for smoother zooming & panning."""
    durations = list(map(int, row.strip().split(',')))
    signal, time = [], []
    current_time = 0

    for duration in durations:
        value = 1 if duration > 0 else 0
        signal.extend([value] * abs(duration))
        time.extend(range(current_time, current_time + abs(duration)))
        current_time += abs(duration)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=signal, mode='lines', name=f"Row {row_index}"))

    fig.update_layout(
        title=f"Signal Row {row_index} (Plotly Interactive)",
        xaxis_title="Time (Arbitrary Units)",
        yaxis_title="Signal",
        yaxis=dict(range=[-0.2, 1.2]),
        dragmode="pan",  # Default mode is pan
    )

    fig.show()

# Read and plot each row
with open(input_file, "r") as file:
    for i, line in enumerate(file):
        if USE_PLOTLY:
            plot_signal_plotly(line, i)
        else:
            plot_signal_matplotlib(line, i)
