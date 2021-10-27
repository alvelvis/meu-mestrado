# Changelog

Last update: 2021-10-27-16:41:12

## Figura, tabela, quadro etc.

* Aline Silveira
* Date:   Wed Aug 25 19:21:31 2021 -0300
* Lines changed: 928
* Patch file: [2021_8_25_19-21-31-8d418fdffb04a527db48464dad5aa1a3364b3c2f.patch](patch_changelog_dep/2021_8_25_19-21-31-8d418fdffb04a527db48464dad5aa1a3364b3c2f.patch)

Figura, tabela, quadro etc.
Se não forem flat:name, viram NOUN, com lema minúsculo, e são parataxis quando entre parênteses

```diff
 11	costa	costa	NOUN	_	Gender=Fem|Number=Sing	8	obl	B=UNIDADE_LITOESTRATIGRÁFICA	_
 12	brasileira	brasileiro	ADJ	_	Gender=Fem|Number=Sing	11	amod	O	_
 13	(	(	PUNCT	_	_	14	punct	O	_
-14	Figura	Figura	PROPN	_	Gender=Fem|Number=Sing	11	appos	O	_
+14	Figura	figura	NOUN	_	Gender=Fem|Number=Sing	8	parataxis	O	_
 15	1	1	NUM	_	NumType=Card	14	nummod	O	_
 16	)	)	PUNCT	_	_	14	punct	O	_
 17	e	e	CCONJ	_	_	18	cc	O	_
```

## regras para juntar os flat:name com gap

* Tatiana Cavalcanti
* Date:   Mon Aug 30 23:22:34 2021 -0300
* Lines changed: 520
* Patch file: [2021_8_30_23-22-34-c306455a1bc9030090c0fcf9bae663647ddf5699.patch](patch_changelog_dep/2021_8_30_23-22-34-c306455a1bc9030090c0fcf9bae663647ddf5699.patch)

regras para juntar os flat:name com gap

```diff
 15	doutorado	doutorado	NOUN	_	Gender=Masc|Number=Sing	13	nmod	O	_
 16	)	)	PUNCT	_	_	13	punct	O	_
 17	Villwock	Villwock	PROPN	_	Gender=Masc|Number=Sing	10	conj	O	_
-18	e	e	CCONJ	_	_	19	flat:name	O	_
+18	e	e	CCONJ	_	_	17	flat:name	O	_
 19	Tomazelli	Tomazelli	PROPN	_	Gender=Masc|Number=Sing	17	flat:name	O	_
-20	(	(	PUNCT	_	_	19	flat:name	O	_
-21	1995	1995	NUM	_	NumType=Card	19	flat:name	O	_
-22	)	)	PUNCT	_	_	13	punct	O	_
+20	(	(	PUNCT	_	_	21	punct	O	_
+21	1995	1995	NUM	_	NumType=Card	19	nmod:appos	O	_
+22	)	)	PUNCT	_	_	21	punct	O	_
 23	,	,	PUNCT	_	_	24	punct	O	_
 24	Bueno	Bueno	PROPN	_	Gender=Masc|Number=Sing	10	conj	O	_
 25	et	et	PROPN	_	Number=Sing	24	flat:name	O	_
```

## Adjetivação com gênero diferente

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Fri Sep 17 21:10:35 2021 -0300
* Lines changed: 242
* Patch file: [2021_9_17_21-10-35-d856a970ba91b276f62ab6990edb3d7810d4df8e.patch](patch_changelog_dep/2021_9_17_21-10-35-d856a970ba91b276f62ab6990edb3d7810d4df8e.patch)

Adjetivação com gênero diferente
Erros de validação corrigidos pela Cláudia

