import os, pickle


def DoesSaveDataExist(name):
    return os.path.isfile(os.getcwd()+"/Game/SaveData/"+name+".pickle")

def LoadSaveData(name):
    return pickle.load(open(os.getcwd()+"/Game/SaveData/"+name+".pickle", "rb"))

def SaveData(name, attributes = {}):
    with open(os.getcwd()+"/Game/SaveData/"+name+".pickle", "bw") as f:
        pickle.dump(attributes, f)