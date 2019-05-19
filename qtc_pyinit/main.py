import misc
import os
import globs


def launch():
    args = misc.parser.parse_args()
    tool = ProjFileAppender(args)
    project_file = tool.make_prj_file()


class ProjFileAppender(object):
    FILES = []

    def __init__(self, args):
        self.args = args
        print(self.args.root_dir)
        print(self.args.project_name)

    def _search_files(self):
        working_dir = self.args.root_dir
        for root, dirs, files in os.walk(working_dir, topdown=True):
            for name in files:
                if name.endswith(globs.FILE_TYPE):
                    filepath = os.path.join(root, name)
                    print(filepath)
                    self.FILES.append(misc.pragma_once(filepath, globs.PATH_SEPARATOR))

    def make_prj_file(self):
        self._search_files()
        filename = misc.pragma_once(os.path.join(self.args.root_dir, self.args.project_name) + globs.PROJECT_FNAME, globs.PROJECT_FNAME)
        with open(filename, 'wt+') as project_file:
            for fname in self.FILES:
                project_file.write('%s\n' % fname)
        return filename



if __name__ == '__main__':
    launch()
