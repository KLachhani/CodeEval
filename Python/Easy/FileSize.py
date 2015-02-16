__author__ = 'Kishan'

import sys
import os

sys.stdout.write(str(os.stat(sys.argv[1]).st_size))
