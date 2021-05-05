rm Petroles_3_stanza.conllu
wget http://interrogatorio.ica.ele.puc-rio.br/interrogar-ud/conllu/Petroles_3_stanza.conllu
meld --diff Petroles_3_stanza.conllu Petroles_3/Petroles_3_golden.conllu
