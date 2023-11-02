import subprocess
import os


def main():
    subprocess.run(["pymon", os.path.abspath("./src/api_interface.py")])


if __name__ == "__main__":
    main()
