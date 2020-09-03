"""
Basic definitions:

module: any *.py file. Its name is the file name.
built-in module: a “module” (written in C) that is compiled into the Python interpreter, and therefore does not have a *.py file.
package: any folder containing a file named __init__.py in it. Its name is the name of the folder. In Python 3.3 and above, any folder (even without a __init__.py file) is considered a package

Imports and modules:

When a module is imported, Python runs all of the code in the module file. When a package is imported, Python runs all of the code in the package’s __init__.py file, if such a file exists.

imports must find module's file, compile them to byte code (if needed), and run the module’s code to build the objects it defines

* Compile if - byte code file is older than the source file (i.e., if you’ve changed the source) or was created by a different Python version, Python automatically regenerates the byte code when the program is run
* Don't compile if - Python finds a .pyc byte code file that is not older than the corresponding .py source file and was created by the same Python version, it skips the source-to-byte-code compile step

The final step of an import operation executes the byte code of the module. All statements in the file are run in turn, from top to bottom, and any assignments made to names during this step generate attributes of the resulting module object.

Any given module is imported only once per process by default. Future imports skip all three import steps and reuse the already loaded module in memory. If you need to import a file again after it has already been loaded (for example, to support dynamic end-user customizations), you have to force the issue with an imp.reload call

The Module Search Path - need to tell Python where to look to find files to import:

1. The home directory of the program (automatic) - directory containing your program’s top-level script file
2. PYTHONPATH directories (if set) (configurable) - Python searches all directories listed in your PYTHONPATH environment variable setting, from left to right
3. Standard library directories (automatic) - Python automatically searches the directories where the standard library modules are installed on your machine
4. The contents of any .pth files (if present) (configurable) - advanced feature, google
5. The site-packages home of third-party extensions (automatic) - Python automatically adds the site-packages subdirectory of its standard library to the module search path. By convention, this is the place that most third-party extensions are installed

It is also possible to create a Python module by writing code in an external language such as C, C++, and others (e.g., Java, in the Jython implementation of the language). Such modules are called extension modules
"""
import asyncio

import sys  # Load a library module
from importlib import reload

from langauge import module, shell_commands, data_types
# from module1 import *                   # Copy out all variables in the file (note that this will not copy out variables from multiple python files, just one)
# from M import func as mfunc    # Rename uniquely with "as"
from langauge.async_io import coroutine, event_loop, async_io, future_and_tasks, async_with, run_in_executor, \
    async_for_and_async_comphrension
from langauge.data_types import basic_types, collection_types, x_in_package_init
from langauge.data_types import file_type
from langauge.exception import exceptions, context_management
from langauge.functions import generators, lambda_expressions, functions_and_scopes
from langauge.oop.oop import \
    demo  # from copies a module’s attributes, such that they become simple variables in the recipient
from langauge.package1 import utility as pkg1_util
from langauge.package2 import utility as pkg2_util
from langauge.statements_expressions import expressions, assignments, statements
from langauge.threads import threads, locks, conditions, race_condition

reload(module)  # reload module

print('Module search path - ', sys.path)
print('Namespace of the module - ', module.__dict__.keys())

# commenting out line below so that it does not get removed while optimizing imports
# from module import var1     from copies a module’s attributes, such that they become simple variables in the recipient

var1 = "This will overridden var1 reference by the by the 'import from' statement above!"

print(sys.platform)
print(module.var1, var1)

'''
`python -m pydoc -b` command to start browser only mode of PyDoc. The effect is to start PyDoc as a locally running web server on a dedicated (but by default arbitrary unused) port, and pop up
 a web browser to act as client, displaying a page giving links to documentation for all the modules importable on your module search path (including the directory where PyDoc is launched).
 
 If you ask for documentation for a top-level script file, though, the shell window where you launched PyDoc serves as the script’s standard input and output for any user interaction. The net effect is that the documentation page for a script will appear AFTER IT RUNS THE SCRIPT, AND AFTER ITS PRINTED OUTPUT SHOWS UP IN THE SHELL WINDOW.
'''
print('Pydoc for module - ', module.__doc__)  # print out pydoc for the module called 'module'

'''
Weak Reference - implemented by the weakref standard library module, is a reference to an object that does not by itself prevent the referenced object from being garbage-collected. 
If the last remaining references to an object are weak references, the object is reclaimed and the weak references to it are automatically deleted (or otherwise notified).
'''
print("sys.getrefcount(1) = ", sys.getrefcount(
    1))  # Python garbage collects an object as soon as its reference count goes to 0, python caches values like ints

aString = ''

print(dir(aString))  # dir() attempts to return all attributes of this object
print(help(aString.replace))  # Get info on a specific attribute
print(dir(
    str))  # Both dir and help also accept as arguments either a real object (like our string S), or the name of a data type (like str, list, and dict)
print(dir(str.replace))

basic_types.demo()
collection_types.demo()
file_type.demo()

print('var in package init file - ', x_in_package_init)
print('var in package init file - ', data_types.x_in_package_init)
print('reload imported directory / package - ', reload(data_types))

pkg1_util.printing_fun()
pkg2_util.printing_fun()

shell_commands.demo()


# helper method
def create_new_event_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop


async_io.demo()
coroutine.demo()
event_loop.demo()
create_new_event_loop()
future_and_tasks.demo()
async_with.demo()
run_in_executor.demo()
async_for_and_async_comphrension.demo()

print('\n\nDone!')
