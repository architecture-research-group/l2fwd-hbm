import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_metric_from_csv(csv_path, memory_type, socket_choice, metric_choice):
    df = pd.read_csv(csv_path, header=[0, 1])
    df.columns = pd.MultiIndex.from_tuples([(i.strip(), j.strip()) for i, j in df.columns])
    socket = f"SKT{socket_choice}"
    mem_prefix = 'HBM' if memory_type == 'h' else 'Mem'
    # Special handling for HBM Write metric due to the space in the CSV header
    hbm_write_metric = ' HBM Write (MB/s)' if memory_type == 'h' else 'Mem Write (MB/s)'
    
    metric_mapping = {
        'r': f'{mem_prefix} Read (MB/s)',
        'w': hbm_write_metric,
        't': f'{mem_prefix} (MB/s)',
        'rw': (f'{mem_prefix} Read (MB/s)', hbm_write_metric)
    }
    
    if metric_choice not in metric_mapping:
        raise ValueError("Invalid metric choice. Use 'r', 'w', 't', or 'rw'.")
    
    metrics_to_plot = metric_mapping[metric_choice]
    if not isinstance(metrics_to_plot, tuple):
        metrics_to_plot = (metrics_to_plot,)

    time_axis = range(1, len(df) + 1)

    plt.figure(figsize=(12, 6))
    for metric in metrics_to_plot:
        data_to_plot = df[(socket, metric.strip())]
        plt.plot(time_axis, data_to_plot, label=metric.strip(), marker='o')
    
    plt.title(f"{' and '.join(metrics_to_plot)} for {socket} over Time")
    plt.xlabel('Entry Number')
    plt.ylabel('Bandwidth (MB/s)')
    plt.legend()
    plt.grid(True)
    plt.savefig("bandwidth.png")
    plt.show()

# Example command-line usage: python plot.py h 0 rw
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python plot.py <memory_type> <socket_choice> <metric_choice> e.g 'python plot.py h 0 rw' for HBM Read and Write")
        sys.exit(1)

    memory_type = sys.argv[1]  # Should be "h" for HBM or "m" for Mem
    socket_choice = sys.argv[2]  # Should be "0" (For socket 0 and HBM) or "1" (For socket 1) 
    metric_choice = sys.argv[3]  # Should be "r", "w", "t", or "rw" i.e Read and write on same graph.

    csv_file_path = 'pcm.csv'
    plot_metric_from_csv(csv_file_path, memory_type, socket_choice, metric_choice)
