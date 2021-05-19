import os
if not os.path.isfile("estrutura_ud.py"):
    os.system("wget https://raw.githubusercontent.com/alvelvis/ACDC-UD/master/estrutura_ud.py")
import estrutura_ud
import copy

file = "../Petroles_3/Petroles_3_golden.conllu"
corpus = estrutura_ud.Corpus(recursivo=True)
corpus.load(file)

lemmas = {
    'a': 'a', 
    'partir': 'partir',
    'de': 'de',
    }

upos = {
    'a': 'ADP',
    'partir': 'VERB',
    'de': 'ADP',
    }

feats = {
    'a': '_',
    'partir': 'VerbForm=Inf',
    'de': '_',
    }

for sentence in corpus.sentences.values():
    for token in sentence.tokens:
        if (token.word.lower() in ["a"] and
        token.next_token.word.lower() in ["partir"] and
        token.next_token.next_token.word.lower() in ["de"]):
            if token.next_token.next_token.deprel != "fixed":
                token.next_token.next_token.head_token.dephead = token.dephead
                token.dephead = token.next_token.next_token.dephead
            token.deprel = "case"
            token.misc = "|".join(sorted(
                [x for x in token.misc.split("|") if not x.startswith("MWEPOS=") and x != "_"] + 
                ["MWEPOS=ADP"]))
            token.next_token.deprel = "fixed"
            token.next_token.next_token.deprel = "fixed"
            token.next_token.dephead = token.id
            token.next_token.next_token.dephead = token.id
            token.lemma = lemmas[token.word.lower()]
            token.feats = feats[token.word.lower()]
            token.next_token.lemma = lemmas[token.next_token.word.lower()]
            token.next_token.next_token.lemma = lemmas[token.next_token.next_token.word.lower()]
            token.next_token.feats = feats[token.next_token.word.lower()]
            token.next_token.next_token.feats = feats[token.next_token.next_token.word.lower()]
            token.next_token.upos = upos[token.next_token.word.lower()]
            token.next_token.next_token.upos = upos[token.next_token.next_token.word.lower()]
            for _token in sentence.tokens:
                if _token.dephead in [token.id, token.next_token.id, token.next_token.next_token.id] and _token.deprel != "fixed":
                    _token.dephead = token.dephead

file_name = file.rsplit("/", 1)[1]
corpus.save("regras.conllu")
os.system("python3 ../../conllu-merge-resolver/cosmo.py {} regras.conllu '.*'".format(file))
os.system("cp {} antes-{}".format(file, file_name))
os.system("rm regras-correcao.zip; zip regras-correcao.zip antes-{} regras.conllu".format(file_name))
os.remove("antes-{}".format(file_name))
os.remove("regras.conllu")