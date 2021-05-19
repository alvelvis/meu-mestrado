import os
if not os.path.isfile("estrutura_ud.py"):
    os.system("wget https://raw.githubusercontent.com/alvelvis/ACDC-UD/master/estrutura_ud.py")
import estrutura_ud
import copy

file = "../Petroles_3/Petroles_3_golden.conllu"
corpus = estrutura_ud.Corpus(recursivo=True)
corpus.load(file)

for sentence in corpus.sentences.values():
    for token in sentence.tokens:
        if token.lemma.lower() in ["abservar"]:
            token.word = ("o" if token.word.startswith("a") else "O") + "".join(token.word[1:]) 
            token.lemma = "observar"

file_name = file.rsplit("/", 1)[1]
corpus.save("regras.conllu")
os.system("python3 ../../conllu-merge-resolver/cosmo.py {} regras.conllu '.*'".format(file))
os.system("cp {} antes-{}".format(file, file_name))
os.system("rm regras-correcao.zip; zip regras-correcao.zip antes-{} regras.conllu".format(file_name))
os.remove("antes-{}".format(file_name))
os.remove("regras.conllu")