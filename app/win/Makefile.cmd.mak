GSRC = $(GPROJECT_SRC)
GBUILD = build\main
GTARGET = $(GBUILD)\main.exe
   
#================================================
# all
all: python_compile
#================================================
# python
python_version:
	@python --version
python_compile:
	python $(GSRC)\main.py $(argv)
cxf:
	@python setup.py build
pyi:
	@python -m PyInstaller --noconfirm --onefile $(GSRC)\main.py
run:
	@$(GTARGET) $(argv)
clean: 
	@if not exist $(GBUILD) @mkdir $(GBUILD)
	@del /s /q $(GTARGET)
#================================================
# git
git_push:
	@cd $(GPROJECT_PATH) && git pull && git add --all && git commit -m "Initial Commit" && git push -u origin master
git_commit:
	@cd $(GPROJECT_PATH) && git add --all && git commit -m "Initial Commit"
git_clone:
	@cd $(GPROJECT_ROOT) && git clone $(GGIT_URL) $(GGIT_NAME) 
#================================================
# pip
pip_version: 
	@python -m $(GPIP_PACKAGE_NAME) --version
pip_install: 
	@python -m pip install --upgrade $(GPIP_PACKAGE_NAME)
pip_list: 
	@python -m pip list
pip_rm: 
	@python -m pip uninstall -y $(GPIP_PACKAGE_NAME)
#================================================
