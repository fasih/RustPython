import sys

print(sys.argv)
assert sys.argv[0].endswith('.py')
assert  sys.__doc__ == "This module provides access to some objects used or maintained by the\ninterpreter and to functions that interact strongly with the interpreter.\n\nDynamic objects:\n\nargv -- command line arguments; argv[0] is the script pathname if known\npath -- module search path; path[0] is the script directory, else ''\nmodules -- dictionary of loaded modules\n\ndisplayhook -- called to show results in an interactive session\nexcepthook -- called to handle any uncaught exception other than SystemExit\n  To customize printing in an interactive session or to install a custom\n  top-level exception handler, assign other functions to replace these.\n\nstdin -- standard input file object; used by input()\nstdout -- standard output file object; used by print()\nstderr -- standard error object; used for error messages\n  By assigning other file objects (or objects that behave like files)\n  to these, it is possible to redirect all of the interpreter's I/O.\n\nlast_type -- type of last uncaught exception\nlast_value -- value of last uncaught exception\nlast_traceback -- traceback of last uncaught exception\n  These three are only available in an interactive session after a\n  traceback has been printed.\n\nStatic objects:\n\nbuiltin_module_names -- tuple of module names built into this interpreter\ncopyright -- copyright notice pertaining to this interpreter\nexec_prefix -- prefix used to find the machine-specific Python library\nexecutable -- absolute path of the executable binary of the Python interpreter\nfloat_info -- a struct sequence with information about the float implementation.\nfloat_repr_style -- string indicating the style of repr() output for floats\nhash_info -- a struct sequence with information about the hash algorithm.\nhexversion -- version information encoded as a single integer\nimplementation -- Python implementation information.\nint_info -- a struct sequence with information about the int implementation.\nmaxsize -- the largest supported length of containers.\nmaxunicode -- the value of the largest Unicode code point\nplatform -- platform identifier\nprefix -- prefix used to find the Python library\nthread_info -- a struct sequence with information about the thread implementation.\nversion -- the version of this interpreter as a string\nversion_info -- version information as a named tuple\n__stdin__ -- the original stdin; don't touch!\n__stdout__ -- the original stdout; don't touch!\n__stderr__ -- the original stderr; don't touch!\n__displayhook__ -- the original displayhook; don't touch!\n__excepthook__ -- the original excepthook; don't touch!\n\nFunctions:\n\ndisplayhook() -- print an object to the screen, and save it in builtins._\nexcepthook() -- print an exception and its traceback to sys.stderr\nexc_info() -- return thread-safe information about the current exception\nexit() -- exit the interpreter by raising SystemExit\ngetdlopenflags() -- returns flags to be used for dlopen() calls\ngetprofile() -- get the global profiling function\ngetrefcount() -- return the reference count for an object (plus one :-)\ngetrecursionlimit() -- return the max recursion depth for the interpreter\ngetsizeof() -- return the size of an object in bytes\ngettrace() -- get the global debug tracing function\nsetcheckinterval() -- control how often the interpreter checks for events\nsetdlopenflags() -- set the flags to be used for dlopen() calls\nsetprofile() -- set the global profiling function\nsetrecursionlimit() -- set the max recursion depth for the interpreter\nsettrace() -- set the global debug tracing function\n"
