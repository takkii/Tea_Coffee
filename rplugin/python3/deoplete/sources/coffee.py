import re
import base64
from deoplete.source.base import Base

# ------------------------------- KEYWORD -------------------------------------------------------------------------


home = expanduser("~")

dire1 = os.path.expanduser("~/.vim/.cache/dein/repos/github.com/takkii/Tea_Coffee/")
dire2 = os.path.expanduser("~/.vim/repos/github.com/takkii/Tea_Coffee/")
dire3 = os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/Tea_Coffee/")
dire4 = os.path.expanduser("~/.config/nvim/repos/github.com/takkii/Tea_Coffee/")
dire5 = os.path.expanduser("~/.cache/dein/repos/github.com/takkii/Tea_Coffee/")

if os.path.exists(dire1):
    java = open(os.path.expanduser("~/.vim/.cache/dein/repos/github.com/takkii/Tea_Coffee/complete/java_complete"))
elif os.path.exists(dire2):
    java = open(os.path.expanduser("~/.vim/repos/github.com/takkii/Tea_Coffee/complete/java_complete"))
elif os.path.exists(dire3):
    java = open(os.path.expanduser("~/.config/nvim/.cache/dein/repos/github.com/takkii/Tea_Coffee/complete/java_complete"))
elif os.path.exists(dire4):
    java = open(os.path.expanduser("~/.config/nvim/repos/github.com/takkii/Tea_Coffee/complete/java_complete"))
elif os.path.exists(dire5):
    java = open(os.path.expanduser("~/.cache/dein/repos/github.com/takkii/Tea_Coffee/complete/java_complete"))
else:
    print('どれにも該当しません、Tea_coffeeを入れてください。')

java_lib = java.readlines()
data_java = list(map(lambda s:s.rstrip(),java_lib))
java.close()

# ------------------------------- KEYWORD -------------------------------------------------------------------------


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'Tea_coffee'
        self.filetypes = ['java']
        self.mark = '[Lost_paradise]'
        javamatch = [r'\.[a-zA-Z0-9_?!]*|[a-zA-Z]\w*::\w*']
        regexmatch = [r'[<a-zA-Z(?: .+?)?>.*?<\/a-zA-Z>]']
        self.input_pattern = '|'.join(javamatch + regexmatch)
        self.rank = 500

    def get_complete_position(self, context):
        m = re.search('[a-zA-Z0-9_?!]*$', context['input'])
        return m.start() if m else -1

    def gather_candidates(self, context):
        try:
            dic = data_java
            dic.sort(key=lambda dic: dic[0])
            return dic
        except Exception:
            traceback.print_exc()