#================================================
from cx_Freeze import setup, Executable 
#================================================
setup(
    name = "ReadyApp", 
    version = "1.0.0", 
    description = "Plateforme de développement continu", 
    executables = [Executable("..\code\GProject\src\main.py")]
) 
#================================================
