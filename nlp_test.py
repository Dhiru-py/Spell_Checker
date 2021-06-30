a_dict = {}

a_file_train = open("/home/dhirendra/0_Desktop/Untitled Document", "r")
a_file_test = open("/home/dhirendra/0_Desktop/Untitled Document", "r")

#a_dict["train"] = a_file_train.read()
#a_dict["test"] = a_file_test.read()

sent_token = a_file_train.read().split("\n")
print (tuple(sent_token))
