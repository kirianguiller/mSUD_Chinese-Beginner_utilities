import os
from conllup.conllup import readConlluFile


PATH_CLOSSICON = "glossicon.txt"
PATH_CONLLS = 'mSUD_Chinese-Beginner'

glossicon = {}
if os.path.exists(PATH_CLOSSICON):
    with open(PATH_CLOSSICON, 'r') as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            gloss_key = " ".join(line.split(" ")[:-1])
            gloss_value = line.split(" ")[-1]
            glossicon[gloss_key] = gloss_value
        print("glossicon", glossicon)

for file in os.listdir(PATH_CONLLS):
    if file.endswith('.conllu'):
        path_conll = os.path.join(PATH_CONLLS, file)
        sentences = readConlluFile(path_conll)

        for sentence in sentences:
            for token in sentence['treeJson']['nodesJson'].values():
                if token['UPOS'] == 'PUNCT':
                    continue
                form = token['FORM']
                upos = token['UPOS']
                deprel = token['DEPREL']
                gloss_key = f"{form} {upos} {deprel}"
                if gloss_key not in glossicon:
                    glossicon[gloss_key] = "_UNK_"

with open(PATH_CLOSSICON, "w") as outfile:
    for key, value in dict(sorted(glossicon.items())).items():
        outfile.write(f"{key} {value}\n")