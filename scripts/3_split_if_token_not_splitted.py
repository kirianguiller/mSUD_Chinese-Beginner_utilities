import os
from conllup.conllup import readConlluFile, writeConlluFile, readConlluFile, treeJson_T, _compareTokenIndexes, writeConlluFile
from conllup.processing import replaceArrayOfTokens


from typing import Union
import functools



# 我 是 一 个 中国 人 你呢 ？
# 1  2  3  4 5   6
# old_token_index = [5]
# newTokensForms = ["中", "国"]

def split_or_do_nothing(tree_json: treeJson_T) -> Union[treeJson_T, None]:
    for token_json in tree_json["nodesJson"].values():
        if len(token_json["FORM"]) > 1:
            print(token_json["FORM"])
            old_token_index = int(token_json["ID"])
            new_token_forms = list(token_json["FORM"])
            new_tree_json = replaceArrayOfTokens(tree_json, [old_token_index], new_token_forms, smartBehavior=True)
            for id_diff in range(1, len(new_token_forms)):
                this_added_char_id = str(old_token_index + id_diff)
                new_tree_json["nodesJson"][this_added_char_id]["HEAD"] = old_token_index
                new_tree_json["nodesJson"][this_added_char_id]["DEPREL"] = "@m"

            return new_tree_json
    return None


PATH_CONLL_FOLDERS = 'data/2_corrected/'
PATH_OUTPUT = 'data/3_splitted/'


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
                    finished = False
                    tree_json = sentence["treeJson"]
                    while finished == False:
                        new_tree_json = split_or_do_nothing(tree_json)
                        if new_tree_json is None:
                            finished = True
                        else:
                            print(sentence["metaJson"]["sent_id"])
                            tree_json = new_tree_json
                    
                    ids = sorted(tree_json["nodesJson"], key=functools.cmp_to_key(_compareTokenIndexes))
                    sentence["treeJson"] = tree_json
    
            writeConlluFile(path_output, sentences, overwrite=True)