import argparse , subprocess

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("command" , help="command to run.")

    args = parser.parse_args()
    
    command = args.command.split()
    try:
        subprocess.Popen(command).wait()
    except FileNotFoundError:
        print("command not found.")

if __name__ == "__main__":
    main()
