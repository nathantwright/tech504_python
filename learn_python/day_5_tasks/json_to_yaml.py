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
        source_content = json.load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] +
              " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: json_to_yaml.py <source_file.json>"
          " <target_file.yaml>")

# 1. Convert the JSON to YAML - use yaml library
yaml_str = yaml.dump(source_content)

# 2. Save the YAML into a new file with the name
# for it received as an argument

# 2.2 Check the target file doesn't already exist
# WRITE YOUR CODE HERE
def part_2_2():
    if os.path.exists(sys.argv[2]):
        print(f"File with name '{sys.argv[2]}' "
              f"already exists!")
    else:
        # 2.3 If previous conditions not met, then save
        # YAML file
        # WRITE YOUR CODE HERE
        with open(sys.argv[2], "w") as yaml_file:
            yaml_file.write(yaml_str)

# 2.1 Check the target file name was specified as
# an argument, if not, output the YAML to the
# screen instead
if len(sys.argv) > 2:
    part_2_2()
else:
    print(yaml_str)

