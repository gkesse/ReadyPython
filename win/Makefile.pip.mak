all:

version: 
	@python -m $(GPIP_PACKAGE_NAME) --version
install: 
	@python -m pip install --upgrade $(GPIP_PACKAGE_NAME)
list: 
	@python -m pip list
rm: 
	@python -m pip uninstall -y $(GPIP_PACKAGE_NAME)
