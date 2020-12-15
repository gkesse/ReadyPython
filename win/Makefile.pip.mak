all:

version: 
	@python -m $(GPIP_PACKAGE_NAME) --version
install: 
	@python -m pip install $(GPIP_PACKAGE_NAME)
list: 
	@python -m pip list
upgrade: 
	@python -m pip install --upgrade $(GPIP_PACKAGE_NAME)
reinstall: 
	@python -m pip install --force-reinstall $(GPIP_PACKAGE_NAME)
