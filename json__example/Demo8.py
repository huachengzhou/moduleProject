import json as jsonUtils
import os as osUtils

import pathlib as pathLib

DIR_THIS_ = osUtils.sep.join(*(pathLib.Path.cwd(),))

print(DIR_THIS_)
