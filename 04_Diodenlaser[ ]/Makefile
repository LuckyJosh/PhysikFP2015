all:	protocol clean
	


protocol:	Latex/*.tex ../../.global/latex/literatur.bib 
		cd Latex/;\
		pdflatex Protokoll.tex
		cd Latex/;\
		biber Protokoll
		cd Latex/;\
		pdflatex Protokoll.tex
		cd Latex/;\
		pdflatex Protokoll.tex
		mv Latex/Protokoll.pdf Protokoll.pdf
		make clean


Messdaten/*.txt: 

../../.global/latex/literatur.bib:


pdf2tex:
	python ../.global/python/pdf2tex.py

clean:  
	rm -f Latex/*.aux
	rm -f *.aux
	rm -f Latex/*.synctex
	rm -f *.synctex	
	rm -f Latex/*.synctex.gz
	rm -f *.synctex.gz
	rm -f Latex/*.blg
	rm -f *.blg
	rm -f Latex/*.log
	rm -f *.log
	rm -f Latex/*.nav
	rm -f *.nav
	rm -f Latex/*.out		
	rm -f *.out		
	rm -f Latex/*.run.xml
	rm -f *.run.xml
	rm -f Latex/*.snm
	rm -f *.snm
	rm -f Latex/*.toc	
	rm -f *.toc	
	rm -f Latex/*.tmp	
	rm -f *.tmp
	rm -f Latex/*.bcf	
	rm -f *.bcf
	rm -f Latex/*.bbl
	rm -f *.bbl
