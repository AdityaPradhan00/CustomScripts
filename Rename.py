import os

p = input("Enter the path : ")
path = os.chdir(p)
e = input("Enter the extension : ")
i = 1
pre = input("Enter the prefix 'Leave it blank in case you don't want a prefix' : ")
if pre == '':
    for file in os.listdir(path):
        new_file_name = "{}.{}".format(i, e)
        os.rename(file, new_file_name)
        i = i + 1
else:
    for file in os.listdir(path):
        new_file_name = "{} {}.{}".format(pre, i, e)
        os.rename(file, new_file_name)
        i = i + 1
