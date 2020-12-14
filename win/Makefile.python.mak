GSRC = ..\code\GProject\src
GBUILD = build\main
GTARGET = $(GBUILD)\main.exe
   
all: exe run

compile:
	@python $(GSRC)\main.py
exe:
	@python -m PyInstaller --noconfirm $(GSRC)\main.py
run:
	@set "PATH=C:\Python38" && $(GTARGET) $(argv)
clean: 
	@if not exist $(GBUILD) @mkdir $(GBUILD)
	@del /s /q $(GTARGET)
