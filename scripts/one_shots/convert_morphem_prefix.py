import os
from conllup.conllup import readConlluFile, writeConlluFile

PATH_CONLL_FOLDERS = '../../../mSUD_Chinese-Beginner/'

for file in os.listdir(PATH_CONLL_FOLDERS):
    path_file = os.path.join(PATH_CONLL_FOLDERS, file)
    print("KK file", path_file)
    if os.path.isfile(path_file) and file.endswith('.conllu'): 
        sentences = readConlluFile(path_file)
        for sentence in sentences:
            for token in sentence['treeJson']['nodesJson'].values():
                token["DEPREL"] = token["DEPREL"].replace("@m", "/m")
                print(token["DEPREL"])

        writeConlluFile(path_file, sentences, overwrite=True)
            
