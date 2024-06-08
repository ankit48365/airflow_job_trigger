
###########################################################################################
# Example 1
import yaml

# Load the somefile.yml file
with open('somefile.yml', 'r') as file:
    config = yaml.safe_load(file)

# Reading key called message from the YAML 
msg = config['message']
# Print the value associated with the key 'message'
print(msg)

###########################################################################################
# Example 1
import os

message= os.environ['msg_local_variable']
# Print the value associated with the key 'message'
print(message)