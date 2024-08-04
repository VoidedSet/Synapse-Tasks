def calculate_average_waiting_time(arrival_times, time_required):
    current_time = 0
    total_waiting_time = 0
    num_customers = len(arrival_times)
    
    for i in range(num_customers):
        arrival_time = arrival_times[i]
        prepare_time = time_required[i]
    
        start_time = max(current_time, arrival_time)
        
    
        waiting_time = (start_time + prepare_time) - arrival_time
        total_waiting_time += waiting_time
        current_time = start_time + prepare_time
    
    average_waiting_time = total_waiting_time / num_customers
    
    return average_waiting_time

arrival_times = [5, 5, 10, 20]
time_required = [2, 4, 3, 1]

average_waiting_time = calculate_average_waiting_time(arrival_times, time_required)
print(f"Average waiting time: {average_waiting_time:.2f}")
