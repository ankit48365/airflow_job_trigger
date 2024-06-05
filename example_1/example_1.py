import yaml

# Load the somefile.yml file
with open('somefile.yml', 'r') as file:
    config = yaml.safe_load(file)

# Reading key called message from the YAML 
msg = config['message']

# Print the value associated with the key 'message'
print(msg)


# try:
#     # Load the somefile.yml file
#     with open('somefile.yml', 'r') as file:
#         config = yaml.safe_load(file)
#     # Check if 'config' is not None and 'greeting' key exists
#     if config is not None and 'message' in config:
#         msg = config['message']
#         print(msg)
#     else:
#         print("The 'message' key does not exist or the file is empty.")
# except FileNotFoundError:
#     print("The file 'somefile.yml' was not found.")
# except yaml.YAMLError as exc:
#     print(f"An error occurred while parsing the YAML file: {exc}")