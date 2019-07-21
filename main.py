# imports must find files, compile them to byte code, and run the code.
import sys                  # Load a library module

import module               # import a module, each module file is a package of variables—that is, a namespace
from module import var1     # from copies a module’s attributes, such that they become simple variables in the recipient

var1 = "This will overridden var1 reference by the by the 'import from' statement above!"

print(sys.platform)
print(module.var, var1)

input()
