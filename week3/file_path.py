import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

# Get the full path of the current script
script_path = os.path.abspath(__file__)
print(script_path)

# to get the parent directory of the current script
parent_dir = os.path.dirname(script_dir)
print(parent_dir)