import sys
from utilities import *

class BaseView:

    def logout(self):
        print_yellow('Thank you', is_indent=False)
        sys.exit(0)
