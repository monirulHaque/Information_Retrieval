import sys
import subprocess
import os

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'ir_datasets'])

# imports
import ir_datasets

# clear the terminal after pip installation
clear = lambda: os.system('clear')
if os.name == 'nt':
    clear = lambda: os.system('cls')
clear()

# loading dataset for queries
dataset = ir_datasets.load("wapo/v2/trec-news-2018")

# check callable methods of a class
def getObjectMethods(object):
    return [method_name for method_name in dir(object) if callable(getattr(object, method_name))]

# testing queries_iter()
print('------------------testing queries_iter()---------------------------')
for query in dataset.queries_iter():
    print(query) #TrecBackgroundLinkingQuery(query_id='321', doc_id='9171debc316e5e2782e0d2404ca7d09d', url='https://www.washingtonpost.com/news/worldviews/wp/2016/09/01/women-are-half-of-the-world-but-only-22-percent-of-its-parliaments/<url>')
    print('******************************************')
    print(type(query))
    print('******************************************')
    print(getObjectMethods(query))
    print('******************************************')
    print(query.query_id)
    print('******************************************')
    print(query.doc_id)
    print('******************************************')
    print(query.url)
    break


# testing qrels_iter()
print('-------------------qrels_iter()--------------------------')
for qrels in dataset.qrels_iter():
    print(qrels) # TrecQrel(query_id='321', doc_id='00f57310e5c8ec7833d6756ba637332e', relevance=16, iteration='0')
    print('******************************************')
    print(qrels.query_id)
    print('******************************************')
    print(qrels.doc_id)
    print('******************************************')
    print(qrels.relevance)
    print('******************************************')
    print(qrels.iteration)
    break

# learning about the dataset
print('--------------------learning about the dataset-------------------------')
print("Total Queries:", dataset.queries_count())
print("Total Docs:", dataset.docs_count())
print("Total qrels:", dataset.qrels_count())
print("Has Doc Pairs?:", dataset.has_docpairs())
print("Has Doc Scores?:", dataset.has_scoreddocs())
print("Doc class", dataset.docs_cls())

# loading dataset for documents
print('-------------------loading dataset for documents--------------------------')
dataset = ir_datasets.load("wapo/v2")
for doc in dataset.docs_iter():
    print(doc)
    print('******************************************')
    print(type(doc)) #<class 'ir_datasets.datasets.wapo.WapoDoc'>
    print('******************************************')
    print(doc.doc_id) #b2e89334-33f9-11e1-825f-dabc29fd7071
    print('******************************************')
    print(doc.url) #https://www.washingtonpost.com/sports/colleges/danny-coale-jarrett-boykin-are-a-perfect-1-2-punch-for-virginia-tech/2011/12/31/gIQAAaW4SP_story.html
    print('******************************************')
    print(doc.title) #Danny Coale, Jarrett Boykin are a perfect 1-2 punch for Virginia Tech
    print('******************************************')
    print(doc.author) #Mark Giannotto
    print('******************************************')
    print(doc.published_date) #1325376562000
    print('******************************************')
    print(doc.kicker) #Colleges
    print('******************************************')
    print(doc.body) 
    print('******************************************')
    print(doc.body_paras_html)
    print('******************************************')
    print(doc.body_media)
    break
print('---------------------------------------------')