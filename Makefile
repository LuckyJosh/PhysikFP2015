new:
	$(MAKE) -C .template/ clean
	#mkdir $(filter-out $@,$(MAKECMDGOALS))[]
	cp -r .template/. $(filter-out $@,$(MAKECMDGOALS)[' '])
	mv $(filter-out $@,$(MAKECMDGOALS)[' '])/Protokoll.tex $(filter-out $@,$(MAKECMDGOALS)[' '])/Protokoll_$(filter-out $@,$(MAKECMDGOALS).tex)
	mv $(filter-out $@,$(MAKECMDGOALS)[' '])/Auswertung.py $(filter-out $@,$(MAKECMDGOALS)[' '])/Auswertung_$(filter-out $@,$(MAKECMDGOALS).tex)

done:
	mv $(filter-out $@,$(MAKECMDGOALS))[' '] $(filter-out $@,$(MAKECMDGOALS))[X]