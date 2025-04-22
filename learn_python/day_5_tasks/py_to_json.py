# import json
import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}
print(type(servers_dict), "\n", servers_dict, "\n")

# create a JSON string of the python dictionary
json_string = json.dumps(servers_dict, indent=2)
print(type(json_string), "\n", json_string, "\n")

# create a JSON file of the python dictionary
json_file = open("servers.json", "w")
json_file.write(json_string)
json_file.close()

json_file = open("servers.json", "r")
print(json_file.read())
json_file.close()