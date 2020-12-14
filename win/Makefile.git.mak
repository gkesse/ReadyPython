all:

push:
	@cd $(GPROJECT_PATH) && git pull && git add --all && git commit -m "Initial Commit" && git push -u origin master
commit:
	@cd $(GPROJECT_PATH) && git add --all && git commit -m "Initial Commit"
clone:
	@cd $(GPROJECT_ROOT) && git clone $(GGIT_URL) $(GGIT_NAME) 
