"""
Package __init__.py Files

If you choose to use package imports, there is one more constraint you must follow: at least until Python 3.3, each directory named within the path of a package import statement must contain a file named __init__.py, or your package imports will fail.

The __init__.py files can contain Python code, just like normal module files. Their names are special because their code is run automatically the first
time a Python program imports a directory, and thus serves primarily as a hook for performing initialization steps required by the package.
These files can also be completely empty, though, and sometimes have additional roles.

PACKAGE INITIALIZATION FILE ROLES:

Package initialization
The first time a Python program imports through a directory, it automatically runs all the code in the directory’s __init__.py file. Because of that, these files are a natural place to put code to initialize the state required by files in a package. For instance, a package might use its initialization file to create required data files, open connections to databases, and so on. Typically, __init__.py files are not meant to be useful if executed directly; they are run automatically when a package is first accessed.

Module usability declarations
Package __init__.py files are also partly present to declare that a directory is a Python package. In this role, these files serve to prevent directories with common names from unintentionally hiding true modules that appear later on the module search path. Without this safeguard, Python might pick a directory that has nothing to do with your code, just because it appears nested in an earlier directory on the search path. As we’ll see later, Python 3.3’s namespace packages obviate much of this role, but achieve a similar effect algorithmically by scanning ahead on the path to find later files.

Module namespace initialization
In the package import model, the directory paths in your script become real nested object paths after an import. For instance, in the preceding example, after the import the expression dir1.dir2 works and returns a module object whose namespace contains all the names assigned by dir2’s __init__.py initialization file. Such files provide a namespace for module objects created for directories, which would otherwise have no real associated module file.

from * statement behavior
As an advanced feature, you can use __all__ lists in __init__.py files to define what is exported when a directory is imported with the from * statement form. In an __init__.py file, the __all__ list is taken to be the list of submodule names that should be automatically imported when from * is used on the package (directory) name. If __all__ is not set, the from * statement does not automatically load submodules nested in the directory; instead, it loads just names defined by assignments in the directory’s __init__.py file, including any submodules explicitly imported by code in this file. For instance, the statement from submodule import X in a directory’s __init__.py makes the name X available in that directory’s namespace. (We’ll see additional roles for __all__ in Chapter 25: it serves to declare from * exports of simple files as well.)
"""

print('from init of package data_types')

x_in_package_init = 939
