import time

import matrix_operations
from matrix_operations import stringify
import os


def get_file_index():
    last_item = 0
    for i in range(100):
        try:
            with open(f"history/history_{i}.txt") as last_file:
                last_file.read()
                last_item = i + 1
        except FileNotFoundError:
            return last_item


class Recaller:
    previous_command = None
    previous_matrix = None

    def __init__(self):
        self.item = get_file_index()
        self.history_open()

    def history_open(self):
        with open(f"history/history_{self.item}.txt", mode="w") as history_file:
            history_file.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            history_file.write("\n")

    def history_append(self, command, matrix):
        with open(f"history/history_{self.item}.txt", mode="a") as history_file:
            history_file.write("\n")
            history_file.write(command)
            history_file.write("\n")
            history_file.write(stringify(matrix))
        self.previous_command = command
        self.previous_matrix = matrix

    def history_read(self):
        with open(f"history/history_{self.item}.txt") as history_file:
            lines = history_file.readlines()
            matrices_dicts = []
            key = ""
            matrix_string = ""
            for line in lines:
                if line[0] == "\n":
                    if key != "":
                        # matrix_dict = {key: matrix_operations.read_string(matrix_string)}
                        matrices_dicts.append({key: matrix_operations.read_string(matrix_string)})
                    key = ""
                    matrix_string = ""
                elif line.strip() in matrix_operations.operation_dict:
                    key = line.strip()
                elif line[0] == "|":
                    matrix_string += line
                # breakpoint()

            return matrices_dicts

    def undo(self, step):
        command_result_dict = {}
        if self.previous_command is not None and self.previous_matrix is not None:
            command_result_dict[self.previous_command] = self.previous_matrix
            return command_result_dict
        else:
            history = self.history_read()
            # self.previous_command
            return history[step]


def history_purge():
    for i in range(get_file_index()):
        try:
            os.remove(f"history/history_{i}.txt")
        except FileNotFoundError:
            pass
    print("history purged")
