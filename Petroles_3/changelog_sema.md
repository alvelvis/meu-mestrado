# Changelog

Last update: 2021-9-2-11:49:52

## Regras para B=CAMPO

* Aline Silveira
* Date:   Wed Aug 18 19:22:06 2021 -0300
* Lines changed: 99
* Commit: [226aa79550f0842f205240d0c43935cfd428d81f](https://github.com/alvelvis/meu-mestrado/commit/226aa79550f0842f205240d0c43935cfd428d81f)
* Patch file: [2021_8_18_19:22:06-226aa79550f0842f205240d0c43935cfd428d81f.patch](patch_changelog_sema/2021_8_18_19:22:06-226aa79550f0842f205240d0c43935cfd428d81f.patch)

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
* Patch file: [2021_8_18_19:23:20-8559b82e8dbfcce0a511e5435f089b9cbf462a15.patch](patch_changelog_sema/2021_8_18_19:23:20-8559b82e8dbfcce0a511e5435f089b9cbf462a15.patch)

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
* Patch file: [2021_8_19_11:40:12-b4ce4f35cba57636d3e032f30cc8e865b2b099ad.patch](patch_changelog_sema/2021_8_19_11:40:12-b4ce4f35cba57636d3e032f30cc8e865b2b099ad.patch)

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
* Patch file: [2021_8_25_19:23:23-4a4aa82216f1d360758dd3bce77553100e0de996.patch](patch_changelog_sema/2021_8_25_19:23:23-4a4aa82216f1d360758dd3bce77553100e0de996.patch)

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
* Patch file: [2021_9_1_00:09:42-b3cfec4aea74f99aeb4b4758c42ed5850af40a2c.patch](patch_changelog_sema/2021_9_1_00:09:42-b3cfec4aea74f99aeb4b4758c42ed5850af40a2c.patch)

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