import os
from conllup.conllup import readConlluFile, writeConlluFile

PATH_CONLL_FOLDERS = '../../mSUD_Chinese-Beginner/'

for file in os.listdir(PATH_CONLL_FOLDERS):
    path_file = os.path.join(PATH_CONLL_FOLDERS, file)
    print("KK file", path_file)
    if os.path.isfile(path_file) and file.endswith('.conllu'): 
        sentences = readConlluFile(path_file)
        for sentence in sentences:
            text_meta = sentence['metaJson']['text'].replace(" ", "")
            text_from_tokens = "".join([token['FORM'] for token in sentence['treeJson']['nodesJson'].values()])
            if text_meta != text_from_tokens:
                print("text_meta", text_meta)
                print("text_from_tokens", text_from_tokens)
            
            sentence['metaJson']['text_orig'] = sentence['metaJson']['text']
            sentence['metaJson']['text'] = text_from_tokens
            
            for token in sentence['treeJson']['nodesJson'].values():
                token["MISC"]["SpaceAfter"] = "No"

        writeConlluFile(path_file, sentences, overwrite=True)
            
