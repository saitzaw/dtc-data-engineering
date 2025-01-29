import pandas as pd 
import sys 
import subprocess

arg = sys.argv[1]

print(f"job finished with arg: {arg}")
pip_version = subprocess.check_output(["pip", "--version"]).decode("utf-8")
print(f"pip version: {pip_version}")
