# This code renames the file "Question10.py" to "Question10_old.py" using the os module in Python. It first imports the os module, then uses the rename() function to change the name of the file, and finally prints a message confirming that the file has been renamed.

import os          # imports the os module to perform operating system related tasks

os.rename("Question10.py", "Question10_old.py")       # renames the file "Question10.py" to "Question10_old.py" using the rename() function from the os module

print("The file has been renamed to Question10_old.py") 