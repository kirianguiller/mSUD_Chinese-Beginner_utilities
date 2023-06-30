import os
from conllup.conllup import readConlluFile, writeConlluFile

PATH_CONLL_FOLDERS = 'data/1_deduplicated/'
PATH_OUTPUT = 'data/2_corrected/'


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
                    if sentence['metaJson'].get('translation_english'):
                        sentence['metaJson']['text_en'] = sentence['metaJson']['translation_english']
                        del sentence['metaJson']['translation_english']
                    if sentence['metaJson'].get('pinyin'):
                        sentence['metaJson']['translit'] = sentence['metaJson']['pinyin']
                        del sentence['metaJson']['pinyin']
            writeConlluFile(path_output, sentences, overwrite=True)
            