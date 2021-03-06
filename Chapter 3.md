 # Chapter Summary
 Several common ways to launch Python programs:
 
 1. Runing codes interactively using Python prompt.
 
 2. Runing codes typed in files with system command lines.
 
 3. File-icon clicks
 
 4. Module imports
 
 5. 'exec' calls.
 
 6. IDE GUIs such as IDIE.
 
 Tips: If you really want to force Python to run the file in the same session without stopping and restarting the session, you need to instead call the reload function available in the imp standard library module (this function is also a simple built-in Python 2.6, but not in 3.0)
 The reload function expects the name of an already loaded module object, so you have to have successfully imported a module once before reloading it.
 'reload' is a function that is called, and thereby should come with a parentheses around the module object name. 'import' is a statement. 
 
Modules serve the role of libraries of tools, and it is just a package of variable names, known as a namespace. The variable names within a module are called attributes.In the broader sheme of things, an attribute is simply a variable name that is attached to a specific object (like a module).
 
What makes from different from import?
From is just like an import, with an extra assignment to names in the importing component. Technically, 'from' copies a module's attributes, such that they become simple variables in the recipient-thus, you can simply refer to the imported string this time as title (a variable) instead of myfile.title (an attribute reference).

When the dir function is called with the name of an imported module passed in parentheses like this, it returns all the attributes inside that module. Some of the names it returns are names you get 'for free': names with leading and trailing double underscores are built-in names that are always predefined by Python and that have special meaning to the interpreter.

Because each file is a self-contained namespace,the names in one file cannot clash with those in another, even if they are spelled the same way.
 
 Useful tips:
 import versus from: I should point out that the from statement in a sense defeats the namespace partitioning purpose of modules--because the from copies variables from one file to another, it can cause same-named variables in the importing file to be overwritten (and won't warn you if it does). This essentially collapses namespaces together, at least in terms of the copied variables.
 
 After the first import, later imports do nothing, even if you change and save the module's source file again in another window. This is by design, imports are too expensive an operation to repeat more than once per file, per program run. If you really want to force Python to run the file again in the same session without stopping and restarting the session, you need to instead call the reload function avaivable in the imp standard library module. 
 
 Python searches for imported modules in every directory listed in sys.path--a Python list of directory name strings in the sys module, which is initialized from a PYTHONPATH enviroment variable, plus a set of standard directories. If you want to import from a directory other than the one you are working in, that directory must generally be listed in your PYTHONPATH setting. 

By contrast, the basic import statement runs the file only once per process, and it makes the file a separate module namespace so that its assignments will not change variables in your scope. The price you pay for the namespace partioning of modules is the need to reload after changes.

IDIE hint of the day: Alt-P key combination to scroll backward through the command history to repeat prior command, and Alt-N to scroll forward. Or just simply position the cursor on them.

# Using IDIE:
1. You must add ".py" explicitly when saving your files.
2. Run scripts by selecting Run-Run Module in text edit windows, not by interactive imports and reloads.
3. You need to reload only modules being tested interactively.
4. You can customize IDIE.
5. There is currently no clear-screen option in IDIE. Just press the ENTER key.
6. tkinter GUI and threaded programs may not work well with IDIE.
7. If connection error arise, try starting IDIE in single-process mode.
8. Beware of some IDIE usability features.

# Debugging Python Code
1. Do nothing; 2. insert print statements; 3. Use IDE GUI debuggers; 4. Use the pdb command-line debugger; 5. Other options.


# Test Your Knowledge: Quiz
1. How can you start an interactive interpreter session?
2. Where do you type a system command line to launch a script file?
3. Name four or more ways to run the code saved in a script file.
4. Name two pitfalls related to clicking file icons on Windows.
5. Why might you need to reload a module?
6. How do you run a script from within IDIE?
7. Name two pitfalls related to using IDIE.
8. What is a namespace, and how does it relate to module files?
