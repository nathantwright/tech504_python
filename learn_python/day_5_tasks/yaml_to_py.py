import yaml

with open("servers.yaml", "r") as file:
    # Converts the YAML file to a dictionary
    servers = yaml.safe_load(file)

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