import os

import numpy as np
import scipy as sp
import pandas as pd

from datetime import datetime
import time

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as md

path_tools = 'ita_public_tools/'
gz_file = 'test_log.gz' #logfile no formato binario
file_name = 'recreate.out' #logfile name

def logBinGz2Text(gz_file,output_name):
	os.chdir(path_tools)
	os.system("ls")
	os.system("make clean")
	os.system("make recreate")
	os.system("gzip -dc input/"+str(gz_file)+" | bin/recreate state/object_mappings.sort > output/"+str(output_name))
	os.chdir("../")


logBinGz2Text(gz_file,"recreate.out")

#pode ocorrer de algumas linhas vir com erro
data = pd.read_csv(path_tools+"output/"+file_name,sep=' ',header=None,error_bad_lines=False)

#R->clientID, date, MethodNames[method], - -   ObjectNames[R->objectID], ProtocolNames[http],   CodeNames[status],R->size
data = data.rename(columns={0: 'clientID', 3: 'timestamp',4 : 'url', 5 : 'protocol', 6: 'code', 7 : 'size'})
data = data.sort_values(['clientID', 'timestamp'], ascending=[True, True])

plt.hist(data['timestamp'])
plt.show()
