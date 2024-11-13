from ..utils.gantt import print_gantt_chart

def sjf_algorithm(processes):
    n = len(processes)
    # Sort the processes by their arrival time
    processes = sorted(processes, key=lambda p: p.arrival_time)

    current_time = 0
    completed = 0 # The number of completed processes
    is_completed = [False] * n # A boolean array to store the completion status of processes
    start_times = [0] * n # A list to store the start time of each process
    end_times = [0] * n # A list to store the end time of each process

    total_waiting_time = 0
    total_turnaround_time = 0

    # While all processes are not completed
    while completed != n:
        min_burst = float('inf')
        min_index = -1

        # Go through all the processes and select the one with the shortest burst time that has arrived
        for i, process in enumerate(processes):
            if process.arrival_time <= current_time and not is_completed[i]:
                if process.burst_time < min_burst:
                    min_burst = process.burst_time
                    min_index = i

        # If no process is available to run, go to the next arrival time
        if min_index == -1:
            next_arrival = float('inf')

            # Get the next item that will arrive, and then skip to that time
            for i in range(n):
                if not is_completed[i] and processes[i].arrival_time < next_arrival:
                    next_arrival = processes[i].arrival_time
            current_time = next_arrival
            continue

        # Update the start and end times of the selected process
        start_times[min_index] = current_time
        end_times[min_index] = current_time + processes[min_index].burst_time
        
        # Calculate the waiting time and turnaround time of the selected process
        waiting_time = start_times[min_index] - processes[min_index].arrival_time
        turnaround_time = waiting_time + processes[min_index].burst_time
        
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        
        print(f"Pid: {processes[min_index].id}, Arrived: {processes[min_index].arrival_time}, "
              f"Started: {start_times[min_index]}, Waiting: {waiting_time}, "
              f"Turnaround: {turnaround_time}")

        # Update the current time and mark the process as completed
        current_time += processes[min_index].burst_time
        is_completed[min_index] = True
        completed += 1

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Check if we have any 'idle' moments to calculate CPU utilization
    total_cpu_time = sum(p.burst_time for p in processes)
    total_time = max(end_times) - min(p.arrival_time for p in processes)
    cpu_utilization = total_cpu_time / total_time if total_time > 0 else 0

    print(f"\nAverage waiting time: {average_waiting_time:.2f}")
    print(f"Average turnaround time: {average_turnaround_time:.2f}")
    print(f"CPU Utilization: {cpu_utilization:.2f}")

    print_gantt_chart(processes, start_times, end_times)
    
    return average_waiting_time, average_turnaround_time