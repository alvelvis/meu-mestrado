import os
if not os.path.isfile("estrutura_ud.py"):
    os.system("wget https://raw.githubusercontent.com/alvelvis/ACDC-UD/master/estrutura_ud.py")
import estrutura_ud
import copy

file = "../Petroles_3/Petroles_3_golden.conllu"
corpus = estrutura_ud.Corpus(recursivo=True)
corpus.load(file)

lemmas = {
    'visto': 'ver', 
    'já': 'já',
    'uma': 'um',
    'vez': 'vez',
    'que': 'que'}

upos = {
    'uma': 'DET',
    'vez': 'NOUN',
    'que': 'SCONJ',
    'visto': 'VERB',
    'já': 'ADV'}

feats = {
    'visto': 'Gender=Masc|Number=Sing|VerbForm=Part',
    'uma': 'Definite=Ind|Gender=Fem|Number=Sing|PronType=Art',
    'que': '_',
    'já': '_',
    'vez': 'Gender=Fem|Number=Sing'}

for sentence in corpus.sentences.values():
    for token in sentence.tokens:
        if (token.word.lower() in ["visto", "já"] and
        token.next_token.word.lower() in ["que"]):
            if token.deprel != "mark":
                token.next_token.head_token.dephead = token.head_token.id
                token.next_token.head_token.deprel = "advcl"
            else:
                token.head_token.deprel = "advcl"
            token.deprel = "mark"
            token.upos = upos[token.word.lower()]
            token.feats = feats[token.word.lower()]
            token.lemma = lemmas[token.word.lower()]
            token.next_token.lemma = lemmas[token.next_token.word.lower()]
            token.next_token.upos = upos[token.next_token.word.lower()]
            token.next_token.deprel = "fixed"
            token.next_token.feats = feats[token.next_token.word.lower()]
            if token.next_token.dephead != token.id:
                token.dephead = token.next_token.dephead
                token.next_token.dephead = token.id            
            token.misc = "|".join(sorted([
                x for x in token.misc.split("|") if x != "_" and not x.startswith("MWEPOS")] + 
                ["MWEPOS=SCONJ"]))
            for _token in sentence.tokens:
                if _token.dephead == token.id and _token.deprel != "fixed":
                    _token.dephead = token.dephead

file_name = file.rsplit("/", 1)[1]
corpus.save("regras.conllu")
os.system("python3 ../../conllu-merge-resolver/cosmo.py {} regras.conllu '.*'".format(file))
os.system("cp {} antes-{}".format(file, file_name))
os.system("rm regras-correcao.zip; zip regras-correcao.zip antes-{} regras.conllu".format(file_name))
os.remove("antes-{}".format(file_name))
os.remove("regras.conllu")