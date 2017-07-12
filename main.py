# -*- coding: UTF-8 -*-
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
import sys

path_tools = 'ita_public_tools/'
gz_file = 'test_log.gz' #logfile no formato binario
if sys.argv[1] != "" :
	gz_file = sys.argv[1]
file_name = 'recreate.out' #logfile name

def logBinGz2Text(gz_file,output_name):
	os.chdir(path_tools)
	os.system("ls")
	os.system("make clean")
	os.system("make recreate")
	os.system("gzip -dc input/"+str(gz_file)+" | bin/recreate state/object_mappings.sort > output/"+str(output_name))
	os.chdir("../")


logBinGz2Text(gz_file,"recreate.out")

# pode ocorrer de algumas linhas vir com erro
data = pd.read_csv(path_tools+"output/"+file_name,sep=' ',header=None,error_bad_lines=False)

#R->clientID, date, MethodNames[method], - -   ObjectNames[R->objectID], ProtocolNames[http],   CodeNames[status],R->size
data = data.rename(columns={0: 'clientID', 3: 'timestamp',4 : 'url', 5 : 'protocol', 6: 'code', 7 : 'size'})
data = data.sort_values(['clientID', 'timestamp'], ascending=[True, True])

sns.distplot(data['timestamp'],kde=True)
#plt.hist(data['timestamp'])
plt.title("Requests X Time - file : "+str(gz_file))
plt.ylabel("Requests")
plt.xlabel("Time")
plt.xlim(min(data['timestamp']),max(data['timestamp']))
spacing = np.linspace(min(data['timestamp']),max(data['timestamp']),5)
times = [time.strftime('%H:%M:%S', time.localtime(item)) for item in spacing]
plt.xticks(spacing, times)
plt.savefig('figs/Requests_X_Time'+gz_file[:len(gz_file)-3]+'.png')
plt.show()


#cdf
sns.distplot(data['timestamp'], hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
plt.ylim(0,1)
plt.title("Probability X Requests - file : "+str(gz_file))
plt.ylabel("Probability")
plt.xlabel("Requests")
plt.xlim(min(data['timestamp']),max(data['timestamp']))
spacing = np.linspace(min(data['timestamp']),max(data['timestamp']),5)
times = [time.strftime('%H:%M:%S', time.localtime(item)) for item in spacing]
plt.xticks(spacing, times)
plt.savefig('figs/Probability_X_Requests'+gz_file[:len(gz_file)-3]+'.png')
plt.show()

