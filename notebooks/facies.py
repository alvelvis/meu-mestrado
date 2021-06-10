import os
if not os.path.isfile("estrutura_ud.py"):
    os.system("wget https://raw.githubusercontent.com/alvelvis/ACDC-UD/master/estrutura_ud.py")
import estrutura_ud
import copy

file = "../Petroles_3/Petroles_3_golden.conllu"
corpus = estrutura_ud.Corpus(recursivo=True)
corpus.load(file)

fix_feats = lambda feats: "|".join(sorted([x for x in feats.split("|") if not any(x.startswith(y) for y in ["Gender", "_"])] + ["Gender=Fem"]))

for sentence in corpus.sentences.values():
    for t, token in enumerate(sentence.tokens):
        if token.word.lower() == "fácies":
            token.lemma = "fácies"
            token.feats = fix_feats(token.feats)
            for _token in sentence.tokens:
                if _token.dephead == token.id and _token.deprel not in ["case", "nmod", "acl:relcl", "punct", "conj", "advmod", "nmod:appos", "cc", "mark"]:
                    _token.feats = fix_feats(_token.feats)
                if "PronType=Rel" in _token.feats and _token.head_token.deprel == "acl:relcl" and _token.head_token.dephead == token.id:
                    _token.feats = fix_feats(_token.feats)

file_name = file.rsplit("/", 1)[1]
corpus.save("regras.conllu")
os.system("python3 ../../conllu-merge-resolver/cosmo.py {} regras.conllu '.*'".format(file))
os.system("cp {} antes-{}".format(file, file_name))
os.system("rm regras-correcao.zip; zip regras-correcao.zip antes-{} regras.conllu".format(file_name))
os.remove("antes-{}".format(file_name))
os.remove("regras.conllu")