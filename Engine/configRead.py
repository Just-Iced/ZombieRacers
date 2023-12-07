import configparser


def getConfig(path, section, configuration):
    config = configparser.ConfigParser()
    config.read(path)
    return config[section][configuration]


def setConfig(path, section, configuration, value):
    config = configparser.ConfigParser()
    config.read(path)
    config[section] = {configuration: value}
