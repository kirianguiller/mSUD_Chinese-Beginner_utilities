#!/bin/bash

# The name of your file
OUTPUT_FILENAME="zh_beginner-sud-test.conllu"
PATH_CONLLUS_FOLDER="./mSUD_Chinese-Beginner"
PATH_GREW_GRS="../tools/converter/grs/zh_mSUD_to_SUD.grs"
# Create the file if it doesn't exist
touch "$OUTPUT_FILENAME"

# Empty the file
> "$OUTPUT_FILENAME"


# Levels
LEVELS=("A1" "A2" "B1" "B2" "C1")
for LEVEL in "${LEVELS[@]}"; do
    # Construct the filename for each level
    INPUT_FILENAME="$PATH_CONLLUS_FOLDER/chinese-beginner.$LEVEL.mSUD.conllu"
    opam exec -- grew transform -grs "$PATH_GREW_GRS" -config sud -i "$INPUT_FILENAME" -strat zh_mSUD_to_SUD_main >> "$OUTPUT_FILENAME"
done