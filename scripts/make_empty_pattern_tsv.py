from conllup.conllup import readConlluFile
import csv 

list_structures = []

for level in ["A1", "A2", "B1", "B2", "C1"]:
    path_file = PATH_TO_CONLLU_FILES
    sentences_json = readConlluFile(path_file)
    for sentence_json in sentences_json:
        structure_tuple = (sentence_json["metaJson"]["structure"], sentence_json["metaJson"]["structure_verbose"])
        if structure_tuple not in list_structures:
            list_structures.append(structure_tuple)


to_output_json = []

for structure in list_structures:
    to_output_json.append(
        {
            "structure": structure[0], 
            "structure_verbose": structure[1],
            "grew_pattern_sud": "pattern {  }",
            "grew_pattern_ud": "pattern {  }",
        }
    )

with open('grammar_patterns.tsv', 'w') as output_file:
    dw = csv.DictWriter(output_file, to_output_json[0].keys(), delimiter='\t')
    dw.writeheader()
    dw.writerows(to_output_json)