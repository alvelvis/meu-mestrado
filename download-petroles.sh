rm Petroles.conllu
rm Petroles_2.conllu
wget http://interrogatorio.ica.ele.puc-rio.br/interrogar-ud/conllu/Petroles.conllu
wget http://interrogatorio.ica.ele.puc-rio.br/interrogar-ud/conllu/Petroles_2.conllu
meld --diff Petroles.conllu Petroles/Petroles.conllu
meld --diff Petroles_2.conllu Petroles/Petroles_2.conllu
