from collections import namedtuple

from .utils.plot import plot_data
from .algorithms.shortest_job_first import sjf_algorithm
from .algorithms.first_come_first_serve import fcfs_algorithm

def calculate():
    Process = namedtuple('Process', ['id', 'arrival_time', 'burst_time'])

    # Processes: (id, arrival_time, burst_time)
    processes = [
        Process(1, 0, 8),
        Process(2, 5, 5),
        Process(3, 3, 4),
        Process(4, 2, 7),
        Process(5, 1, 2),
        Process(6, 7, 5),
        Process(7, 2, 3),
        Process(8, 3, 6),
        Process(9, 5, 1),
        Process(10, 1, 2)
    ]

    # Get the results from the algorithms
    print("FCFS Algorithm:")
    fcfs_data = fcfs_algorithm(processes)
    print("\nSJF Algorithm:")
    sjf_data = sjf_algorithm(processes)

    # Plot the data
    plot_data(fcfs_data, sjf_data)



