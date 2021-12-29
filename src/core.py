
import tokenize
import os
import runpy

from src.config import keyword_map


def translate_code(readline, keyword_map=keyword_map):
    for token in tokenize.generate_tokens(readline):
        type, word = token[0], token[1]
        # if type == tokenize.NAME and word in keyword_map:
        if word in keyword_map:
            yield type, keyword_map[word]
        else:
            yield type, word

def translate_file(file_path, keyword_map=keyword_map):
    if not os.path.exists(file_path):
        raise(f"pua: {file_path} does not exists.")
    file = open(file_path, encoding='utf-8')
    en_codes = translate_code(file.readline, keyword_map)
    sources = tokenize.untokenize(list(en_codes))
    file.close()
    return sources

def run_file(file_path, keyword_map=keyword_map):
    """run pua file

    Args:
        file_path: pua file path
    """
    if not os.path.exists(file_path):
        raise(f"pua: {file_path} does not exists.")
    sources = translate_file(file_path, keyword_map=keyword_map)
    runpy._run_module_code(sources, mod_name="__main__")

