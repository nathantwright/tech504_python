import os
import sys
import yaml

if len(sys.argv) > 1:
    # check directory exists
    if os.path.exists(sys.argv[1]):
        dir_contents = os.listdir(sys.argv[1])
        for f in dir_contents:
            if os.path.isfile(sys.argv[1] + "/" +
                              f):
                try:
                    file = open(sys.argv[1] + "/"
                                + f, "r")
                    yaml.safe_load(file)
                    file.close()
                    print(f"'{f}' is valid")
                except:
                    print(f"'{f}' is not valid")
    else:
        # alert user that directory specified does
        # not exist
        print("ERROR: Directory '" + sys.argv[1] +
              "' not found")
else:
    print("ERROR: No YAML directory was specified "
          "to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")