```diff
 23	atinge	atingir	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	21	acl:relcl	O	_
 24	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	25	det	O	_
 25	coberturas	cobertura	NOUN	_	Gender=Fem|Number=Plur	23	obj	O	_
-26	metassedimentares	metassedimentar	ADJ	_	Gender=Unsp|Number=Plur	25	amod	O	_
+26	metassedimentares	metassedimentar	ADJ	_	Gender=Fem|Number=Plur	25	amod	O	_
 27-28	meso-a	_	_	_	_	_	_	_	_
 27	meso	meso	NOUN	_	Gender=Masc|Number=Sing	26	nmod	O	_
 28	a	a	ADP	_	_	29	case	O	_
```

## Correções derivadas da busca por obj de não-verbo

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sat Sep 18 02:36:16 2021 -0300
* Lines changed: 375
* Patch file: [2021_9_18_02-36-16-98cce96cff4375f3660b117c32afb30f484b738b.patch](patch_changelog_dep/2021_9_18_02-36-16-98cce96cff4375f3660b117c32afb30f484b738b.patch)

Correções derivadas da busca por obj de não-verbo

```diff
 25	coberturas	cobertura	NOUN	_	Gender=Fem|Number=Plur	23	obj	O	_
 26	metassedimentares	metassedimentar	ADJ	_	Gender=Unsp|Number=Plur	25	amod	O	_
 27-28	meso-a	_	_	_	_	_	_	_	_
-27	meso	meso	NOUN	_	Gender=Masc|Number=Sing	26	nmod	O	_
+27	meso	meso	NOUN	_	Gender=Masc|Number=Sing	26	obl	O	_
 28	a	a	ADP	_	_	29	case	O	_
 29	neoproterozóicas	neoproterozóico	ADJ	_	Gender=Fem|Number=Plur	27	nmod	B=GEOCRONOLOGIA	_
 30	,	,	PUNCT	_	_	31	punct	O	_
```

## Números em título de seção

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Sep 21 09:41:19 2021 -0300
* Lines changed: 612
* Patch file: [2021_9_21_09-41-19-41775229e2aa5e0a0fb68c99f2e17a5810583722.patch](patch_changelog_dep/2021_9_21_09-41-19-41775229e2aa5e0a0fb68c99f2e17a5810583722.patch)

Números em título de seção

```diff
 # text = 1. - INTRODUÇÃO
 # sent_id = 247-20140910-MONOGRAFIA_0-1
-1	1	1	NUM	_	NumType=Card	4	parataxis	O	_
-2	.	.	PUNCT	_	_	4	punct	O	_
+1	1	1	NUM	_	NumType=Card	4	nummod	O	_
+2	.	.	PUNCT	_	_	1	punct	O	_
 3	-	-	PUNCT	_	_	4	punct	O	_
 4	INTRODUÇÃO	introdução	NOUN	_	Gender=Fem|Number=Sing	0	root	O	_
```

## 'ocorrer' não deve ter objeto

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Sep 23 15:06:45 2021 -0300
* Lines changed: 112
* Patch file: [2021_9_23_15-06-45-8b98a96c5d4e804102e3353e3ce92f0332d5fe20.patch](patch_changelog_dep/2021_9_23_15-06-45-8b98a96c5d4e804102e3353e3ce92f0332d5fe20.patch)

'ocorrer' não deve ter objeto

```diff
 7	,	,	PUNCT	_	_	3	punct	O	_
 8	ocorre	ocorrer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
 9	marcante	marcante	ADJ	_	Gender=Fem|Number=Sing	10	amod	O	_
-10	aloctonia	aloctonia	NOUN	_	Gender=Fem|Number=Sing	8	obj	O	_
+10	aloctonia	aloctonia	NOUN	_	Gender=Fem|Number=Sing	8	nsubj	O	_
 11	e	e	CCONJ	_	_	13	cc	O	_
 12	elevado	elevado	ADJ	_	Gender=Masc|Number=Sing	13	amod	O	_
 13	grau	grau	NOUN	_	Gender=Masc|Number=Sing	10	conj	O	_
```

