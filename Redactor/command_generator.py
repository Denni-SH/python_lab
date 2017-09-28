import json
import figure_work


cli_commands = {"create file": figure_work.create_file, 
                "redactor": {"show figure list": figure_work.get_figure_list,
                                   "add new figure": figure_work.add_figure,
                                   "edit figure": figure_work.edit_figure,
                                   "draw paint": figure_work.draw},
                "exit": figure_work.finish
                }


def find_command(commands_list):
    while isinstance(commands_list,dict):
        command = input("Available commands:\n\t- %s\nInput command: " % '\n\t- '.join(map(str, commands_list)))
        if command in commands_list: # проверяем есть ли команда в списке
            commands_list = commands_list[command]
        else:
            print("Re enter correct command!")
    return commands_list


def get_command():
    while True:
        command = find_command(cli_commands)
        command()
        yield command
