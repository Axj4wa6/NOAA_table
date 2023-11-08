
#Raw data from noaa chart
'''noaa = [
    [0.71, 40, 17, 27, 38, 50, 62, 76, 91, 107, 125, 145, 167, 193, 223, 260, 307, 371],
    [0.76, 45, 14, 23, 32, 42, 52, 63, 74, 87, 100, 115, 131, 148, 168, 190, 215, 232],
    [0.80, 50, 12, 20, 27, 36, 44, 53, 63, 73, 84, 95, 108, 121, 135, 151, 163,],
    [0.85, 55, 11, 17, 24, 31, 39, 46, 55, 63, 72, 82, 92, 102, 114, 125],
    [0.90, 60, 9, 15, 21, 28, 34, 41, 48, 56, 63, 71, 80, 89, 92],
    [1.00, 70, 7, 12, 17, 22, 28, 33, 39, 45, 51, 57, 60],
    [1.10, 80, 6, 10, 14, 19, 23, 28, 32, 37, 42, 47, 48],
    [1.19, 90, 59, 12, 16, 20, 24, 28, 32, 36, 39],
    [1.29, 100, 4, 7, 11, 14, 17, 21, 24, 28, 30],
    [1.39, 110, 4, 7, 11, 14, 17, 21, 24, 28, 30],
    [1.48, 120, 4, 6, 9, 12, 15, 18, 21, 25],
    [1.58, 130, 3, 6, 8, 11, 14, 16, 19, 20]
]

'''

'''
# test script for only 40 feet values (then flipped for ease of reading
_40 = {0.71: 'PPO2', 17: 'A', 27: 'B', 38: 'C', 50: 'D', 62: 'E', 76: 'F', 91: 'G', 107: 'H', 125: 'I', 145: 'J', 167: 'K', 193: 'L', 223: 'M', 260: 'N', 307: 'O', 371: 'Z'}
_40_flipped = {value: key for key, value in _40.items()}


#user input
depth=int(input("Enter Depth: "))

if depth== 40:
    print("PPO2: " + str(_40_flipped.get('PPO2')) + " ATA")'''
'''
# Raw data with depth column removed
noaa_without_second_column = [
    [0.71, 17, 27, 38, 50, 62, 76, 91, 107, 125, 145, 167, 193, 223, 260, 307, 371],
    [0.76, 14, 23, 32, 42, 52, 63, 74, 87, 100, 115, 131, 148, 168, 190, 215, 232],
    [0.80, 12, 20, 27, 36, 44, 53, 63, 73, 84, 95, 108, 121, 135, 151, 163],
    [0.85, 11, 17, 24, 31, 39, 46, 55, 63, 72, 82, 92, 102, 114, 125],
    [0.90, 9, 15, 21, 28, 34, 41, 48, 56, 63, 71, 80, 89, 92],
    [1.00, 7, 12, 17, 22, 28, 33, 39, 45, 51, 57, 60],
    [1.10, 6, 10, 14, 19, 23, 28, 32, 37, 42, 47, 48],
    [1.19, 59, 12, 16, 20, 24, 28, 32, 36, 39],
    [1.29, 4, 7, 11, 14, 17, 21, 24, 28, 30],
    [1.39, 4, 7, 11, 14, 17, 21, 24, 28, 30],
    [1.48, 4, 6, 9, 12, 15, 18, 21, 25],
    [1.58, 3, 6, 8, 11, 14, 16, 19, 20]
]

#convert to list of dictionaries
# Header values to insert into each dataset
headers = ["PPO2", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "Z"]

# Convert each dataset to a dictionary
noaa_with_headers = []

for dataset in noaa_without_second_column:
    dataset_dict = {}
    for i, value in enumerate(dataset):
        if i < len(headers):
            dataset_dict[headers[i]] = value
    noaa_with_headers.append(dataset_dict)

# Print the result
for dataset_dict in noaa_with_headers:
    print(dataset_dict)
'''

noaa_w_headers = [
    {'depth': 40, 'PPO2': 0.71, 'A': 17, 'B': 27, 'C': 38, 'D': 50, 'E': 62, 'F': 76, 'G': 91, 'H': 107, 'I': 125, 'J': 145, 'K': 167, 'L': 193, 'M': 223, 'N': 260, 'O': 307, 'Z': 371},
    {'depth': 45, 'PPO2': 0.76, 'A': 14, 'B': 23, 'C': 32, 'D': 42, 'E': 52, 'F': 63, 'G': 74, 'H': 87, 'I': 100, 'J': 115, 'K': 131, 'L': 148, 'M': 168, 'N': 190, 'O': 215, 'Z': 232},
    {'depth': 50, 'PPO2': 0.8, 'A': 12, 'B': 20, 'C': 27, 'D': 36, 'E': 44, 'F': 53, 'G': 63, 'H': 73, 'I': 84, 'J': 95, 'K': 108, 'L': 121, 'M': 135, 'N': 151, 'O': 163},
    {'depth': 55, 'PPO2': 0.85, 'A': 11, 'B': 17, 'C': 24, 'D': 31, 'E': 39, 'F': 46, 'G': 55, 'H': 63, 'I': 72, 'J': 82, 'K': 92, 'L': 102, 'M': 114, 'N': 125},
    {'depth': 60, 'PPO2': 0.9, 'A': 9, 'B': 15, 'C': 21, 'D': 28, 'E': 34, 'F': 41, 'G': 48, 'H': 56, 'I': 63, 'J': 71, 'K': 80, 'L': 89, 'M': 92},
    {'depth': 70, 'PPO2': 1.0, 'A': 7, 'B': 12, 'C': 17, 'D': 22, 'E': 28, 'F': 33, 'G': 39, 'H': 45, 'I': 51, 'J': 57, 'K': 60},
    {'depth': 80, 'PPO2': 1.1, 'A': 6, 'B': 10, 'C': 14, 'D': 19, 'E': 23, 'F': 28, 'G': 32, 'H': 37, 'I': 42, 'J': 47, 'K': 48},
    {'depth': 90, 'PPO2': 1.19, 'A': 59, 'B': 12, 'C': 16, 'D': 20, 'E': 24, 'F': 28, 'G': 32, 'H': 36, 'I': 39},
    {'depth': 100, 'PPO2': 1.29, 'A': 4, 'B': 7, 'C': 11, 'D': 14, 'E': 17, 'F': 21, 'G': 24, 'H': 28, 'I': 30},
    {'depth': 110, 'PPO2': 1.39, 'A': 4, 'B': 7, 'C': 11, 'D': 14, 'E': 17, 'F': 21, 'G': 24, 'H': 28, 'I': 30},
    {'depth': 120, 'PPO2': 1.48, 'A': 4, 'B': 6, 'C': 9, 'D': 12, 'E': 15, 'F': 18, 'G': 21, 'H': 25},
    {'depth': 130, 'PPO2': 1.58, 'A': 3, 'B': 6, 'C': 8, 'D': 11, 'E': 14, 'F': 16, 'G': 19, 'H': 20}
]

max_depth = int(input("Enter max depth in feet: "))
found_data = None

for data_set in noaa_w_headers:
    if data_set['depth'] == max_depth:
        found_data = data_set
        break

if found_data:
    print(f"PPO2 for depth {max_depth} feet: {found_data['PPO2']}")
else:
    print(f"No data found for depth {max_depth} feet.")

if found_data:
    last_header = list(found_data.keys())[-1]
    last_value = found_data[last_header]
    print(f"Last data for depth {max_depth} feet: {last_header}: {last_value}")
else:
    print(f"No data found for depth {max_depth} feet.")
