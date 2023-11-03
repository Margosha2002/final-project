import subprocess
import os


def main():
    subprocess.run(["python3", os.path.abspath("./src/cli_interface.py")])


if __name__ == "__main__":
    main()
