import json

def f_open():
    my_file = open('./saved_files/' + 
        input('Enter filename:') + 
        '.json', 'a+')
    return my_file


def add_info(new_dict, my_file):
    json.dump(new_dict, my_file)


new_dict = {"1":"odin"}
add_info(new_dict,f_open())


# {"Create": {'func': you_function, 'child': {"Show figure list": {},
#                            "Add new figure": {"Line": {'param1': '',
#                                                        'param2': ''},
#                                               "Triangle": {'param1}