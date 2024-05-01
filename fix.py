import os

'''
A file for dummies who annotate two sets of data with different
index->class mappings
'''



mapping = {
    0: 2,  # 'd'
    1: 3,  # 'df'
    2: 4,  # 'f'
    3: 5,  # 'uf'
    4: 6,  # 'u'
    5: 7,  # 'ub'
    6: 0,  # 'b'
    7: 1,  # 'db'
    8: 8,  # '1'
    9: 9,  # '2'
    10: 10, # '3'
    11: 11, # '4'
    12: 12, # '1+2'
    13: 13, # '3+4'
    14: 14  # '2+3'
}

def map_numbers_in_file(file_path, mapping):
    # Read all lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Create a new list for modified lines
    modified_lines = []

    # Process each line in the original file
    for line in lines:
        # Extract the first part of the line which is expected to be the number
        parts = line.split(' ', 1)  # Splitting on the first space
        if parts and parts[0].isdigit():
            number = int(parts[0])
            if number in mapping:
                # Replace the number with its mapped value
                new_line = line.replace(str(number), str(mapping[number]), 1)
                modified_lines.append(new_line)
            else:
                # If the number is not in the mapping, keep the line unchanged
                modified_lines.append(line)
        else:
            # If the line does not start with a number, keep it unchanged
            modified_lines.append(line)

    # Write all modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

# Define the mapping based on the previous description

# Call the function with the path to your text file
# for i in range(176, 250):
#     file_path = f'./frames/input/val/labels/cropped_input_frame{i}.txt'
#     if(os.path.isfile(file_path)):
#         print(f"Running {i}")
#         map_numbers_in_file(file_path, mapping)


# file_path = f'./frames/input/train/labels/cropped_input_frame.txt'
# if(os.path.isfile(file_path)):
#     print(f"Running")
#     map_numbers_in_file(file_path, mapping)