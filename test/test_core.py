import unittest
import os.path
import tokenize

from src.core import translate_code, translate_file, run_file


class TestCoreMethods(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        self.cur_path = os.path.dirname(__file__)
        self.code_file = 'examples/code_pua.txt'
        self.code_file = os.path.join(self.cur_path, self.code_file)

    def test_translate_keyword(self):
        with open(self.code_file, encoding='utf-8') as zh_file:
            en_codes = translate_code(zh_file.readline)
            en_codes = tokenize.untokenize(en_codes)
            with open(os.path.join(self.cur_path, 'examples/code_en.txt')) as excepted_file:
                excepted_codes = excepted_file.readlines()
                excepted_codes = ''.join(excepted_codes)
                self.assertEqual(en_codes, excepted_codes)
        
    def test_translate_file(self):
        sources = translate_file(self.code_file)
        with open(os.path.join(self.cur_path, 'examples/code_en.txt')) as excepted_file:
            excepted_code = excepted_file.readlines()
            excepted_code = ''.join(excepted_code)
            self.assertEqual(sources, excepted_code)
    
    def test_run_file(self):
        file = 'examples/helloworld_zh.pua'
        file_path = os.path.join(self.cur_path, file) 
        run_file(file_path)


if __name__ == '__main__':
    unittest.main()