## Sujeito vira objeto nos casos de SE indeterminado

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Sep 23 20:49:56 2021 -0300
* Lines changed: 453
* Patch file: [2021_9_23_20-49-56-f96eab90d05d8c518a6230b3436bb495d898302b.patch](patch_changelog_dep/2021_9_23_20-49-56-f96eab90d05d8c518a6230b3436bb495d898302b.patch)

Sujeito vira objeto nos casos de SE indeterminado
Voz passiva sintética também foi modificada, e o "SE" recebeu a etiqueta expl:impers

```diff
 18	Rifte	Rifte	PROPN	_	Number=Sing	15	flat:name	O	_
 19-20	observou-se	_	_	_	_	_	_	_	_
 19	observou	observar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	O	_
-20	se	se	PRON	_	Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs	19	expl	O	_
+20	se	se	PRON	_	Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs	19	expl:impers	O	_
 21	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	22	det	O	_
-22	presença	presença	NOUN	_	Gender=Fem|Number=Sing	19	nsubj	O	_
+22	presença	presença	NOUN	_	Gender=Fem|Number=Sing	19	obj	O	_
 23	de	de	ADP	_	_	25	case	O	_
 24	um	um	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	25	det	O	_
 25	adensamento	adensamento	NOUN	_	Gender=Masc|Number=Sing	22	nmod	O	_
```

## Uniformização de nominais

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Sep 23 21:03:40 2021 -0300
* Lines changed: 264
* Patch file: [2021_9_23_21-03-40-48004c2867aaff9e1add51f9bdd2ba789bad46d3.patch](patch_changelog_dep/2021_9_23_21-03-40-48004c2867aaff9e1add51f9bdd2ba789bad46d3.patch)

Uniformização de nominais

```diff
 # sent_id = 247-20140910-MONOGRAFIA_0-129
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
 2	seção	seção	NOUN	_	Gender=Fem|Number=Sing	4	nsubj	O	_
-3	pós-rifte	pós-rifte	ADJ	_	Gender=Fem|Number=Sing	2	amod	O	_
+3	pós-rifte	pós-rifte	NOUN	_	Gender=Masc|Number=Sing	2	nmod	O	_
 4	apresenta	apresentar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
 5	estruturação	estruturação	NOUN	_	Gender=Fem|Number=Sing	4	obj	O	_
 6	incipiente	incipiente	ADJ	_	Gender=Fem|Number=Sing	5	amod	O	_
```

## Alguns deprel não podem ter filho

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Sep 15 21:21:06 2021 -0300
* Lines changed: 695
* Patch file: [2021_9_15_21-21-06-39825cc98f1d855a00a21ded5a52d21708dc9fdf.patch](patch_changelog_dep/2021_9_15_21-21-06-39825cc98f1d855a00a21ded5a52d21708dc9fdf.patch)

Alguns deprel não podem ter filho
compound flat:name fixed punct aux cop
Organização de feats por ordem alfabética

```diff
 # sent_id = 247-20140910-MONOGRAFIA_0-16
 1	A	a	ADP	_	_	5	obl	O	MWEPOS=ADV
 2	seguir	seguir	VERB	_	VerbForm=Inf	1	fixed	O	_
-3	,	,	PUNCT	_	_	2	punct	O	_
+3	,	,	PUNCT	_	_	1	punct	O	_
 4	são	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	5	aux:pass	O	_
 5	apresentadas	apresentar	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass	0	root	O	_
 6	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	7	det	O	_
```

## Correções derivadas de n-grams inconsistentes

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Fri Oct 1 10:32:17 2021 -0300
* Lines changed: 86
* Patch file: [2021_10_1_10-32-17-aec3cdbf6502b1c114db9587bed2002c059cbdfb.patch](patch_changelog_dep/2021_10_1_10-32-17-aec3cdbf6502b1c114db9587bed2002c059cbdfb.patch)

Correções derivadas de n-grams inconsistentes

