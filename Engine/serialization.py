import os, pickle


def DoesSaveDataExist(name):
    return os.path.isfile(os.getcwd()+"/Game/SaveData/"+name)

def LoadSaveData(name):
    return pickle.load(open(os.getcwd()+"/Game/SaveData/"+name, "rb"))

def SaveData(name, attributes = {}):
    with open(os.getcwd()+"/Game/SaveData/"+name, "bw") as f:
        pickle.dump(attributes, f)