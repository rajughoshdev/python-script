import json
import os

'''Read text file to convert json'''
with open ("text.txt", "r") as t_file:
        read_t_file = json.load(t_file)
        print("text file read complete")

'''Check json file is exists if yes delete then delete it'''
if os.path.isfile("file.json"):
    os.remove("file.json")
    print("file.json is remove")
else: 
    print("File not avaiable")

'''Write json file from text file'''
with open ("file.json", "w") as j_file:
        json.dump(read_t_file, j_file)
        print("Json dump success")

'''Read Json file'''
with open ("file.json", "r") as j_file:
        read_j_file = json.load(j_file)

print(read_j_file)