```diff
 3	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	4	cop	O	_
 4	responsável	responsável	ADJ	_	Gender=Fem|Number=Sing	0	root	O	_
 5	por	por	SCONJ	_	_	6	mark	O	_
-6	separar	separar	VERB	_	VerbForm=Inf	4	advcl	O	_
+6	separar	separar	VERB	_	VerbForm=Inf	4	acl	O	_
 7	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	8	det	O	_
 8	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	6	obj	O	_
 9	de	de	ADP	_	_	10	case	O	_
```

## Correção de formas participiais

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Fri Oct 8 22:09:28 2021 -0300
* Lines changed: 1246
* Patch file: [2021_10_8_22-09-28-4c643837ad26325c9a56be001195613789872fc8.patch](patch_changelog_dep/2021_10_8_22-09-28-4c643837ad26325c9a56be001195613789872fc8.patch)

Correção de formas participiais

```diff
 49	estes	este	DET	_	Gender=Masc|Number=Plur|PronType=Dem	52	det	O	_
 50	278	278	NUM	_	NumType=Card	52	nummod	O	_
 51	048	048	NUM	_	NumType=Card	52	nummod	O	_
-52	Km²	Km²	PROPN	_	Gender=Masc|Number=Plur	54	nsubj	O	_
-53	estão	estar	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	54	cop	O	_
-54	localizados	localizar	ADJ	_	Gender=Masc|Number=Plur	40	advcl	O	_
+52	Km²	Km²	PROPN	_	Gender=Masc|Number=Plur	54	nsubj:pass	O	_
+53	estão	estar	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	54	aux:pass	O	_
+54	localizados	localizar	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part|Voice=Pass	40	advcl	O	_
 55-56	na	_	_	_	_	_	_	_	_
 55	em	em	ADP	_	_	57	case	O	_
 56	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	57	det	O	_
```

## Referências como nmod:appos

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Fri Oct 8 22:13:49 2021 -0300
* Lines changed: 60
* Patch file: [2021_10_8_22-13-49-3e3e48ea493b7aeea4db59da4abf09577e11859d.patch](patch_changelog_dep/2021_10_8_22-13-49-3e3e48ea493b7aeea4db59da4abf09577e11859d.patch)

Referências como nmod:appos

```diff
 4	Luiz	Luiz	PROPN	_	Gender=Masc|Number=Sing	20	obl	O	_
 5	&	&	PROPN	_	Number=Sing	4	flat:name	O	_
 6	Silva	Silva	PROPN	_	Number=Sing	4	flat:name	O	_
-7	(	(	PUNCT	_	_	4	flat:name	O	_
-8	1995	1995	NUM	_	NumType=Card	4	flat:name	O	_
-9	)	)	PUNCT	_	_	4	flat:name	O	_
+7	(	(	PUNCT	_	_	8	punct	O	_
+8	1995	1995	NUM	_	NumType=Card	4	nmod:appos	O	_
+9	)	)	PUNCT	_	_	8	punct	O	_
 10	,	,	PUNCT	_	_	4	punct	O	_
 11	frequentemente	frequentemente	ADV	_	_	20	advmod	O	_
 12	os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	13	det	O	_
```

## ADJ não tem filhos determinantes

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Oct 19 14:23:56 2021 -0300
* Lines changed: 25
* Patch file: [2021_10_19_14-23-56-31da4f425f0280b4347e5245c432956ee9b2f8d0.patch](patch_changelog_dep/2021_10_19_14-23-56-31da4f425f0280b4347e5245c432956ee9b2f8d0.patch)

ADJ não tem filhos determinantes

```diff
 16	de	de	ADP	_	_	17	case	O	_
 17	etileno	etileno	NOUN	_	Gender=Masc|Number=Sing	15	nmod	O	_
 18	sobre	sobre	ADP	_	_	21	case	O	_
-19	um	um	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	21	det	O	_
+19	um	um	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	20	det	O	_
 20	composto	composto	NOUN	_	Gender=Masc|Number=Sing	7	obl	O	_
 21	lipófilo	lipófilo	ADJ	_	Gender=Masc|Number=Sing	20	amod	O	_
 22	com	com	ADP	_	_	23	case	O	_
```

