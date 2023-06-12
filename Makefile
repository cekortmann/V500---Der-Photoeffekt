all: build/v500.pdf

build/v500.pdf: build/frequenz.pdf build/plotgruen.pdf build/plotlila.pdf build/plotgelb.pdf build/plotrot.pdf v500.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v500.tex
	lualatex  --output-directory=build v500.tex
	biber build/v500.bcf
	lualatex  --output-directory=build v500.tex

build/plotrot.pdf:  rot.txt rot2.txt plotrot.py| build
	python plotrot.py

build/plotfrequenz.pdf:  frequenz.txt frequenz2.txt frequenz.py| build
	python frequenz.py

build/plotgruen.pdf: gruen.txt gruen2.txt plotgruen.py| build
	python plotgruen.py

build/plotlila.pdf: lila.txt lila3.txt plotlila.py| build
	python plotlila.py

build/plotgelb.pdf: gelb.txt plotgelb.py| build
	python plotgelb.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
