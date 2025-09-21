import subprocess , signal
from colorama import Style , Fore , init
from pathlib import Path
from sys import exit
import os

init()

signal.signal(signal.SIGTSTP, signal.SIG_IGN)
available_commands = ["echo" , "clear" , "exit" , "touch" , "mkdir" , "cd" , "ls" , "edit" , "py" , "rm"]

def echo(input): 
    input = input.removeprefix("echo").strip()
    print(input)

def clear():
    subprocess.run("clear")

def exit_shell():
    exit()

def touch(input , path):
    target = path / input
    target.touch()

def mkdir(input , path):
    target = path / input 
    target.mkdir()

def cd(input , path):
    path = path / input.removeprefix("cd").strip()
    return path

def ls(input , path):
    if input is None:
        output = subprocess.run(f"ls {path}" , shell=True , capture_output=True , text=True).stdout.strip()
    else:
        output = subprocess.run(f"ls {input}" , shell=True , capture_output=True , text=True).stdout.strip()
    
    print(output)

def edit(input , path):
    if input is None:
        subprocess.Popen(f"nano {path}" , shell=True).wait()
    else:
        subprocess.Popen(f"nano {path / input}" , shell=True).wait()

def python(input , path):
    try:
        if input is None:
            subprocess.Popen("python" , shell=True).wait()
        else:
            subprocess.Popen(f"python {str(path / input)}" , shell=True).wait()
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.WHITE + f"'{path / input}'" + Fore.RED + " not found!" + Style.RESET_ALL)

def rm(input , path):
    try:
        os.remove(f"{path / input}")
    except FileNotFoundError:
        pass

commands = {
    "echo": echo,
    "clear": clear,
    "exit": exit_shell,
    "touch": touch,
    "mkdir": mkdir,
    "cd": cd,
    "ls": ls,
    "edit": edit,
    "py": python,
    "rm": rm
}

path = Path("~").expanduser()
while True:
    try:
        user_input = input(Style.BRIGHT + Fore.BLACK + "v" + Fore.WHITE + f"shell @ {path} > " + Style.RESET_ALL)    
        if user_input.split()[0].strip() not in available_commands:            
            print(f"'{user_input}'" + Style.BRIGHT + Fore.RED + " not recognized as a command." + Style.RESET_ALL)
        else:
            if "echo" in user_input:
                commands[user_input.split()[0]](user_input)
            elif user_input.split()[0].strip() in ["exit" , "clear"]:
                commands[user_input]()
            elif user_input.split()[0] in "cd":
                path = commands[user_input.split()[0]](user_input , path)
            elif user_input.split()[0] in "ls":
                try:
                    commands[user_input.split()[0]](user_input.split()[1].strip() , path)
                except IndexError:
                    commands[user_input.strip()](None , path)
            else:
                commands[user_input.split()[0]](user_input.split()[1].strip() , path)
    except KeyboardInterrupt:
        pass
    except IndexError:
        pass
