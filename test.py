import subprocess
import os
from typing import List
import colorama
from colorama import Fore, Style

colorama.init()


def call_cmd(cmd: List):
    print(Fore.CYAN + "[CMD] " + " ".join(cmd) + Style.RESET_ALL)
    return subprocess.call(cmd)


def main():
    print("TESTING ALL PROJECT-EULER EXAMPLES.")
    print("If everything is fine, this code exits with exit code 0.")
    print("If not, you'll see shiny red text that shows what went wrong.")
    for filename in os.listdir("./project-euler"):
        if filename.endswith(".hpt"):
            filename = "./project-euler/" + filename
            print("Running " + filename)
            exitcode = call_cmd(["python", "haupt.py", filename, "-c", "-o", "-m"])
            print("Compiling " + filename + " exited with exit code " + str(exitcode))
            if exitcode != 0:
                print(Fore.RED + "COMPILATION FAILED: " + filename + Style.RESET_ALL)
                exit(1)
            exitcode = call_cmd(["output.exe"])
            print("Executing " + filename + " exited with exit code " + str(exitcode))
            if exitcode != 0:
                print(Fore.RED + "EXECUTION FAILED: " + filename + Style.RESET_ALL)
                exit(1)
            print("*" * 100)
    print(Fore.GREEN + "All Tests passed!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()