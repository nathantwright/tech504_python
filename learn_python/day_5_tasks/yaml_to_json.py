import json
import os
import sys
import yaml

source_content = {}
# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] +
              " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No YAML file was specified")
    print("Usage: yaml_to_json.py <source_file.yaml>"
          " <target_file.json>")

# 1. Convert the YAML to JSON - use json library
json_str = json.dumps(source_content, indent=2)

# 2. Save the JSON into a new file with the name
# for it received as an argument

# 2.2 Check the target file doesn't already exist
# WRITE YOUR CODE HERE
def part_2_2():
    if os.path.exists(sys.argv[2]):
        print(f"File with name '{sys.argv[2]}' "
              f"already exists!")
    else:
        # 2.3 If previous conditions not met, then save
        # JSON file
        # WRITE YOUR CODE HERE
        with open(sys.argv[2], "w") as json_file:
            json_file.write(json_str)

# 2.1 Check the target file name was specified as
# an argument, if not, output the JSON to the
# screen instead
if len(sys.argv) > 2:
    part_2_2()
else:
    print(json_str)

