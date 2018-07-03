import os, shutil

path = os.getcwd() + '\\'
print("Current directory: " + path)

config_name = "config.par"
print("Config filename: " + config_name)

def parse_config(config):
    f = open(path+config, 'r')
    configs = {}
    line = f.readline()
    while(line):
        ls = line.split()
        if not isvalid(ls):
            print("Wrong arguments: " + line)
            line = f.readline()
            continue
        configs[ls[0]] = ls[1:]
        line = f.readline()
    return configs

def isvalid(ls):
    if len(ls) < 2:
        return False
    if (ls[1] == 'MOVE' or ls[1] == 'COPY'):
        if len(ls) < 3:
            return False
        if not os.path.isdir(ls[2]):
            print("No such directory: " + ls[2])
            return False
        return True
    if (ls[1] == 'REMOVE'):
        return True
    return False
        

def to_do(name, configs):
    ext = name.split('.')[-1]
    if ext in configs.keys():
        command = configs[ext][0]
        src = path + name
        if len(configs[ext])>1:
            dst = configs[ext][1]+ '\\' + name
            if command == 'MOVE':
                shutil.move(src, dst) 
            elif command == 'COPY':
                shutil.copy(src, dst)
        elif command == 'REMOVE':
            os.remove(src)

configs = parse_config(config_name)   
files = []
for f in os.listdir(path):
    if os.path.isfile(path+f) and '.' in f:
        files.append(f)

files_todo = input("Input filenames separated by spaces: ")

if (files_todo == '*.*'):
    for f in files:
        to_do(f, configs)
else:
    files_todo = files_todo.split()    
    for f in files_todo:
        if f in files:
            to_do(f, configs)
            continue
        filename = os.path.splitext(f)[0]
        ext = os.path.splitext(f)[1]
        if ext == '.*':
            for fd in files:
                if (filename == os.path.splitext(fd)[0]):
                    to_do(fd, configs)
            continue
        if filename == '*':
            for fd in files:
                if (ext == os.path.splitext(fd)[1]):
                    to_do(fd, configs)
        else:
            print ("file not found: " + f)
