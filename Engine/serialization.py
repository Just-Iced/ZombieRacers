import os, pickle


def DoesSaveDataExist(name):
    return os.path.isfile(f"{os.getcwd()}/Game/SaveData/{name}.pickle")

def LoadSaveData(name):
    return pickle.load(open(f"{os.getcwd()}/Game/SaveData/{name}.pickle", "rb"))

def SaveData(name, attributes = {}):
    with open(f"{os.getcwd()}/Game/SaveData/{name}.pickle", "bw") as f:
        pickle.dump(attributes, f)