import os
from conllup.conllup import readConlluFile, writeConlluFile

PATH_CLOSSICON = "glossicon.txt"
glossicon = {}
with open(PATH_CLOSSICON, 'r') as f:
    for line in f:
        line = line.strip()
        if line == "":
            continue
        gloss_key = " ".join(line.split(" ")[:-1])
        gloss_value = line.split(" ")[-1]
        glossicon[gloss_key] = gloss_value
    print("glossicon", glossicon)

PATH_CONLL_FOLDERS = 'data/4_pinyin_added'
PATH_OUTPUT = 'data/5_gloss_added/'

for folder in os.listdir(PATH_CONLL_FOLDERS):
    print("KK folder", folder)
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
                        unique_key = f"{token['FORM']} {token['UPOS']} {token['DEPREL']}"
                        to_attribute_gloss = glossicon.get(unique_key, "_UNK_")
                        already_present_gloss = token['MISC'].get("Gloss")
                        if already_present_gloss:
                            if already_present_gloss != to_attribute_gloss:
                                print("already_present_gloss", already_present_gloss, "to_attribute_gloss", to_attribute_gloss)
                        elif to_attribute_gloss != "_UNK_":
                            token['MISC']["Gloss"] = to_attribute_gloss

            writeConlluFile(path_output, sentences, overwrite=True)
            