import os
from conllup.conllup import readConlluFile, writeConlluFile

PATH_CONLL_FOLDERS = '/home/kirian/Downloads/dump_chinese_grammar_wiki_morphSUD'
PATH_OUTPUT = '/home/kirian/Downloads/dump_chinese_grammar_wiki_morphSUD_converted'


for folder in os.listdir(PATH_CONLL_FOLDERS):
    path_folder = os.path.join(PATH_CONLL_FOLDERS, folder)
    if os.path.isdir(path_folder): 
        path_folder_output = os.path.join(PATH_OUTPUT, folder)
        if not os.path.exists(path_folder_output):
            os.makedirs(path_folder_output)

        for file in os.listdir(path_folder):
            if file.endswith('.conllu'):
                path_conll = os.path.join(path_folder, file)
                path_output = os.path.join(path_folder_output, file)
                sentences = readConlluFile(path_conll)
                for sentence in sentences:
                    for token in sentence['treeJson']['nodesJson'].values():
                        if token['XPOS'] != "_":
                            token['MISC']['CpdPos'] = token['XPOS']
                            token['XPOS'] = "_"
                        if token['MISC'].get('WordPos'):
                            token['MISC']['CpdPos'] = token['MISC']['WordPos']
                            del token['MISC']['WordPos']
            writeConlluFile(path_output, sentences, overwrite=True)
            