'''
File to convert the program into an executable file

```cmd
python setup.py build
```
'''

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base , icon="logo.ico")]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "OOMPA LOOMPA",
    options = options,
    version = "1.0",
    description = 'OOMPA LOOMPA',
    executables = executables
)
# creates the application
# i will add logo.ico later its not required anyway