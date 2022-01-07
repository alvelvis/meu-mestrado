# changelog_sema

Last update: 2022-1-7-1:50:18

## Regras para B=CAMPO

* Aline Silveira
* Date:   Wed Aug 18 19:22:06 2021 -0300
* Lines changed: 99
* Commit: [226aa79550f0842f205240d0c43935cfd428d81f](https://github.com/alvelvis/meu-mestrado/commit/226aa79550f0842f205240d0c43935cfd428d81f)
* Patch file: [2021_8_18_19-22-06-226aa79550f0842f205240d0c43935cfd428d81f.patch](patch_changelog_sema/2021_8_18_19-22-06-226aa79550f0842f205240d0c43935cfd428d81f.patch)

Regras para B=CAMPO

```diff
 # text = A Bacia de Pelotas é a mais meridional na costa brasileira (Figura 1) e apresenta poucos trabalhos publicados a seu respeito se comparada às outras bacias de margem continental brasileiras.
 # sent_id = 247-20140910-MONOGRAFIA_0-2
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
-2	Bacia	bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	O	_
+2	Bacia	Bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	B=BACIA	_
 3	de	de	ADP	_	_	2	flat:name	O	_
 4	Pelotas	Pelotas	PROPN	_	Number=Sing	2	flat:name	B=BACIA	_
 5	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	cop	O	_
```

## Regras para B=UNIDADE_LITOESTRATIGRÁFICA

* Maria Clara Castro
* Date:   Wed Aug 18 19:23:20 2021 -0300
* Lines changed: 169
* Commit: [8559b82e8dbfcce0a511e5435f089b9cbf462a15](https://github.com/alvelvis/meu-mestrado/commit/8559b82e8dbfcce0a511e5435f089b9cbf462a15)
* Patch file: [2021_8_18_19-23-20-8559b82e8dbfcce0a511e5435f089b9cbf462a15.patch](patch_changelog_sema/2021_8_18_19-23-20-8559b82e8dbfcce0a511e5435f089b9cbf462a15.patch)

Regras para B=UNIDADE_LITOESTRATIGRÁFICA

```diff
 # text = A Bacia de Pelotas é a mais meridional na costa brasileira (Figura 1) e apresenta poucos trabalhos publicados a seu respeito se comparada às outras bacias de margem continental brasileiras.
 # sent_id = 247-20140910-MONOGRAFIA_0-2
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
-2	Bacia	bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	O	_
+2	Bacia	Bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	B=BACIA	_
 3	de	de	ADP	_	_	2	flat:name	O	_
 4	Pelotas	Pelotas	PROPN	_	Number=Sing	2	flat:name	B=BACIA	_
 5	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	cop	O	_
```

## Regras para B=BACIA

* Tatiana Cavalcanti
* Date:   Thu Aug 19 11:40:12 2021 -0300
* Lines changed: 223
* Commit: [b4ce4f35cba57636d3e032f30cc8e865b2b099ad](https://github.com/alvelvis/meu-mestrado/commit/b4ce4f35cba57636d3e032f30cc8e865b2b099ad)
* Patch file: [2021_8_19_11-40-12-b4ce4f35cba57636d3e032f30cc8e865b2b099ad.patch](patch_changelog_sema/2021_8_19_11-40-12-b4ce4f35cba57636d3e032f30cc8e865b2b099ad.patch)

Regras para B=BACIA

```diff
 # text = A Bacia de Pelotas é a mais meridional na costa brasileira (Figura 1) e apresenta poucos trabalhos publicados a seu respeito se comparada às outras bacias de margem continental brasileiras.
 # sent_id = 247-20140910-MONOGRAFIA_0-2
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
-2	Bacia	bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	O	_
+2	Bacia	Bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	B=BACIA	_
 3	de	de	ADP	_	_	2	flat:name	O	_
 4	Pelotas	Pelotas	PROPN	_	Number=Sing	2	flat:name	B=BACIA	_
 5	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	cop	O	_
```

## Regras para B=GEOCRONOLOGIA

* Aline Silveira
* Date:   Wed Aug 25 19:23:23 2021 -0300
* Lines changed: 8
* Commit: [4a4aa82216f1d360758dd3bce77553100e0de996](https://github.com/alvelvis/meu-mestrado/commit/4a4aa82216f1d360758dd3bce77553100e0de996)
* Patch file: [2021_8_25_19-23-23-4a4aa82216f1d360758dd3bce77553100e0de996.patch](patch_changelog_sema/2021_8_25_19-23-23-4a4aa82216f1d360758dd3bce77553100e0de996.patch)

Regras para B=GEOCRONOLOGIA

```diff
 3-4	desta	_	_	_	_	_	_	_	_
 3	de	de	ADP	_	_	5	case	O	_
 4	esta	este	DET	_	Gender=Fem|Number=Sing|PronType=Dem	5	det	O	_
-5	Zona	Zona	PROPN	_	Gender=Fem|Number=Sing	2	nmod	O	_
+5	Zona	Zona	PROPN	_	Gender=Fem|Number=Sing	2	nmod	B=GEOCRONOLOGIA	_
 6	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	cop	O	_
 7	possivelmente	possivelmente	ADV	_	_	8	advmod	O	_
 8	pré-neógeno	pré-neógeno	NOUN	_	Gender=Masc|Number=Sing	0	root	O	_
```

## Sentenciação corrigida de frases que terminavam com Fm.

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Sep 1 00:09:42 2021 -0300
* Lines changed: 572
* Commit: [b3cfec4aea74f99aeb4b4758c42ed5850af40a2c](https://github.com/alvelvis/meu-mestrado/commit/b3cfec4aea74f99aeb4b4758c42ed5850af40a2c)
* Patch file: [2021_9_1_00-09-42-b3cfec4aea74f99aeb4b4758c42ed5850af40a2c.patch](patch_changelog_sema/2021_9_1_00-09-42-b3cfec4aea74f99aeb4b4758c42ed5850af40a2c.patch)

Sentenciação corrigida de frases que terminavam com Fm.

```diff
 33	Fé	Fé	PROPN	_	Number=Sing	31	flat:name	O	_
 34	.	.	PUNCT	_	_	3	punct	O	_
-# text = Rochas da Fm.
+# text = Rochas da Fm. Abaeté foram descritas principalmente na região de Cana Brava, Município de João Pinheiro (MG), onde ocorrem com relativa frequência e com espessuras significativas.
 # sent_id = 283-20150917-MONOGRAFIA_0-125
-1	Rochas	rocha	NOUN	_	Gender=Fem|Number=Plur	0	root	O	_
+1	Rochas	rocha	NOUN	_	Gender=Fem|Number=Plur	8	nsubj:pass	O	_
 2-3	da	_	_	_	_	_	_	_	_
 2	de	de	ADP	_	_	4	case	O	_
 3	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	det	O	_
 4	Fm	Fm	PROPN	_	Gender=Fem|Number=Sing	1	nmod	O	_
-5	.	.	PUNCT	_	_	1	punct	O	_
-
-# text = Abaeté foram descritas principalmente na região de Cana Brava, Município de João Pinheiro (MG), onde ocorrem com relativa frequência e com espessuras significativas.
-# sent_id = 283-20150917-MONOGRAFIA_0-126
-1	Abaeté	Abaeté	PROPN	_	Gender=Masc|Number=Sing	3	nsubj:pass	O	_
-2	foram	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	3	aux:pass	O	_
-3	descritas	descrever	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass	0	root	O	_
-4	principalmente	principalmente	ADV	_	_	3	advmod	O	_
-5-6	na	_	_	_	_	_	_	_	_
-5	em	em	ADP	_	_	7	case	O	_
-6	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	O	_
-7	região	região	NOUN	_	Gender=Fem|Number=Sing	3	obl	O	_
-8	de	de	ADP	_	_	9	case	O	_
-9	Cana	Cana	PROPN	_	Gender=Masc|Number=Sing	7	nmod	O	_
-10	Brava	Brava	PROPN	_	Number=Sing	9	flat:name	O	_
-11	,	,	PUNCT	_	_	12	punct	O	_
-12	Município	município	NOUN	_	Gender=Masc|Number=Sing	9	appos	O	_
+5	.	.	PUNCT	_	_	4	flat:name	O	_
+6	Abaeté	Abaeté	PROPN	_	Gender=Masc|Number=Sing	4	flat:name	O	_
+7	foram	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	8	aux:pass	O	_
+8	descritas	descrever	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass	0	root	O	_
+9	principalmente	principalmente	ADV	_	_	8	advmod	O	_
+10-11	na	_	_	_	_	_	_	_	_
+10	em	em	ADP	_	_	12	case	O	_
+11	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	12	det	O	_
+12	região	região	NOUN	_	Gender=Fem|Number=Sing	8	obl	O	_
 13	de	de	ADP	_	_	14	case	O	_
-14	João	João	PROPN	_	Gender=Masc|Number=Sing	12	nmod	O	_
-15	Pinheiro	Pinheiro	PROPN	_	Number=Sing	14	flat:name	O	_
-16	(	(	PUNCT	_	_	17	punct	O	_
-17	MG	MG	PROPN	_	Gender=Masc|Number=Sing	14	nmod:appos	O	_
-18	)	)	PUNCT	_	_	17	punct	O	_
-19	,	,	PUNCT	_	_	3	punct	O	_
-20	onde	onde	PRON	_	Gender=Fem|Number=Sing|PronType=Rel	21	nsubj	O	_
-21	ocorrem	ocorrer	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	7	acl:relcl	O	_
-22	com	com	ADP	_	_	24	case	O	_
-23	relativa	relativo	ADJ	_	Gender=Fem|Number=Sing	24	amod	O	_
-24	frequência	frequência	NOUN	_	Gender=Fem|Number=Sing	21	obl	O	_
-25	e	e	CCONJ	_	_	27	cc	O	_
-26	com	com	ADP	_	_	27	case	O	_
-27	espessuras	espessura	NOUN	_	Gender=Fem|Number=Plur	24	conj	O	_
-28	significativas	significativo	ADJ	_	Gender=Fem|Number=Plur	27	amod	O	_
-29	.	.	PUNCT	_	_	3	punct	O	_
+14	Cana	Cana	PROPN	_	Gender=Masc|Number=Sing	12	nmod	O	_
+15	Brava	Brava	PROPN	_	Number=Sing	14	flat:name	O	_
+16	,	,	PUNCT	_	_	17	punct	O	_
+17	Município	município	NOUN	_	Gender=Masc|Number=Sing	14	appos	O	_
+18	de	de	ADP	_	_	19	case	O	_
+19	João	João	PROPN	_	Gender=Masc|Number=Sing	17	nmod	O	_
+20	Pinheiro	Pinheiro	PROPN	_	Number=Sing	19	flat:name	O	_
+21	(	(	PUNCT	_	_	22	punct	O	_
+22	MG	MG	PROPN	_	Gender=Masc|Number=Sing	19	nmod:appos	O	_
+23	)	)	PUNCT	_	_	22	punct	O	_
+24	,	,	PUNCT	_	_	8	punct	O	_
+25	onde	onde	PRON	_	Gender=Fem|Number=Sing|PronType=Rel	26	nsubj	O	_
+26	ocorrem	ocorrer	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	12	acl:relcl	O	_
+27	com	com	ADP	_	_	29	case	O	_
+28	relativa	relativo	ADJ	_	Gender=Fem|Number=Sing	29	amod	O	_
+29	frequência	frequência	NOUN	_	Gender=Fem|Number=Sing	26	obl	O	_
+30	e	e	CCONJ	_	_	32	cc	O	_
+31	com	com	ADP	_	_	32	case	O	_
+32	espessuras	espessura	NOUN	_	Gender=Fem|Number=Plur	29	conj	O	_
+33	significativas	significativo	ADJ	_	Gender=Fem|Number=Plur	32	amod	O	_
+34	.	.	PUNCT	_	_	8	punct	O	_
 # text = Próximo a Presidente Olegário (MG) foram descritos neste estudo pacotes siliciclásticos relativamente espessos (até 60 m) pertencentes a esta formação.
 # sent_id = 283-20150917-MONOGRAFIA_0-127
```

## Sema quando a abreviação foi mal tokenizada

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Sep 8 08:09:05 2021 -0300
* Lines changed: 60
* Commit: [371a74a3e82fd96156b862ceffda4925e6faf8f1](https://github.com/alvelvis/meu-mestrado/commit/371a74a3e82fd96156b862ceffda4925e6faf8f1)
* Patch file: [2021_9_8_08-09-05-371a74a3e82fd96156b862ceffda4925e6faf8f1.patch](patch_changelog_sema/2021_9_8_08-09-05-371a74a3e82fd96156b862ceffda4925e6faf8f1.patch)

Sema quando a abreviação foi mal tokenizada

```diff
 2-3	da	_	_	_	_	_	_	_	_
 2	de	de	ADP	_	_	4	case	O	_
 3	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	det	O	_
-4	Fm	Fm	PROPN	_	Gender=Fem|Number=Sing	1	nmod	O	_
-5	.	.	PUNCT	_	_	4	flat:name	O	_
+4	Fm	Fm	PROPN	_	Gender=Fem|Number=Sing	1	nmod	B=UNIDADE_LITOESTRATIGRÁFICA	_
+5	.	.	PROPN	_	_	4	flat:name	O	_
 6	Abaeté	Abaeté	PROPN	_	Gender=Masc|Number=Sing	4	flat:name	O	_
 7	foram	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	8	aux:pass	O	_
 8	descritas	descrever	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass	0	root	O	_
```

## Regras para B=UNIDADE_LITOESTRATIGRÁFICA

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Sep 8 08:09:50 2021 -0300
* Lines changed: 124
* Commit: [92deb69651a5393f0a8e36520453363f2b0031ec](https://github.com/alvelvis/meu-mestrado/commit/92deb69651a5393f0a8e36520453363f2b0031ec)
* Patch file: [2021_9_8_08-09-50-92deb69651a5393f0a8e36520453363f2b0031ec.patch](patch_changelog_sema/2021_9_8_08-09-50-92deb69651a5393f0a8e36520453363f2b0031ec.patch)

Regras para B=UNIDADE_LITOESTRATIGRÁFICA

```diff
 5-6	do	_	_	_	_	_	_	_	_
 5	de	de	ADP	_	_	3	fixed	O	_
 6	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	7	det	O	_
-7	Terraço	Terraço	PROPN	_	Gender=Masc|Number=Sing	2	nmod	O	_
+7	Terraço	Terraço	PROPN	_	Gender=Masc|Number=Sing	2	nmod	B=UNIDADE_LITOESTRATIGRÁFICA	_
 8	de	de	ADP	_	_	7	flat:name	O	_
 9	Rio	Rio	PROPN	_	Number=Sing	7	flat:name	O	_
 10	Grande	Grande	PROPN	_	Number=Sing	7	flat:name	O	_
```

## Novas entidades a partir de coordenações

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Fri Sep 10 18:35:10 2021 +0000
* Lines changed: 95
* Commit: [081a59fcd72436e3ee95e2689894990abd6398db](https://github.com/alvelvis/meu-mestrado/commit/081a59fcd72436e3ee95e2689894990abd6398db)
* Patch file: [2021_9_10_18-35-10-081a59fcd72436e3ee95e2689894990abd6398db.patch](patch_changelog_sema/2021_9_10_18-35-10-081a59fcd72436e3ee95e2689894990abd6398db.patch)

Novas entidades a partir de coordenações

```diff
 24	conglomeráticos	conglomerático	ADJ	_	Gender=Masc|Number=Plur	23	amod	O	_
 25	)	)	PUNCT	_	_	21	punct	O	_
 26	,	,	PUNCT	_	_	27	punct	O	_
-27	Iapó	Iapó	PROPN	_	Gender=Masc|Number=Sing	18	conj	O	_
+27	Iapó	Iapó	PROPN	_	Gender=Masc|Number=Sing	18	conj	B=UNIDADE_LITOESTRATIGRÁFICA	_
 28	(	(	PUNCT	_	_	29	punct	O	_
 29	diamictitos	diamictito	NOUN	_	Gender=Masc|Number=Plur	27	parataxis	O	_
 30	)	)	PUNCT	_	_	29	punct	O	_
 31	e	e	CCONJ	_	_	32	cc	O	_
-32	Vila	Vila	PROPN	_	Gender=Fem|Number=Sing	18	conj	O	_
+32	Vila	Vila	PROPN	_	Gender=Fem|Number=Sing	18	conj	B=UNIDADE_LITOESTRATIGRÁFICA	_
 33	Maria	Maria	PROPN	_	Number=Sing	32	flat:name	O	_
 34	(	(	PUNCT	_	_	35	punct	O	_
 35	folhelhos	folhelho	NOUN	_	Gender=Masc|Number=Plur	32	parataxis	O	_
```

## regras para juntar os flat:name, compound e fixed com gap

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Sep 15 12:32:45 2021 -0300
* Lines changed: 172
* Commit: [1a060032f9a11afed1f66139089182823718a018](https://github.com/alvelvis/meu-mestrado/commit/1a060032f9a11afed1f66139089182823718a018)
* Patch file: [2021_9_15_12-32-45-1a060032f9a11afed1f66139089182823718a018.patch](patch_changelog_sema/2021_9_15_12-32-45-1a060032f9a11afed1f66139089182823718a018.patch)

regras para juntar os flat:name, compound e fixed com gap

```diff
 18	(	(	PUNCT	_	_	19	punct	O	_
 19	Norte	Norte	PROPN	_	Gender=Masc|Number=Sing	15	appos	O	_
 20-21	da	_	_	_	_	_	_	_	_
-20	de	de	ADP	_	_	19	flat:name	O	_
-21	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	19	flat:name	O	_
+20	de	de	ADP	_	_	22	case	O	_
+21	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	22	det	O	_
 22	Bacia	Bacia	PROPN	_	Number=Sing	19	nmod	B=BACIA	_
-23	de	de	ADP	_	_	19	flat:name	O	_
-24	Pelotas	Pelotas	PROPN	_	Number=Sing	19	flat:name	B=BACIA	_
+23	de	de	ADP	_	_	22	flat:name	O	_
+24	Pelotas	Pelotas	PROPN	_	Number=Sing	22	flat:name	B=BACIA	_
 25	)	)	PUNCT	_	_	19	punct	O	_
 26	ainda	ainda	ADV	_	_	27	advmod	O	_
 27	sofria	sofrer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Imp|VerbForm=Fin	12	ccomp	O	_
```

## Novas entidades a partir de coordenações -- Parte 2

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Mon Sep 20 19:03:49 2021 -0300
* Lines changed: 61
* Commit: [cba25738cacf75dc179cde10cfd29ebf52147d18](https://github.com/alvelvis/meu-mestrado/commit/cba25738cacf75dc179cde10cfd29ebf52147d18)
* Patch file: [2021_9_20_19-03-49-cba25738cacf75dc179cde10cfd29ebf52147d18.patch](patch_changelog_sema/2021_9_20_19-03-49-cba25738cacf75dc179cde10cfd29ebf52147d18.patch)

Novas entidades a partir de coordenações -- Parte 2

```diff
 31	de	de	ADP	_	_	30	flat:name	O	_
 32	Pelotas	Pelotas	PROPN	_	Number=Sing	30	flat:name	B=BACIA	_
 33	,	,	PUNCT	_	_	34	punct	O	_
-34	registro	registro	NOUN	_	Gender=Masc|Number=Sing	30	conj	O	_
+34	registro	registro	NOUN	_	Gender=Masc|Number=Sing	16	conj	O	_
 35	sônico	sônico	ADJ	_	Gender=Masc|Number=Sing	34	amod	O	_
 36	,	,	PUNCT	_	_	37	punct	O	_
-37	pasta	pasta	NOUN	_	Gender=Fem|Number=Sing	30	conj	O	_
+37	pasta	pasta	NOUN	_	Gender=Fem|Number=Sing	16	conj	O	_
 38	de	de	ADP	_	_	39	case	O	_
 39	poço	poço	NOUN	_	Gender=Masc|Number=Sing	37	nmod	O	_
 40	,	,	PUNCT	_	_	41	punct	O	_
-41	perfil	perfil	NOUN	_	Gender=Masc|Number=Sing	30	conj	O	_
+41	perfil	perfil	NOUN	_	Gender=Masc|Number=Sing	16	conj	O	_
 42	composto	composto	ADJ	_	Gender=Masc|Number=Sing	41	amod	O	_
 43	,	,	PUNCT	_	_	44	punct	O	_
-44	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	30	conj	O	_
+44	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	16	conj	O	_
 45	gravimétrico	gravimétrico	ADJ	_	Gender=Masc|Number=Sing	44	amod	O	_
 46	e	e	CCONJ	_	_	47	cc	O	_
 47	magnetométrico	magnetométrico	ADJ	_	Gender=Masc|Number=Sing	45	conj	O	_
```

## Novas entidades a partir de coordenações -- Parte 3

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Sep 28 18:41:39 2021 -0300
* Lines changed: 37
* Commit: [566c4f4aa1eff82c22b7a0c9008b36dea5f2712e](https://github.com/alvelvis/meu-mestrado/commit/566c4f4aa1eff82c22b7a0c9008b36dea5f2712e)
* Patch file: [2021_9_28_18-41-39-566c4f4aa1eff82c22b7a0c9008b36dea5f2712e.patch](patch_changelog_sema/2021_9_28_18-41-39-566c4f4aa1eff82c22b7a0c9008b36dea5f2712e.patch)

Novas entidades a partir de coordenações -- Parte 3

```diff
 39	,	,	PUNCT	_	_	40	punct	O	_
 40	Teresina	Teresina	PROPN	_	Gender=Fem|Number=Sing	37	conj	B=UNIDADE_LITOESTRATIGRÁFICA	_
 41	e	e	CCONJ	_	_	42	cc	O	_
-42	parte	parte	NOUN	_	Gender=Fem|Number=Sing	37	conj	O	_
+42	parte	parte	NOUN	_	Gender=Fem|Number=Sing	36	conj	O	_
 43-44	da	_	_	_	_	_	_	_	_
 43	de	de	ADP	_	_	45	case	O	_
 44	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	45	det	O	_
```

## Adicionando sema I de acordo com flat:name

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sat Oct 23 01:29:41 2021 -0300
* Lines changed: 1582
* Commit: [56a3b7b1ea6614a7de89b590d05c6ba5da97cbe4](https://github.com/alvelvis/meu-mestrado/commit/56a3b7b1ea6614a7de89b590d05c6ba5da97cbe4)
* Patch file: [2021_10_23_01-29-41-56a3b7b1ea6614a7de89b590d05c6ba5da97cbe4.patch](patch_changelog_sema/2021_10_23_01-29-41-56a3b7b1ea6614a7de89b590d05c6ba5da97cbe4.patch)

Adicionando sema I de acordo com flat:name

```diff
 # sent_id = 247-20140910-MONOGRAFIA_0-2
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
 2	Bacia	Bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	B=BACIA	_
-3	de	de	ADP	_	_	2	flat:name	O	_
-4	Pelotas	Pelotas	PROPN	_	Number=Sing	2	flat:name	B=BACIA	_
+3	de	de	ADP	_	_	2	flat:name	I=BACIA	_
+4	Pelotas	Pelotas	PROPN	_	Number=Sing	2	flat:name	I=BACIA	_
 5	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	cop	O	_
 6	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	8	det	O	_
 7	mais	mais	ADV	_	_	8	advmod	O	_
```

## Conversão de GEOCRONOLOGIA para UNIDADE_CRONOESTRATIGRÁFICA

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Oct 27 09:46:26 2021 -0300
* Lines changed: 455
* Commit: [fbf1f850b5368d17dfa267afe3e44bfc0ef96a6b](https://github.com/alvelvis/meu-mestrado/commit/fbf1f850b5368d17dfa267afe3e44bfc0ef96a6b)
* Patch file: [2021_10_27_09-46-26-fbf1f850b5368d17dfa267afe3e44bfc0ef96a6b.patch](patch_changelog_sema/2021_10_27_09-46-26-fbf1f850b5368d17dfa267afe3e44bfc0ef96a6b.patch)

Conversão de GEOCRONOLOGIA para UNIDADE_CRONOESTRATIGRÁFICA

```diff
 45	estratigráficos	estratigráfico	ADJ	_	Gender=Masc|Number=Plur	44	amod	O	_
 46	mapeados	mapear	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part	44	acl	O	_
 47	(	(	PUNCT	_	_	48	punct	O	_
-48	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	44	appos	B=GEOCRONOLOGIA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+48	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	44	appos	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
 49-50	do	_	_	_	_	_	_	_	_
-49	de	de	ADP	_	_	48	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-50	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	48	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-51	Embasamento	Embasamento	PROPN	_	Number=Sing	48	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+49	de	de	ADP	_	_	48	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+50	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	48	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+51	Embasamento	Embasamento	PROPN	_	Number=Sing	48	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
 52	,	,	PUNCT	_	_	53	punct	O	_
-53	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=GEOCRONOLOGIA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+53	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
 54-55	do	_	_	_	_	_	_	_	_
-54	de	de	ADP	_	_	53	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-55	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	53	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-56	Rifte	Rifte	PROPN	_	Number=Sing	53	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+54	de	de	ADP	_	_	53	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+55	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	53	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+56	Rifte	Rifte	PROPN	_	Number=Sing	53	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
 57	,	,	PUNCT	_	_	58	punct	O	_
-58	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=GEOCRONOLOGIA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+58	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
 59-60	do	_	_	_	_	_	_	_	_
-59	de	de	ADP	_	_	58	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-60	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	58	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-61	Albiano	Albiano	PROPN	_	Number=Sing	58	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+59	de	de	ADP	_	_	58	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+60	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	58	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+61	Albiano	Albiano	PROPN	_	Number=Sing	58	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
 62	,	,	PUNCT	_	_	63	punct	O	_
-63	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=GEOCRONOLOGIA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+63	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
 64-65	do	_	_	_	_	_	_	_	_
-64	de	de	ADP	_	_	63	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-65	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	63	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-66	Cretáceo	Cretáceo	PROPN	_	Number=Sing	63	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-67	Superior	Superior	PROPN	_	Number=Sing	63	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+64	de	de	ADP	_	_	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+65	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+66	Cretáceo	Cretáceo	PROPN	_	Number=Sing	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+67	Superior	Superior	PROPN	_	Number=Sing	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
 68	,	,	PUNCT	_	_	69	punct	O	_
-69	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=GEOCRONOLOGIA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+69	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
 70-71	do	_	_	_	_	_	_	_	_
-70	de	de	ADP	_	_	69	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-71	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	69	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-72	Eoceno	Eoceno	PROPN	_	Number=Sing	69	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+70	de	de	ADP	_	_	69	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+71	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	69	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+72	Eoceno	Eoceno	PROPN	_	Number=Sing	69	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
 73	e	e	CCONJ	_	_	74	cc	O	_
-74	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=GEOCRONOLOGIA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+74	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
 75-76	do	_	_	_	_	_	_	_	_
-75	de	de	ADP	_	_	74	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-76	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	74	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-77	Mioceno	Mioceno	PROPN	_	Number=Sing	74	flat:name	I=GEOCRONOLOGIA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+75	de	de	ADP	_	_	74	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+76	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	74	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+77	Mioceno	Mioceno	PROPN	_	Number=Sing	74	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
 78	)	)	PUNCT	_	_	48	punct	O	_
 79	.	.	PUNCT	_	_	15	punct	O	_
```

## litologia e tipo_fluido

* Maria Clara Castro
* Date:   Tue Dec 7 11:53:46 2021 -0300
* Lines changed: 4034
* Commit: [fba2de17575b774aee209ea6ea9548f6a44ae7b2](https://github.com/alvelvis/meu-mestrado/commit/fba2de17575b774aee209ea6ea9548f6a44ae7b2)
* Patch file: [2021_12_7_11-53-46-fba2de17575b774aee209ea6ea9548f6a44ae7b2.patch](patch_changelog_sema/2021_12_7_11-53-46-fba2de17575b774aee209ea6ea9548f6a44ae7b2.patch)

litologia e tipo_fluido

```diff
 23	atinge	atingir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	21	acl:relcl	O	_
 24	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	25	det	O	_
 25	coberturas	cobertura	NOUN	_	Gender=Fem|Number=Plur	23	obj	O	_
-26	metassedimentares	metassedimentar	ADJ	_	Gender=Fem|Number=Plur	25	amod	B=LITOLOGIA	_
+26	metassedimentares	metassedimentar	ADJ	_	Gender=Fem|Number=Plur	25	amod	O	_
 27-28	meso-a	_	_	_	_	_	_	_	_
 27	meso	meso	NOUN	_	Gender=Masc|Number=Sing	26	obl	O	_
 28	a	a	ADP	_	_	29	case	O	_
```

## sistema deposicional

* Tatiana Cavalcanti
* Date:   Tue Dec 7 11:57:09 2021 -0300
* Lines changed: 469
* Commit: [1b3a1e1177fa095bcc6034b0fc856e9b444522d7](https://github.com/alvelvis/meu-mestrado/commit/1b3a1e1177fa095bcc6034b0fc856e9b444522d7)
* Patch file: [2021_12_7_11-57-09-1b3a1e1177fa095bcc6034b0fc856e9b444522d7.patch](patch_changelog_sema/2021_12_7_11-57-09-1b3a1e1177fa095bcc6034b0fc856e9b444522d7.patch)

sistema deposicional

```diff
 30	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	26	obl:arg	O	_
 31	de	de	ADP	_	_	32	case	O	_
 32	margem	margem	NOUN	_	Gender=Fem|Number=Sing	30	nmod	O	_
-33	continental	continental	ADJ	_	Gender=Fem|Number=Sing	32	amod	B=SISTEMA_DEPOSICIONAL	_
+33	continental	continental	ADJ	_	Gender=Fem|Number=Sing	32	amod	O	_
 34	brasileiras	brasileiro	ADJ	_	Gender=Fem|Number=Plur	30	amod	O	_
 35	.	.	PUNCT	_	_	8	punct	O	_
```

## Estrutura deposicional e poços

* Aline Silveira
* Date:   Wed Dec 8 11:41:35 2021 -0300
* Lines changed: 758
* Commit: [9f4b3162c32d889b4569e72ef236b848ea3c0d73](https://github.com/alvelvis/meu-mestrado/commit/9f4b3162c32d889b4569e72ef236b848ea3c0d73)
* Patch file: [2021_12_8_11-41-35-9f4b3162c32d889b4569e72ef236b848ea3c0d73.patch](patch_changelog_sema/2021_12_8_11-41-35-9f4b3162c32d889b4569e72ef236b848ea3c0d73.patch)

Estrutura deposicional e poços

```diff
 5-6	pela	_	_	_	_	_	_	_	_
 5	por	por	ADP	_	_	7	case	O	_
 6	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	O	_
-7	presença	presença	NOUN	_	Gender=Fem|Number=Sing	4	obl:agent	B=ESTRUTURA_DEPOSICIONAL	_
+7	presença	presença	NOUN	_	Gender=Fem|Number=Sing	4	obl:agent	O	_
 8	de	de	ADP	_	_	9	case	O	_
 9	sequência	sequência	NOUN	_	Gender=Fem|Number=Sing	7	nmod	O	_
 10	sedimentar	sedimentar	ADJ	_	Gender=Fem|Number=Sing	9	amod	O	_
```

## Correções de sema duplicados

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Dec 9 17:19:20 2021 -0300
* Lines changed: 155
* Commit: [b4177285db2f20b511409f98b78c505dc6333a78](https://github.com/alvelvis/meu-mestrado/commit/b4177285db2f20b511409f98b78c505dc6333a78)
* Patch file: [2021_12_9_17-19-20-b4177285db2f20b511409f98b78c505dc6333a78.patch](patch_changelog_sema/2021_12_9_17-19-20-b4177285db2f20b511409f98b78c505dc6333a78.patch)

Correções de sema duplicados

```diff
 45	estratigráficos	estratigráfico	ADJ	_	Gender=Masc|Number=Plur	44	amod	O	_
 46	mapeados	mapear	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part	44	acl	O	_
 47	(	(	PUNCT	_	_	48	punct	O	_
-48	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	44	appos	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+48	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	44	appos	O	_
 49-50	do	_	_	_	_	_	_	_	_
-49	de	de	ADP	_	_	48	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-50	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	48	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-51	Embasamento	Embasamento	PROPN	_	Number=Sing	48	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+49	de	de	ADP	_	_	48	flat:name	O	_
+50	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	48	flat:name	O	_
+51	Embasamento	Embasamento	PROPN	_	Number=Sing	48	flat:name	B=UNIDADE_LITOESTRATIGRÁFICA	_
 52	,	,	PUNCT	_	_	53	punct	O	_
-53	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+53	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	O	_
 54-55	do	_	_	_	_	_	_	_	_
-54	de	de	ADP	_	_	53	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-55	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	53	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-56	Rifte	Rifte	PROPN	_	Number=Sing	53	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+54	de	de	ADP	_	_	53	flat:name	O	_
+55	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	53	flat:name	O	_
+56	Rifte	Rifte	PROPN	_	Number=Sing	53	flat:name	O	_
 57	,	,	PUNCT	_	_	58	punct	O	_
-58	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+58	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	O	_
 59-60	do	_	_	_	_	_	_	_	_
-59	de	de	ADP	_	_	58	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-60	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	58	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-61	Albiano	Albiano	PROPN	_	Number=Sing	58	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+59	de	de	ADP	_	_	58	flat:name	O	_
+60	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	58	flat:name	O	_
+61	Albiano	Albiano	PROPN	_	Number=Sing	58	flat:name	B=UNIDADE_CRONOESTRATIGRÁFICA	_
 62	,	,	PUNCT	_	_	63	punct	O	_
-63	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+63	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	O	_
 64-65	do	_	_	_	_	_	_	_	_
-64	de	de	ADP	_	_	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-65	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-66	Cretáceo	Cretáceo	PROPN	_	Number=Sing	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-67	Superior	Superior	PROPN	_	Number=Sing	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+64	de	de	ADP	_	_	63	flat:name	O	_
+65	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	63	flat:name	O	_
+66	Cretáceo	Cretáceo	PROPN	_	Number=Sing	63	flat:name	B=UNIDADE_CRONOESTRATIGRÁFICA	_
+67	Superior	Superior	PROPN	_	Number=Sing	63	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA	_
 68	,	,	PUNCT	_	_	69	punct	O	_
-69	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+69	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	O	_
 70-71	do	_	_	_	_	_	_	_	_
-70	de	de	ADP	_	_	69	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-71	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	69	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-72	Eoceno	Eoceno	PROPN	_	Number=Sing	69	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+70	de	de	ADP	_	_	69	flat:name	O	_
+71	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	69	flat:name	O	_
+72	Eoceno	Eoceno	PROPN	_	Number=Sing	69	flat:name	B=UNIDADE_CRONOESTRATIGRÁFICA	_
 73	e	e	CCONJ	_	_	74	cc	O	_
-74	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	B=UNIDADE_CRONOESTRATIGRÁFICA|B=UNIDADE_LITOESTRATIGRÁFICA	_
+74	Topo	Topo	PROPN	_	Gender=Masc|Number=Sing	48	conj	O	_
 75-76	do	_	_	_	_	_	_	_	_
-75	de	de	ADP	_	_	74	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-76	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	74	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
-77	Mioceno	Mioceno	PROPN	_	Number=Sing	74	flat:name	I=UNIDADE_CRONOESTRATIGRÁFICA|I=UNIDADE_LITOESTRATIGRÁFICA	_
+75	de	de	ADP	_	_	74	flat:name	O	_
+76	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	74	flat:name	O	_
+77	Mioceno	Mioceno	PROPN	_	Number=Sing	74	flat:name	B=UNIDADE_CRONOESTRATIGRÁFICA	_
 78	)	)	PUNCT	_	_	48	punct	O	_
 79	.	.	PUNCT	_	_	15	punct	O	_
```

## correções de estrutura deposicional

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Dec 21 18:44:29 2021 -0300
* Lines changed: 60
* Commit: [95b5b95ca08122eabca00937a42210c4a1118278](https://github.com/alvelvis/meu-mestrado/commit/95b5b95ca08122eabca00937a42210c4a1118278)
* Patch file: [2021_12_21_18-44-29-95b5b95ca08122eabca00937a42210c4a1118278.patch](patch_changelog_sema/2021_12_21_18-44-29-95b5b95ca08122eabca00937a42210c4a1118278.patch)

correções de estrutura deposicional

```diff
 # text = Os fluxos das marés, quando canalizados, têm períodos distintos de águas estagnadas que resultam na deposição de finos.
 # sent_id = 284-20150917-MONOGRAFIA_0-232
 1	Os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	2	det	O	_
-2	fluxos	fluxo	NOUN	_	Gender=Masc|Number=Plur	10	nsubj	B=ESTRUTURA_DEPOSICIONAL	_
+2	fluxos	fluxo	NOUN	_	Gender=Masc|Number=Plur	10	nsubj	O	_
 3-4	das	_	_	_	_	_	_	_	_
 3	de	de	ADP	_	_	5	case	O	_
 4	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	5	det	O	_
```

## Modificações relacionadas a “ambiente”, “deposicional”, “sistemas (deposicionais)” e uma revisão geral dos elementos SD da planilha.

* Tatiana Cavalcanti
* Date:   Tue Jan 4 17:07:53 2022 -0300
* Lines changed: 105
* Commit: [ee6963ce7d15ddec121f49b3f1e77273985d578d](https://github.com/alvelvis/meu-mestrado/commit/ee6963ce7d15ddec121f49b3f1e77273985d578d)
* Patch file: [2022_1_4_17-07-53-ee6963ce7d15ddec121f49b3f1e77273985d578d.patch](patch_changelog_sema/2022_1_4_17-07-53-ee6963ce7d15ddec121f49b3f1e77273985d578d.patch)

Modificações relacionadas a “ambiente”, “deposicional”, “sistemas (deposicionais)” e uma revisão geral dos elementos SD da planilha.

```diff
 19	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	17	nmod	O	_
 20	geradas	gerar	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part	19	acl	O	_
 21	em	em	ADP	_	_	22	case	O	_
-22	ambientes	ambiente	NOUN	_	Gender=Masc|Number=Plur	20	obl	O	_
-23	tectônicos	tectônico	ADJ	_	Gender=Masc|Number=Plur	22	amod	B=SISTEMA_DEPOSICIONAL	_
+22	ambientes	ambiente	NOUN	_	Gender=Masc|Number=Plur	20	obl	B=SISTEMA_DEPOSICIONAL	_
+23	tectônicos	tectônico	ADJ	_	Gender=Masc|Number=Plur	22	amod	O	_
 24	distintos	distinto	ADJ	_	Gender=Masc|Number=Plur	22	amod	O	_
 25	,	,	PUNCT	_	_	26	punct	O	_
 26-27	tratando-se	_	_	_	_	_	_	_	_
```