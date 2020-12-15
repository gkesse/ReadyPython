GSRC = ..\code\GProject\src
GBUILD = build\main
GTARGET = $(GBUILD)\main.exe
   
all: exe run

version:
	@python --version
compile:
	@python $(GSRC)\main.py $(argv)
cxf:
	@python setup.py build
pyi:
	@python -m PyInstaller --noconfirm --onefile $(GSRC)\main.py
run:
	@$(GTARGET) $(argv)
clean: 
	@if not exist $(GBUILD) @mkdir $(GBUILD)
	@del /s /q $(GTARGET)
