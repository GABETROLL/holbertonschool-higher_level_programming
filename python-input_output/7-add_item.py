#!/usr/bin/python3
"""
Exercise 7: Make a script that adds all
arguments to a Python list (except this script's name),
and then saves the list to a JSON file called "add_item.json",
in its JSON form.
"""
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

if __name__ == "__main__":
    from sys import argv
    # This import
    # does what this exercise's description
    # says: "adds all arguments to a Python list"
    # (I think???) But, the list is created.
    save_to_json_file(argv[1:] + load_from_json_file("add_item.json"),
                      "add_item.json")
