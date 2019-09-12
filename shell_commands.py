import os


def demo():
    # Python’s os.popen call gives a file-like interface, for reading the outputs of spawned shell commands
    # Tools such as os.popen and subprocess. Popen that support spawning shell commands and reading and writing to their standard streams
    F = os.popen('dir')         # this runs a dir directory listing on Windows, but any program that can be started with a command line can be launched this way
    for line in F.readlines():
        print(line.rstrip())

    os.system('systeminfo')     # os.system simply runs a shell command, but os.popen also connects to its streams

