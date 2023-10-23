import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'ir_datasets'])

import ir_datasets
dataset = ir_datasets.load("wapo/v2/trec-news-2019")

for query in dataset.queries_iter():
    print(query)