import time
import os

import matrix_math


def get_file_index(matrix_name):
    last_item = 0
    for i in range(100):
        try:
            with open(f"history/history_{i}_{matrix_name}.txt") as last_file:
                last_file.read()
                last_item = i + 1
        except FileNotFoundError:
            return last_item


class Recaller:

    def __init__(self, initial_matrix, name):
        self.name = name
        self.item = get_file_index(name)
        self.history_open()
        self.history_append("start", initial_matrix)

    def history_open(self):
        with open(f"history/history_{self.item}_{self.name}.txt", mode="w") as history_file:
            history_file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            history_file.write("\n")

    def history_append(self, command, matrix):
        with open(f"history/history_{self.item}_{self.name}.txt", mode="a") as history_file:
            history_file.write("\n")
            history_file.write(command)
            history_file.write("\n")
            history_file.write(matrix_math.stringify(matrix))

    def history_read(self):
        with open(f"history/history_{self.item}_{self.name}.txt") as history_file:
            lines = history_file.readlines()
            matrices_dicts = []
            key = ""
            matrix_string = ""
            for line in lines:
                if line[0] == "\n":
                    if key != "":
                        matrices_dicts.append({"command": key, "matrix": matrix_math.read_string(matrix_string),})
                    key = ""
                    matrix_string = ""
                elif line.strip() in matrix_math.operation_dict or line.strip() == "start":
                    key = line.strip()
                elif line[0] == "|":
                    matrix_string += line

            return matrices_dicts

    def undo(self, step):
        history = self.history_read()
        # try:
        return history[-step]
        # except IndexError:
        #     print("end of history")
        #     return history[-1]


def history_purge():
    for i in range(100):  # get_file_index()
        try:
            os.remove(f"history/history_{i}.txt")
        except FileNotFoundError:
            break
    print("history purged")