## correções de frases com 'colocar'

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Oct 19 14:27:39 2021 -0300
* Lines changed: 5
* Patch file: [2021_10_19_14-27-39-44088d4fc25dc0c6252bbd65408d38d38795a22f.patch](patch_changelog_dep/2021_10_19_14-27-39-44088d4fc25dc0c6252bbd65408d38d38795a22f.patch)

correções de frases com 'colocar'

```diff
 18	que	que	PRON	_	Gender=Masc|Number=Plur|PronType=Rel	21	nsubj	O	_
 19	são	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	21	cop	O	_
 20	,	,	PUNCT	_	_	21	punct	O	_
-21	sólidos	sólido	ADJ	_	Gender=Masc|Number=Plur	17	amod	O	_
+21	sólidos	sólido	ADJ	_	Gender=Masc|Number=Plur	13	acl:relcl	O	_
 22-23	na	_	_	_	_	_	_	_	_
 22	em	em	ADP	_	_	24	case	O	_
 23	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	24	det	O	_
 24	superfície	superfície	NOUN	_	Gender=Fem|Number=Sing	21	obl	O	_
 25-26	dos	_	_	_	_	_	_	_	_
 25	de	de	ADP	_	_	27	case	O	_
-26	os	o	DET	_	Gender=Masc|Number=Plur|PronType=Art	27	det	O	_
-27	quais	qual	PRON	_	Gender=Masc|Number=Plur|PronType=Rel	24	nmod	O	_
-28	se	se	PRON	_	Case=Acc|Gender=Masc|Number=Plur|Person=3|PronType=Prs	29	expl	O	_
+26	os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	27	det	O	_
+27	quais	qual	PRON	_	Gender=Masc|Number=Plur|PronType=Rel	29	obl	O	_
+28	se	se	PRON	_	_	29	expl	O	_
 29	colocam	colocar	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	24	acl:relcl	O	_
-30	complexos	complexo	ADJ	_	Gender=Masc|Number=Plur	29	xcomp	O	_
+30	complexos	complexo	NOUN	_	Gender=Masc|Number=Plur	29	obj	O	_
 31	de	de	ADP	_	_	32	case	O	_
 32	coordenação	coordenação	NOUN	_	Gender=Fem|Number=Sing	30	obl	O	_
 33	,	,	PUNCT	_	_	34	punct	O	_
```

## Correções de flat:name com semas estranhos

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Oct 20 17:28:02 2021 -0300
* Lines changed: 226
* Patch file: [2021_10_20_17-28-02-1ef93eb8496c7ffb4d3fc526dcb7754e79d876b9.patch](patch_changelog_dep/2021_10_20_17-28-02-1ef93eb8496c7ffb4d3fc526dcb7754e79d876b9.patch)

Correções de flat:name com semas estranhos

```diff
 3	:	:	PUNCT	_	_	4	punct	O	_
 4	Localização	Localização	PROPN	_	Gender=Fem|Number=Sing	1	parataxis	O	_
 5-6	da	_	_	_	_	_	_	_	_
-5	de	de	ADP	_	_	4	flat:name	O	_
-6	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	flat:name	O	_
-7	Bacia	Bacia	PROPN	_	Number=Sing	4	flat:name	B=BACIA	_
-8	de	de	ADP	_	_	4	flat:name	O	_
-9	Pelotas	Pelotas	PROPN	_	Number=Sing	4	flat:name	B=BACIA	_
+5	de	de	ADP	_	_	7	case	O	_
+6	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	7	det	O	_
+7	Bacia	Bacia	PROPN	_	Number=Sing	4	nmod	B=BACIA	_
+8	de	de	ADP	_	_	7	flat:name	I=BACIA	_
+9	Pelotas	Pelotas	PROPN	_	Number=Sing	7	flat:name	I=BACIA	_
 # text = 2. - OBJETIVOS
 # sent_id = 247-20140910-MONOGRAFIA_0-8
```

