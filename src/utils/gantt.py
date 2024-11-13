def print_gantt_chart(processes, start_times, end_times):
    print("\nGantt Chart:")
        
    max_time = max(end_times)
    timeline = ['IDLE'] * max_time
    
    for i, process in enumerate(processes):
        for t in range(start_times[i], end_times[i]):
            timeline[t] = f'P{process.id}'
    
    print(' '.join(timeline))