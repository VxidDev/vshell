import subprocess , colorama , argparse
from pathlib import Path 

def python():
    parser = argparse.ArgumentParser()

    parser.add_argument("path" , help="Path of file.")
    
    args = parser.parse_args()

    try:
        if input is None:
            subprocess.Popen("python" , shell=True).wait()
        else:
            subprocess.Popen(f"python '{str(args.path)}'" , shell=True).wait()
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.BLUE + "pyt" + Fore.YELLOW + "hon" + Fore.WHITE + f": '{args.path}' " + Fore.RED + "not found!" + Style.RESET_ALL)

python()