## Correções derivadas de n-grams

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Oct 20 21:48:28 2021 -0300
* Lines changed: 201
* Patch file: [2021_10_20_21-48-28-a71fa53e1a5f261d9514193621cc8f7a4246b38d.patch](patch_changelog_dep/2021_10_20_21-48-28-a71fa53e1a5f261d9514193621cc8f7a4246b38d.patch)

Correções derivadas de n-grams

```diff
 # text = 4-METODOLOGIA EXPERIMENTAL
 # sent_id = 241-20140227-MONOGRAFIA_0-118
-1	4-METODOLOGIA	4-metodologia	NOUN	_	Gender=Masc|Number=Sing	0	root	O	_
-2	EXPERIMENTAL	EXPERIMENTAL	PROPN	_	Number=Sing	1	flat:name	O	_
+1	4-METODOLOGIA	4-metodologia	NOUN	_	Gender=Fem|Number=Sing	0	root	O	tokenização
+2	EXPERIMENTAL	experimental	ADJ	_	Gender=Fem|Number=Sing	1	amod	O	_
 # text = Nesta seção, será descrita a metodologia utilizada para a obtenção das emulsões asfálticas convencionais e modificadas com nanomateriais, constituintes dessas emulsões, equipamentos necessários para obtenção e metodologia de caracterização das mesmas.
 # sent_id = 241-20140227-MONOGRAFIA_0-119
```

## mwe por_causa_de

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Oct 20 23:10:26 2021 -0300
* Lines changed: 71
* Patch file: [2021_10_20_23-10-26-907bd8463bd62a3f6a445f52f9e27db3f1e63f50.patch](patch_changelog_dep/2021_10_20_23-10-26-907bd8463bd62a3f6a445f52f9e27db3f1e63f50.patch)

mwe por_causa_de

```diff
 25	asfalto	asfalto	NOUN	_	Gender=Masc|Number=Sing	21	nmod	O	_
 26	recuperado	recuperar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	25	acl	O	_
 27	,	,	PUNCT	_	_	30	punct	O	_
-28	tendo	ter	AUX	_	VerbForm=Ger	30	aux	O	_
-29	em	em	ADP	_	_	30	mark	O	_
-30	vista	ver	VERB	_	VerbForm=Part	19	advcl	O	_
-31	variações	variação	NOUN	_	Gender=Fem|Number=Plur	30	obj	O	_
+28	tendo	ter	AUX	_	VerbForm=Ger	31	case	O	MWEPOS=ADP
+29	em	em	ADP	_	_	28	fixed	O	_
+30	vista	ver	VERB	_	VerbForm=Part	28	fixed	O	_
+31	variações	variação	NOUN	_	Gender=Fem|Number=Plur	19	obl	O	_
 32-33	na	_	_	_	_	_	_	_	_
 32	em	em	ADP	_	_	34	case	O	_
 33	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	34	det	O	_
```

## Modificações de listas

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Oct 21 20:02:00 2021 -0300
* Lines changed: 140
* Patch file: [2021_10_21_20-02-00-b169f9d843aee1d54fb4a23a8870d7c8cdf817af.patch](patch_changelog_dep/2021_10_21_20-02-00-b169f9d843aee1d54fb4a23a8870d7c8cdf817af.patch)

Modificações de listas
Foram aplicadas 2 regras. A primeira modifica os casos de letras entre parênteses, especificamente seu deprel, dephead, lema, pos e features. A segunda regra é relativa aos números que iniciam sentenças e modifica seu deprel e dephead.

