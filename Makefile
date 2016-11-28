all: build

build:
	cd ~/pages/alexhagen.github.io; \
	git rm -r *; \
	cd ~/code/alexhagen.github.io; \
	jekyll build --destination=~/pages/alexhagen.github.io; \
	cd ~/pages/alexhagen.github.io; \
	git add *; \
	git commit -am "$(shell git log -1 --pretty=%B | tr -d '\n')"; \
	git push origin master; \
	cd ~/code/alexhagen.github.io
