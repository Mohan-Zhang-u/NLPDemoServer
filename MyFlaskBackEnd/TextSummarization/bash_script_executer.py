import subprocess
import sys

def main(args):
    runstring = "./run.sh " + args[0]
    print(runstring)
    subprocess.call(runstring, shell=True)

if __name__ == "__main__":
    main(sys.argv[1:])