```diff
 # text = 1. - INTRODUÇÃO
 # sent_id = 247-20140910-MONOGRAFIA_0-1
-1	1	1	NUM	_	NumType=Card	4	parataxis	O	_
-2	.	.	PUNCT	_	_	4	punct	O	_
+1	1	1	NUM	_	NumType=Card	4	nummod	O	_
+2	.	.	PUNCT	_	_	1	punct	O	_
 3	-	-	PUNCT	_	_	4	punct	O	_
 4	INTRODUÇÃO	introdução	NOUN	_	Gender=Fem|Number=Sing	0	root	O	_
```

## Lema de superior

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sat Oct 23 03:02:49 2021 -0300
* Lines changed: 80
* Patch file: [2021_10_23_03-02-49-14edfcfbf766a231a0dc31f58454bbff6069484c.patch](patch_changelog_dep/2021_10_23_03-02-49-14edfcfbf766a231a0dc31f58454bbff6069484c.patch)

Lema de superior

```diff
 27	de	de	ADP	_	_	26	flat:name	I=BACIA	_
 28	Pelotas	Pelotas	PROPN	_	Number=Sing	26	flat:name	I=BACIA	_
 29	verificando	verificar	VERB	_	VerbForm=Ger	5	advcl	O	_
-30	se	se	PRON	_	Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs	31	expl	O	_
+30	se	se	SCONJ	_	_	31	mark	O	_
 31	há	haver	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	29	ccomp	O	_
 32	correspondência	correspondência	NOUN	_	Gender=Fem|Number=Sing	31	obj	O	_
 33	entre	entre	ADP	_	_	35	case	O	_
```

## Correções de ciclo

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sat Oct 23 03:40:54 2021 -0300
* Lines changed: 328
* Patch file: [2021_10_23_03-40-54-0c62b58aa7a67304fdd753c37bfe2f1d8b398971.patch](patch_changelog_dep/2021_10_23_03-40-54-0c62b58aa7a67304fdd753c37bfe2f1d8b398971.patch)

Correções de ciclo

```diff
 2	floco	floco	NOUN	_	Gender=Masc|Number=Sing	4	nsubj	O	_
 3	expandido	expander	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	2	acl	O	_
 4	aprisiona	aprisionar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
-5-6	consigo	_	_	_	_	0	_	_	_
+5-6	consigo	_	_	_	_	_	_	_	_
 5	com	com	ADP	_	_	6	case	O	_
 6	si	ele	PRON	_	Gender=Masc|Number=Sing|Person=3|PronType=Prs	4	obl	O	_
 7	células	célula	NOUN	_	Gender=Fem|Number=Plur	4	obj	O	_
```

## Correções de lema verbal

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sat Oct 23 05:15:15 2021 -0300
* Lines changed: 592
* Patch file: [2021_10_23_05-15-15-a1723d1e3e4c4e70df98c71823f88e35d4b852b6.patch](patch_changelog_dep/2021_10_23_05-15-15-a1723d1e3e4c4e70df98c71823f88e35d4b852b6.patch)

Correções de lema verbal

