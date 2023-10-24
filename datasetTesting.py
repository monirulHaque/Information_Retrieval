import sys
import subprocess
import os
import ir_datasets

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'ir_datasets'])

# clear the terminal after pip installation
clear = lambda: os.system('clear')
if os.name == 'nt':
    clear = lambda: os.system('cls')
clear()

# loading dataset for queries
dataset = ir_datasets.load("wapo/v2/trec-news-2019")

# check callable methods of a class
def getObjectMethods(object):
    return [method_name for method_name in dir(object) if callable(getattr(object, method_name))]

# testing queries_iter()
for query in dataset.queries_iter():
    print(query)
    print(type(query))
    print(getObjectMethods(query))
    print(query.query_id)
    print(query.doc_id)
    print(query.url)
    break

# testing qrels_iter()
for qrels in dataset.qrels_iter():
    print(qrels)
    print(qrels.query_id)
    print(qrels.doc_id)
    print(qrels.relevance)
    print(qrels.iteration)
    break

# learning about the dataset
print("Total Queries:", dataset.queries_count())
print("Total Docs:", dataset.docs_count())
print("Total qrels:", dataset.qrels_count())
print("Has Doc Pairs?:", dataset.has_docpairs())
print("Has Doc Scores?:", dataset.has_scoreddocs())
print("Doc class", dataset.docs_cls())

# loading dataset for documents
dataset = ir_datasets.load("wapo/v2")
for doc in dataset.docs_iter():
    print(doc)
    print(type(doc))
    print(doc.doc_id)
    print(doc.url)
    print(doc.title)
    print(doc.author)
    print(doc.published_date)
    print(doc.kicker)
    print(doc.body)
    print(doc.body_paras_html)
    print(doc.body_media)
    break
