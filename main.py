import subprocess , signal , os , json , readline 
from colorama import Style , Fore , init
from pathlib import Path
from sys import exit

init() # initialize colorama

signal.signal(signal.SIGTSTP, signal.SIG_IGN) # make ctrl+Z not force-close vshell.

available_commands = ["echo" , "clear" , "exit" , "touch" , "mkdir" , "cd" , "ls" , "edit" , "py" , "rm" , "gen_cfg" , "run"]
installed_location = Path(__file__).resolve().parent

default_config = {
    "text_editor": "nano" # config, some new thing may come out soon!
}

def gen_config():
    with open(f"{installed_location}/config.json" , "w") as file:
        json.dump(default_config , file)
    print(Style.BRIGHT + Fore.GREEN + f"success: config at '{installed_location}/config.json'" + Style.RESET_ALL)

def get_config_data():
    try:
        with open(f"{installed_location}/config.json" , "r") as file:
            config = json.load(file)
    except FileNotFoundError:
        config = default_config
    except json.JSONDecodeError: # Maybe possible to optimize those 2 except's but 'or' doesnt work for me...
        config = default_config

    return config

config = get_config_data()

text_editor = config["text_editor"]

# Planning to put commands into separate files. (rm.py / py.py already done!)
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
    input = input.removeprefix("cd").strip()
    if "~" in input:
        input = Path(input).expanduser()
    try:
        os.chdir(input)
    except FileNotFoundError:
        print("no such file or directory!")
    return os.getcwd()

def ls(input , path):
    output_list = []
    if input is None:
        path = Path(path)
    else:
        path = Path(path) / input 
    for file in path.iterdir():
        if Path(file).is_dir():
            output_list.append(Style.BRIGHT + Fore.BLUE + file.name + Style.RESET_ALL)
        else:
            output_list.append(Style.BRIGHT + Fore.WHITE + file.name + Style.RESET_ALL)
    output = " ".join(output_list)

    print(output)

def edit(input , path):
    if input is None:
        subprocess.Popen([text_editor , Path(path)]).wait()
    else:
        subprocess.Popen([text_editor , Path(path) / input]).wait()

def python(input , path):
    try:
        module_location = installed_location / Path("commands") / Path("py.py")
        subprocess.Popen(f"python '{module_location}' '{path / input}'" , shell=True).wait()
    except FileNotFoundError as e:
        print(str(e))
        print(Style.BRIGHT + Fore.RED + "'py.py' not found!" + Style.RESET_ALL)
        

def rm(input , path):
    module_location = installed_location / Path("commands") / Path("rm.py")
    args = ["python" , str(module_location) , str(path / input)]
    if "-r" or "--recursively" in args:
        args.append("-r")
    print(args)
    try:
        subprocess.Popen(args).wait()
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "'rm.py' not found!" + Style.RESET_ALL)

def run(input):
    module_location = installed_location / "commands" / "run.py"
    try:
        subprocess.Popen(["python" , module_location , input]).wait()
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.RED + "'run.py' not found!" + Style.RESET_ALL)

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
    "rm": rm,
    "gen_cfg": gen_config,
    "run": run
}

path = os.getcwd() # get working path

def main():
    while True: # yeah, goodluck reading this spaghetti code. I cant do this myself
        try:
            user_input = input(Style.BRIGHT + Fore.BLACK + "v" + Fore.WHITE + f"shell @ {path} > " + Style.RESET_ALL)    
            if user_input.split()[0].strip() not in available_commands:            
                print(f"'{user_input}'" + Style.BRIGHT + Fore.RED + " not recognized as a command." + Style.RESET_ALL)
            else:
                if user_input.split()[0] in "run":
                    try:
                        commands["run"](user_input.removeprefix("run"))
                    except IndexError:
                        pass
                elif "echo" in user_input:
                    commands[user_input.split()[0]](user_input)
                elif user_input.split()[0].strip() in ["exit" , "clear"]:
                    commands[user_input]()
                elif user_input.split()[0] in "cd":
                    path = commands[user_input.split()[0]](user_input , path)
                elif user_input.split()[0] in "ls":
                    try:
                        commands[user_input.split()[0]](user_input.split()[1] , path)
                    except IndexError:
                        commands[user_input.strip()](None , path)
                elif user_input in "gen_cfg":
                    commands[user_input]()
                else:
                    commands[user_input.split()[0]](user_input.split()[1].strip() , path)
        except KeyboardInterrupt:
            pass
        except IndexError:
            pass
        except PermissionError:
            print("Permission Error: please run vshell with 'sudo'")

if __name__ == "__main__":
    main()
