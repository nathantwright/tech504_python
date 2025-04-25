import json

with open("servers.json", "r") as file:
    # Reads the JSON file to a JSON string
    json_str = file.read()
    # Converts the JSON string to a dictionary
    servers = json.loads(json_str)

    print(type(servers), servers)
    print(servers["server1"])
    print(servers["server2"])
    for key in servers:
        print(f"\nKey and Value: '{key}' = "
              f"'{servers[key]}'" )
        for record_key in servers[key]:
            print(f"Record key and sub value: "
                  f"'{record_key}' = "
                  f"'{servers[key][record_key]}'")

#quit()

with open("servers.json", "r") as file:
    # Reads the JSON file to a dictionary
    servers = json.load(file)

    print(type(servers), servers)
    print(servers["server1"])
    print(servers["server2"])
    for key in servers.keys():
        print(f"\nKey and Value: '{key}' = "
              f"'{servers[key]}'" )
        for record_key in servers[key].keys():
            print(f"Record key and sub value: "
                  f"'{record_key}' = "
                  f"'{servers[key][record_key]}'")