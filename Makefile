all: build/v500.pdf

build/v500.pdf: v500.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v500.tex
	lualatex  --output-directory=build v500.tex
	biber build/v500.bcf
	lualatex  --output-directory=build v500.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
