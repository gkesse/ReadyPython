GSRC = ..\code\GProject\src
GBUILD = build\main
GTARGET = $(GBUILD)\main.exe
   
all: clean compile

compile:
	@python $(GSRC)\main.py
exe:
	@python -m PyInstaller $(GSRC)\main.py
run:
	@$(GTARGET) $(argv)
clean: 
	@if not exist $(GBUILD) @mkdir $(GBUILD)
	@del /s /q $(GTARGET)
