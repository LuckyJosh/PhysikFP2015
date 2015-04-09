all:	protocol clean
	


protocol:	Latex/*.tex ../../globales/latex/Literatur.bib Plots/*.pdf
		cd Latex/;\
		pdflatex Protokoll.tex
		cd Latex/;\
		biber Protokoll
		cd Latex/;\
		pdflatex Protokoll.tex
		cd Latex/;\
		pdflatex Protokoll.tex
		mv Latex/Protokoll.pdf Protokoll.pdf

Plots/*.pdf:	Python/*.py Messdaten/*.txt
		python Python/*.py

Messdaten/*.txt: 

../../globales/latex/Literatur.bib:

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