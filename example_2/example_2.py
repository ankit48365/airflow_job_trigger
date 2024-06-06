import os

# run the below command on your terminal (if linux distribution) and then : source ~/.bashrc
# echo 'export msg_local_variable="example2 - this message comes via local variable on system"' >> ~/.bashrc

message= os.environ['msg_local_variable']
# Print the value associated with the key 'message'
print(message)
# print('hello there, this is test')