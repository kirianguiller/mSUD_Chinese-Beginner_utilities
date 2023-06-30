import json
from conllup.conllup import readConlluFile
import csv 

list_structures = []

for level in ["A1", "A2", "B1", "B2", "C1"]:
    path_file = f"/home/wran/Downloads/dump_chinese_grammar_wiki_morphSUD(18)/parser/chinese-beginner.{level}.mSUD.conllu"
    sentences_json = readConlluFile(path_file)
    for sentence_json in sentences_json:
        structure_tuple = (sentence_json["metaJson"]["structure"], sentence_json["metaJson"]["structure_verbose"], level)
        if structure_tuple not in list_structures:
            list_structures.append(structure_tuple)


to_output_json = []

for structure in list_structures:
    to_output_json.append(
        {
            "structure": structure[0], 
            "structure_verbose": structure[1],
            "level": structure[2],
        }
    )

with open('grammar_patterns_bla.json', 'w') as output_file:
    json.dump(to_output_json, output_file, indent=4, ensure_ascii=False)