import os
from argparse import ArgumentParser
import globs


path_separator = globs.PATH_SEPARATOR or '/'
project_fname = globs.PROJECT_FNAME or '.pyqtc'


class PathSanitizer(object):
    ALLOWED_SEPARATORS_NUM = 1
    SEPARATOR = path_separator

    def __call__(self, string_to_check, substring_to_find):
        assert isinstance(string_to_check, str)
        assert isinstance(substring_to_find, str)
        result = self._sanitize(string_to_check, substring_to_find)
        return result

    def _get_number_of_separators(self, string_to_check, substring_to_find): #To deal with '//'
        possible_max_separators = 10
        for i in xrange(2, possible_max_separators + 1):
            to_search = substring_to_find * i
            if string_to_check.find(to_search) >= 0:
                return int(i)
        return None

    def _sanitize(self, string_to_check, substring_to_find):
        number = 1
        result = string_to_check
        while number:
            number = self._get_number_of_separators(result, substring_to_find)
            if number is None:
                break
            new_result = result.replace(substring_to_find * number, substring_to_find)
            result = new_result
        return result


pragma_once = PathSanitizer()

parser = ArgumentParser(description='Initiallizer of python projects in QtCreator.\nProduces a .pyqtc file, containing all .py files of project.')
parser.add_argument('-r', '--root', dest='root_dir', type=str, help='A root dir of python project', default=pragma_once(os.getcwd() + path_separator, path_separator))
parser.add_argument('-n', '--name', dest='project_name', type=str, help='A python project name', default=(os.path.dirname(os.getcwd()).strip(path_separator)))
parser.add_argument('--silent', dest='silent', type=bool, help='Do not launch QtCreator after', default=False)


if __name__ == '__main__':
    str_to_check = '/adc/de//f/ds///ds//dsa/'
    print(str_to_check)
    final = pragma_once(str_to_check, '/')
    print(final)
