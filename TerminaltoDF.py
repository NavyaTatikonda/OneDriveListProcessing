import sys
import subprocess
from subprocess import PIPE, CalledProcessError, check_call, Popen
import pandas as pd
from io import StringIO

cmd = ['testdf']
a = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
b = StringIO(a.communicate()[0].decode('utf-8'))

df = pd.read_csv(b, sep=",")
print(df)
