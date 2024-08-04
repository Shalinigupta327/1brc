import time

def calculate_optimized(file_path: str):
    start_time = time.time()
    min_temperatures = {}
    max_temperatures = {}
    sum_temperatures = {}
    count_measurements = {}

    with open("measurements.txt", "r") as f:
        for line in f:
            station, temperature = line.split(";")
            temperature = float(temperature)

            if station not in min_temperatures:
                min_temperatures[station] = temperature
                max_temperatures[station] = temperature
                sum_temperatures[station] = temperature
                count_measurements[station] = 1
            else:
                min_temperatures[station] = min(min_temperatures[station], temperature)
                max_temperatures[station] = max(max_temperatures[station], temperature)
                sum_temperatures[station] += temperature
                count_measurements[station] += 1

    # Calculate averages
    average_temperatures = {}
    for station in min_temperatures:
        average_temperatures[station] = sum_temperatures[station] / count_measurements[station]

    # Print the results
    for station in sorted(min_temperatures):
        print(f"{station}: Min={min_temperatures[station]:.1f}, Max={max_temperatures[station]:.1f}, Avg={average_temperatures[station]:.1f}")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds")

# Example usage
calculate_optimized("measurements.txt")
