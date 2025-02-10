import matplotlib.pyplot as plt
import numpy as np

# File paths
input_file = "signal.txt"
output_file = "cropped_signal.txt"
cropped_signals = []

# Function to crop and save selections
def onselect(xmin, xmax, row_index, time, signal, durations):
    start_idx = np.searchsorted(time, xmin)
    end_idx = np.searchsorted(time, xmax)
    cropped_time = time[start_idx:end_idx]
    cropped_signal = signal[start_idx:end_idx]

    cropped_durations = []
    last_value = cropped_signal[0]
    duration_count = 0

    for val in cropped_signal:
        if val == last_value:
            duration_count += 1
        else:
            cropped_durations.append(duration_count if last_value == 1 else -duration_count)
            last_value = val
            duration_count = 1

    cropped_durations.append(duration_count if last_value == 1 else -duration_count)
    cropped_signals.append(",".join(map(str, cropped_durations)))
    print(f"Row {row_index} cropped and saved.")

# Function to process and plot a single row
def plot_signal(row, row_index):
    durations = list(map(int, row.strip().split(',')))
    signal, time = [], []
    current_time = 0

    for duration in durations:
        value = 1 if duration > 0 else 0
        signal.extend([value] * abs(duration))
        time.extend(range(current_time, current_time + abs(duration)))
        current_time += abs(duration)

    fig, ax = plt.subplots(figsize=(12, 4))

    # Cross-platform window maximization
    mng = plt.get_current_fig_manager()
    try:
        mng.window.state('zoomed')
    except AttributeError:
        try:
            mng.window.showMaximized()
        except AttributeError:
            try:
                mng.full_screen_toggle()
            except AttributeError:
                print("Warning: Could not maximize window automatically.")

    ax.step(time, signal, where='post')
    ax.set_title(f"Signal Row {row_index}")
    ax.set_xlabel("Time (Arbitrary Units)")
    ax.set_ylabel("Signal")
    ax.set_ylim(-0.2, 1.2)

    def on_click(event):
        if event.button == 1:
            if not hasattr(on_click, "start_time"):
                on_click.start_time = event.xdata
                print(f"Start selected: {on_click.start_time}")
            else:
                end_time = event.xdata
                print(f"End selected: {end_time}")
                onselect(on_click.start_time, end_time, row_index, time, signal, durations)
                plt.close(fig)

    fig.canvas.mpl_connect("button_press_event", on_click)
    plt.show()

# Read file and process each row
with open(input_file, "r") as file:
    for i, line in enumerate(file):
        plot_signal(line, i)

# Save cropped signals
with open(output_file, "w") as out_file:
    for cropped_row in cropped_signals:
        out_file.write(cropped_row + "\n")

print(f"Cropped signals saved to {output_file}")

# Function to plot the final cropped signals
def plot_final_cropped_signals():
    print("\nPlotting Final Cropped Signals...\n")

    with open(output_file, "r") as file:
        for i, line in enumerate(file):
            durations = list(map(int, line.strip().split(',')))
            signal, time = [], []
            current_time = 0

            for duration in durations:
                value = 1 if duration > 0 else 0
                signal.extend([value] * abs(duration))
                time.extend(range(current_time, current_time + abs(duration)))
                current_time += abs(duration)

            plt.figure(figsize=(10, 2))
            plt.step(time, signal, where='post')
            plt.title(f"Cropped Signal Row {i}")
            plt.xlabel("Time (Arbitrary Units)")
            plt.ylabel("Signal")
            plt.ylim(-0.2, 1.2)
            plt.show()

# Plot the cropped signals
plot_final_cropped_signals()