```diff
 34	brasileiras	brasileiro	ADJ	_	Gender=Fem|Number=Plur	30	amod	O	_
 35	.	.	PUNCT	_	_	8	punct	O	_
-# text = Deste modo o trabalho busca descrever e caracterizar estruturas geológicas na porção continental e da região offshore correspondente ao norte da Bacia de Pelotas verificando se há correspondência entre as estruturas geológicas caracterizadas na porção continental e offshore.
-# sent_id = 247-20140910-MONOGRAFIA_0-3
-1	Deste	destar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
-2	modo	modo	NOUN	_	Gender=Masc|Number=Sing	1	obj	O	_
-3	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	4	det	O	_
-4	trabalho	trabalho	NOUN	_	Gender=Masc|Number=Sing	5	nsubj	O	_
-5	busca	buscar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	1	ccomp	O	_
-6	descrever	descrever	VERB	_	VerbForm=Inf	5	xcomp	O	_
-7	e	e	CCONJ	_	_	8	cc	O	_
-8	caracterizar	caracterizar	VERB	_	VerbForm=Inf	6	conj	O	_
-9	estruturas	estrutura	NOUN	_	Gender=Fem|Number=Plur	8	obj	O	_
-10	geológicas	geológico	ADJ	_	Gender=Fem|Number=Plur	9	amod	O	_
-11-12	na	_	_	_	_	_	_	_	_
-11	em	em	ADP	_	_	13	case	O	_
-12	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	13	det	O	_
-13	porção	porção	NOUN	_	Gender=Fem|Number=Sing	9	nmod	O	_
-14	continental	continental	ADJ	_	Gender=Fem|Number=Sing	13	amod	O	_
-15	e	e	CCONJ	_	_	18	cc	O	_
-16-17	da	_	_	_	_	_	_	_	_
-16	de	de	ADP	_	_	18	case	O	_
-17	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	18	det	O	_
-18	região	região	NOUN	_	Gender=Fem|Number=Sing	13	conj	O	_
-19	offshore	offshore	ADJ	_	Gender=Fem|Number=Sing	18	amod	O	_
-20	correspondente	correspondente	ADJ	_	Gender=Fem|Number=Sing	18	amod	O	_
-21-22	ao	_	_	_	_	_	_	_	_
-21	a	a	ADP	_	_	23	case	O	_
-22	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	23	det	O	_
-23	norte	norte	NOUN	_	Gender=Masc|Number=Sing	20	obl	O	_
-24-25	da	_	_	_	_	_	_	_	_
-24	de	de	ADP	_	_	26	case	O	_
-25	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	26	det	O	_
-26	Bacia	Bacia	PROPN	_	Gender=Fem|Number=Sing	23	nmod	B=BACIA	_
-27	de	de	ADP	_	_	26	flat:name	I=BACIA	_
-28	Pelotas	Pelotas	PROPN	_	Number=Sing	26	flat:name	I=BACIA	_
-29	verificando	verificar	VERB	_	VerbForm=Ger	5	advcl	O	_
-30	se	se	SCONJ	_	_	31	mark	O	_
-31	há	haver	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	29	ccomp	O	_
-32	correspondência	correspondência	NOUN	_	Gender=Fem|Number=Sing	31	obj	O	_
-33	entre	entre	ADP	_	_	35	case	O	_
-34	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	35	det	O	_
-35	estruturas	estrutura	NOUN	_	Gender=Fem|Number=Plur	32	nmod	O	_
-36	geológicas	geológico	ADJ	_	Gender=Fem|Number=Plur	35	amod	O	_
-37	caracterizadas	caracterizar	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part	35	acl	O	_
-38-39	na	_	_	_	_	_	_	_	_
-38	em	em	ADP	_	_	40	case	O	_
-39	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	40	det	O	_
-40	porção	porção	NOUN	_	Gender=Fem|Number=Sing	37	obl	O	_
-41	continental	continental	ADJ	_	Gender=Fem|Number=Sing	40	amod	O	_
-42	e	e	CCONJ	_	_	43	cc	O	_
-43	offshore	offshore	ADJ	_	Gender=Fem|Number=Sing	41	conj	O	_
-44	.	.	PUNCT	_	_	1	punct	O	_
-
 # text = A caracterização estrutural para a porção norte da Bacia de Pelotas foi realizada através de 17 seções sísmicas, onde foram caracterizadas falhas normais, em padrão dominó, falhas sintéticas e antitéticas e lístricas, além da identificação de estruturas como o Arco de Torres (Fonseca 2006), (Alves 1981) a Plataforma de Florianópolis individualizada por Gonçalves et al. (1979), Zona de Falha do Rio Grande (Miranda 1970), (Kowsmann 1974).
 # sent_id = 247-20140910-MONOGRAFIA_0-4
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
```