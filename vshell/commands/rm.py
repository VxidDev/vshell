import os , argparse , shutil
from colorama import Style , Fore , init

init()

def rm():
    parser = argparse.ArgumentParser()

    parser.add_argument("path" , help="path of targeted file.")
    parser.add_argument("-r" , "--recursively" , action="store_true" , help="Delete recursively.")

    args = parser.parse_args()
    try:
        os.remove(args.path)
        print(Style.BRIGHT + Fore.WHITE + "rm: " + Fore.GREEN + "deleted successfully." + Style.RESET_ALL)
    except FileNotFoundError:
        print(Style.BRIGHT + Fore.WHITE + "rm: " + Fore.RED + "no such file or directory at given path!" + Style.RESET_ALL)
    except IsADirectoryError:
        if args.recursively:
            shutil.rmtree(args.path)
        else:
            print(Style.BRIGHT + Fore.WHITE + "rm: " + Fore.YELLOW + "the given path is a directory!" + Style.RESET_ALL)
            choice = input(Style.BRIGHT + Fore.WHITE + "rm: Do you want to continue? Y/N: " + Style.RESET_ALL).lower()
            while choice not in ["y" , "n"]:
                print(f"choice must be 'y' or 'n' not '{choice}'!")
                choice = input(Style.BRIGHT + Fore.WHITE + "rm: Do you want to continue? Y/N: " + Style.RESET_ALL).lower()

            if choice == "n":
                return 0
            else:
                shutil.rmtree(args.path)
                print(Style.BRIGHT + Fore.WHITE + "rm: " + Fore.GREEN + "deleted successfully." + Style.RESET_ALL)

rm()

