import os
import pinyin
from conllup.conllup import readConlluFile, writeConlluFile


PATH_CONLL_FOLDERS = 'data/3_splitted/'
PATH_OUTPUT = 'data/4_pinyin_added/'


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
                        # if token['UPOS'] == 'PUNCT':
                        #     continue
                        form = token['FORM']
                        pinyinized_form = pinyin.get(form, format="diacritical")
                        token['MISC']["Translit"] = pinyinized_form
                        if pinyinized_form == form:
                            # it's useless to add Tone if the form does not have a pinynized form
                            continue
                        token['MISC']["Tone"] = pinyin.get(form, format="numerical")[-1]

                writeConlluFile(path_output, sentences, overwrite=True)
