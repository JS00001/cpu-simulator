from ..utils.gantt import print_gantt_chart

def fcfs_algorithm(processes):
    # Sort processes by arrival time, so we can process them in order
    processes = sorted(processes, key=lambda p: p.arrival_time)
    start_times = []
    end_times = []
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for _, process in enumerate(processes):
        # If there's a gap between processes, move current_time to when the process arrives, the 
        # gannt chart fills empty spaces with IDLE
        current_time = max(current_time, process.arrival_time)
        
        # add the times to the gantt chart
        start_times.append(current_time)
        end_times.append(current_time + process.burst_time)
        
        # Calculate waiting and turnaround times, then update the total times
        waiting_time = current_time - process.arrival_time
        turnaround_time = waiting_time + process.burst_time
        
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        
        print(
          f"Pid:{process.id}, Arrived: {process.arrival_time}, Started: {current_time}, "
          f"Waiting: {waiting_time}, Turnaround: {turnaround_time}"
        )
        
        current_time += process.burst_time

    n = len(processes)
    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    # Check if we have any 'idle' moments to calculate CPU utilization
    total_cpu_time = sum(p.burst_time for p in processes)
    total_time = max(end_times) - min(p.arrival_time for p in processes)
    cpu_utilization = total_cpu_time / total_time if total_time > 0 else 0

    print(f"\nAvg wait time: {average_waiting_time:.2f}")
    print(f"Avg turnaround time: {average_turnaround_time:.2f}")
    print(f"CPU utilization: {cpu_utilization:.2f}")

    # Print the gantt chart
    print_gantt_chart(processes, start_times, end_times)
    
    return average_waiting_time, average_turnaround_time