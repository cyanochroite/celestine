"""Implementation of configparser. May delete in the future."""
import configparser


INI = "celestine.ini"


def generate():
    """Create a configuration file."""
    # CREATE OBJECT
    config_file = configparser.ConfigParser()

    # ADD FTPSettings SECTION
    config_file.add_section("FTPSettings")
    # ADD SETTINGS TO FTPSettings SECTION
    config_file.set("FTPSettings", "ftpUrl", "demoftp.codeteddy.com")
    config_file.set("FTPSettings", "userName", "codeteddy")
    config_file.set("FTPSettings", "password", "my#supersecret#password")

    # ADD NEW SECTION AND SETTINGS
    config_file["Logger"] = {
        "LogFilePath": "<Path to log file>",
        "LogFileName": "<Name of log file>",
        "LogLevel": "Info"
    }

    # SAVE CONFIG FILE
    with open(r"configurations.ini", 'w') as configfileObj:
        config_file.write(configfileObj)
        configfileObj.flush()
        configfileObj.close()

    print("Config file 'configurations.ini' created")

    # PRINT FILE CONTENT
    read_file = open(INI, "r")
    content = read_file.read()
    print("Content of the config file are:\n")
    print(content)
    read_file.flush()
    read_file.close()


def update():
    """Add to the configuration file."""
    # CREATE OBJECT
    config_file = configparser.ConfigParser()

    # READ CONFIG FILE
    config_file.read(INI)

    # UPDATE A FIELD VALUE
    config_file["Logger"]["LogLevel"] = "Debug"

    # ADD A NEW FIELD UNDER A SECTION
    config_file["Logger"].update({"Format": "(message)"})

    # SAVE THE SETTINGS TO THE FILE
    with open("configurations.ini", "w") as file_object:
        config_file.write(file_object)

    # DISPLAY UPDATED SAVED SETTINGS
    print("Config file 'configurations.ini' is updated")
    print("Updated file settings are:\n")
    file = open("configurations.ini", "r")
    settings = file.read()
    print(settings)
