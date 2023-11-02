import subprocess
import os


def main():
    subprocess.run(["pymon", os.path.abspath("./src/cli_interface.py")])


if __name__ == "__main__":
    main()
