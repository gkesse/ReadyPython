all:

version: 
	@python -m pip --version
install: 
	@python -m pip install $(GPIP_PACKAGE_NAME)
list: 
	@python -m pip list
show: 
	@python -m pip show $(GPIP_PACKAGE_NAME)
upgrade: 
	@python -m pip install --upgrade pip
