# import time
# start_time = time.time()

# min_temperatures = {}
# max_temperatures = {}
# sum_temperatures = {}
# count_measurements = {}

# with open("measurements.txt", "r") as f:
#     for line in f:
#         station, temperature = line.split(";")
#         temperature = float(temperature)
#         # print(f"Station: {station}, Measurement: {temperature}")


#         if station not in min_temperatures:
#             min_temperatures[station] = temperature    
#             max_temperatures[station] = temperature
#             sum_temperatures[station] = temperature
#             count_measurements[station] = 1
#         else:
#             min_temperatures[station] = min(min_temperatures[station], temperature)
#             max_temperatures[station] = max(max_temperatures[station], temperature)
#             sum_temperatures[station] += temperature
#             count_measurements[station] += 1

# # print(min_temperatures)

# # Calculating averages
# average_temperatures = {}
# for station in min_temperatures:
#     average_temperatures[station] = sum_temperatures[station] / count_measurements[station]

# # Print the results
# for station in sorted(min_temperatures):
#     print(f"{station}: Min={min_temperatures[station]:.1f}, Max={max_temperatures[station]:.1f}, Avg={average_temperatures[station]:.1f}")

# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Time taken: {elapsed_time:.2f} seconds")














# # def calculate(measurements: str):
# #     stats: dict[str, dict[str, float]] = {}
# #     try: 
# #         with open("measurements.txt", "r") as f:
# #             for row in f:
# #                 city, temp = row.split(";")
# #                 if city in stats:
# #                     stats[city]["min"] = min(stats[city]["min"], float(temp))
# #                     stats[city]["max"] = max(stats[city]["max"], float(temp))
# #                     stats[city]["sum"] += float(temp)
# #                     stats[city]["count"] += 1
# #                 else:
# #                     stats[city] = {"min": float(temp), "max": float(temp), "sum": float(temp), "count": 1}

# #                 print(stats)
# #     except FileNotFoundError:
# #         print("Error: The file 'measurements.txt' does not exist.")
# #     except Exception as e:
# #         print(f"Error: {str(e)}")

# #     return stats


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

# # 

# import time
# import polars as pl

# def calculate_optimized_polars(file_path: str):
#     start_time = time.time()

#     # Read the data using polars
#     df = pl.read_csv(file_path, separator=';', has_header=False, new_columns=['station', 'temperature'])
    
#     # Group by station and calculate min, max, and mean
#     result = df.group_by('station').agg([
#         pl.col('temperature').min().alias('min_temperature'),
#         pl.col('temperature').max().alias('max_temperature'),
#         pl.col('temperature').mean().alias('average_temperature')
#     ])

#     # Sort results by station
#     result = result.sort('station')
    
#     # Print the results
#     for row in result.iter_rows(named=True):
#         print(f"{row['station']}: Min={row['min_temperature']:.1f}, Max={row['max_temperature']:.1f}, Avg={row['average_temperature']:.1f}")

#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Time taken: {elapsed_time:.2f} seconds")

# # Example usage
# calculate_optimized_polars("measurements.txt")



# # import time
# # from collections import defaultdict

# # def calculate_optimized(file_path: str):
# #     start_time = time.time()
    
# #     min_temperatures = defaultdict(lambda: float('inf'))
# #     max_temperatures = defaultdict(lambda: float('-inf'))
# #     sum_temperatures = defaultdict(float)
# #     count_measurements = defaultdict(int)

# #     with open(file_path, "r") as f:
# #         while True:
# #             lines = f.readlines(10**6)  # Read 10 million lines at a time
# #             if not lines:
# #                 break
# #             for line in lines:
# #                 station, temperature = line.strip().split(";")
# #                 temperature = float(temperature)

# #                 min_temperatures[station] = min(min_temperatures[station], temperature)
# #                 max_temperatures[station] = max(max_temperatures[station], temperature)
# #                 sum_temperatures[station] += temperature
# #                 count_measurements[station] += 1

# #     # Calculate averages
# #     average_temperatures = {station: sum_temperatures[station] / count_measurements[station] for station in min_temperatures}

# #     # Print the results
# #     for station in sorted(min_temperatures):
# #         print(f"{station}: Min={min_temperatures[station]:.1f}, Max={max_temperatures[station]:.1f}, Avg={average_temperatures[station]:.1f}")

# #     end_time = time.time()
# #     elapsed_time = end_time - start_time
# #     print(f"Time taken: {elapsed_time:.2f} seconds")

# # # Example usage
# # calculate_optimized("measurements.txt")
