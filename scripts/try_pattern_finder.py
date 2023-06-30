import sys,os

from grewpy import Graph, Corpus, GRSDraft, Rule, Request, Commands, GRS, set_config

set_config("sud")

PATH_CONLL_A1 = "../SUD_Chinese-Beginner/chinese-beginner.A1.mSUD.conllu"

corpus = Corpus(PATH_CONLL_A1)
graph = corpus[0]
print(graph)

PATTERN = """
GOV -[mod]-> DEP; GOV.form = "有"; DEP.form = "没"
"""
PATTERN = """GOV -[mod]-> DEP; GOV[upos = VERB|AUX]; DEP.form = "不"; GOV -[1=comp]-> OBJ; OBJ>>GOV"""
results = corpus.search(Request(PATTERN))

print(len(results), "sentence(s) found")
for result_ in results:

    result: Graph = corpus[result_["sent_id"]]
    print(result.json_data()["meta"]["text"])
