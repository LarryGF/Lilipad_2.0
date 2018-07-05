clean: 
	rm -rf vue/dist vue/build web dist

vuecompile:
	cd vue && rm -rf dist/* && npm run build

vuedev:
	cd vue && npm run dev

webdata: vuecompile
	mkdir -p web && cp -r vue/dist/* web

