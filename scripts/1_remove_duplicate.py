import os
from conllup.conllup import readConlluFile, writeConlluFile, readConlluFile, treeJson_T, _compareTokenIndexes, writeConlluFile
from conllup.processing import replaceArrayOfTokens


from typing import Union
import functools


PATH_CONLL_FOLDERS = 'data/0_dump/'
PATH_OUTPUT = 'data/1_deduplicated/'

count = 0
total = 0
path_folder_parser = os.path.join(PATH_CONLL_FOLDERS, "parser")
list_unique_sentences = []
list_id_to_take = []
to_take_by_struct_and_file = {}
sent_id_to_newkey = {}

if os.path.isdir(path_folder_parser): 
    # path_folder_output = os.path.join(PATH_OUTPUT, folder)
    for file in os.listdir(path_folder_parser):
        if file.endswith('.conllu'):
            to_take_by_struct_and_file[file] = {}
            print("processing file", file)
            path_conll = os.path.join(path_folder_parser, file)
            # path_output = os.path.join(path_folder_output, file)
            sentences = readConlluFile(path_conll)

            
            for sentence in sentences:
                struct_verbose = sentence["metaJson"]["structure_verbose"]
                if struct_verbose not in to_take_by_struct_and_file[file]:
                    to_take_by_struct_and_file[file][struct_verbose] = []

                total += 1
                unique_content = sentence["metaJson"]["text"] + struct_verbose
                if unique_content not in list_unique_sentences:
                    list_unique_sentences.append(unique_content)
                    list_id_to_take.append(sentence["metaJson"]["sent_id"])
                    to_take_by_struct_and_file[file][struct_verbose].append(sentence["metaJson"]["sent_id"])
                    sent_id_to_newkey[sentence["metaJson"]["sent_id"]] = len(to_take_by_struct_and_file[file][struct_verbose])
                
                else:
                    count += 1
                    print("Duplicated", sentence["metaJson"]["sent_id"], unique_content)
                    print(sentence["metaJson"]["url"])
        # writeConlluFile(path_output, sentences, overwrite=True)
print("number of duplicated : ", count)
print("number to keep : ", len(list_id_to_take))
print(total)
assert len(list_id_to_take) + count == total, "number are not matching, check the code"


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
                sentences_de_duplicated = []
                for sentence in sentences:
                    if sentence["metaJson"]["sent_id"] in list_id_to_take:
                        sentences_de_duplicated.append(sentence)
            writeConlluFile(path_output, sentences_de_duplicated, overwrite=True)    