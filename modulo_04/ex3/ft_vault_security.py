#!/usr/bin/env python3
def secure_archive(filename: str, action: str, content=""):
    try:
        if action == "r":
            with open(filename, 'r') as file:
                data = file.read()
            return (True, data)
        elif action == "w":
            with open(filename, 'w') as file:
                file.write(content)
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action specified")
    except Exception as ex:
        return (False, str(ex))
