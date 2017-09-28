import figures
import turtle
import json
import sys

figure_dict = {'line': ['x coord','y coord','lenght','angle right'], 
               'circle': ['x coord','y coord','radius','vector (up/down)'], 
               'triangle': ['x coord','y coord','first lenght','second lenght','angle right','second angle right'], 
               'rectangle': ['x coord','y coord','first lenght','second lenght','angle right','vector (right/left)'] }

def create_file():
    filename = input('Enter filename: ')
    my_file = open('./saved_files/' + filename + '.json', 'w+')
    new_list = []
    json.dump([],my_file)


def open_file():
    while True:
        try:
            filename = input('Enter filename: ')
            file = open('./saved_files/' + filename + '.json', 'r+')
        except IOError as e:
            print('There`s no file! Try again!')
        else:
            return filename


def close(filename):
    filename.close()

def finish():
    return sys.exit()


def add_figure():
    param_row = []
    file_data = get_figure_list()
    file_list = file_data[0]
    filename = file_data[1]

    my_file = open('./saved_files/' + filename + '.json', 'w')
    while True:
        new_figure = input("Figures:\n\t- %s\nInput figure: " % '\n\t- '.join(map(str, figure_dict)))
        if new_figure in figure_dict:
            break
        else:
            print('Re enter figure!')
    func = figure_dict[new_figure]
    for i in func:
        param_row.append(input("Enter %s: " % i))
    file_list.append([new_figure, param_row])
    json.dump(file_list, my_file)
    close(my_file)


def edit_figure():
    param_row = []
    file_data = get_figure_list()
    file_list = file_data[0]
    filename = file_data[1]

    my_file = open('./saved_files/' + filename + '.json', 'w')
    while True:
        edit_figure = input("Enter figure index: ")
        if int(edit_figure) < len(file_list):
            break
        else:
            print('Re enter index!')
    row = file_list[int(edit_figure)]
    func = figure_dict[row[0]]
    for i in func:
        param_row.append(input("Enter %s: " % i))
    file_list[int(edit_figure)] = [row[0],param_row]
    json.dump(file_list, my_file)
    close(my_file)


def get_figure_list():
    filename = open_file()
    # while True:
    my_file = open('./saved_files/' + filename + '.json', 'r+')
    fig_list = json.load(my_file)
    print("Document has figures:\n%s"  % '\n'.join([str(i) 
        + ' - ' 
        + str(fig_list[i][0]) 
        + ' with parameters ' 
        + str(fig_list[i][1]) for i in range(len(fig_list))]))
    close(my_file)
    return [fig_list, filename]


def draw():
    filename = open_file()
    my_file = open('./saved_files/' + filename + '.json', 'r+')
    fig_list = json.load(my_file)
    anton = turtle.Turtle()
    turtle.Screen()
    for i in range(len(fig_list)):
        if fig_list[i][0] == 'line':
            figures.line(anton,*fig_list[i][1])
        if fig_list[i][0] == 'circle':
            figures.circle(anton,*fig_list[i][1])
        if fig_list[i][0] == 'triangle':
            figures.triangle(anton,*fig_list[i][1])
        if fig_list[i][0] == 'rectangle':
            figures.rectangle(anton,*fig_list[i][1])
