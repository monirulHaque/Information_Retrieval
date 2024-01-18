import sys
import subprocess
import os

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'networkx'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'spacy'])

import numpy as np 
import pandas as pd 
import re
import networkx as nx
import spacy

