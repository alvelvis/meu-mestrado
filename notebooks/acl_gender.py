import os
if not os.path.isfile("estrutura_ud.py"):
    os.system("wget https://raw.githubusercontent.com/alvelvis/ACDC-UD/master/estrutura_ud.py")
import estrutura_ud
import copy

file = "../Petroles_3/Petroles_3_golden.conllu"
corpus = estrutura_ud.Corpus(recursivo=True)
corpus.load(file)

allowed_acl_head = ["PROPN", "NOUN", "SYM", "PRON"]
feat = "gender"
deprel = ["acl"]

for sentence in corpus.sentences.values():
    for token in sentence.tokens:
        if (token.deprel in deprel and 
        feat in token.__dict__ and 
        token.__dict__.get(feat, None) != token.head_token.__dict__.get(feat, None)):
            gender = token.__dict__.get(feat, "none")
            head = copy.copy(token.head_token)
            previous = copy.copy(token.previous_token)
            found = False
            while previous.id != "0":
                previous = copy.copy(previous.previous_token)
                if (gender == previous.__dict__.get(feat, None) and 
                previous.upos in allowed_acl_head):
                    if found:
                        token.misc = token.misc + " ou {} ({})".format(previous.word, previous.id)
                    else:
                        token.dephead = previous.id
                        found = True

file_name = file.rsplit("/", 1)[1]
corpus.save("regras.conllu")
os.system("python3 ../../conllu-merge-resolver/cosmo.py {} regras.conllu '.*'".format(file))
os.system("cp {} antes-{}".format(file, file_name))
os.system("rm regras-correcao.zip; zip regras-correcao.zip antes-{} regras.conllu".format(file_name))
os.remove("antes-{}".format(file_name))
os.remove("regras.conllu")