# Changelog

Last update: 2021-8-13-8:54:17

## lemma 'diferentes' is not correct

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu May 13 01:22:25 2021 -0300
* Lines changed: 117
* Commit: [7ad921ca7b0026a8d96285f76a37097fbc5d7dda](https://github.com/alvelvis/meu-mestrado/commit/7ad921ca7b0026a8d96285f76a37097fbc5d7dda)
* Patch file: [2021_5_13_01:22:25-7ad921ca7b0026a8d96285f76a37097fbc5d7dda.patch](patch/2021_5_13_01:22:25-7ad921ca7b0026a8d96285f76a37097fbc5d7dda.patch)

lemma 'diferentes' is not correct

```diff
 5	dados	dado	NOUN	_	Gender=Masc|Number=Plur	4	obj	O	_
 6	sobre	sobre	ADP	_	_	9	case	O	_
 7	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	9	det	O	_
-8	diferentes	diferentes	DET	_	Gender=Fem|Number=Plur|PronType=Ind	9	det	O	_
+8	diferentes	diferente	DET	_	Gender=Fem|Number=Plur|PronType=Ind	9	det	O	_
 9	distribuições	distribuição	NOUN	_	Gender=Fem|Number=Plur	4	obl	O	_
 10	de	de	ADP	_	_	11	case	O	_
 11	densidade	densidade	NOUN	_	Gender=Fem|Number=Sing	9	nmod	O	_
```

## lemmas cannot be fem plur

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu May 13 01:41:07 2021 -0300
* Lines changed: 164
* Commit: [3983c05dde4b414d6a7b400afeb89ad2a9e63603](https://github.com/alvelvis/meu-mestrado/commit/3983c05dde4b414d6a7b400afeb89ad2a9e63603)
* Patch file: [2021_5_13_01:41:07-3983c05dde4b414d6a7b400afeb89ad2a9e63603.patch](patch/2021_5_13_01:41:07-3983c05dde4b414d6a7b400afeb89ad2a9e63603.patch)

lemmas cannot be fem plur

```diff
 23	alinhamentos	alinhamento	NOUN	_	Gender=Masc|Number=Plur	15	conj	O	_
 24	estruturais	estrutural	ADJ	_	Gender=Masc|Number=Plur	23	amod	O	_
 25	e	e	CCONJ	_	_	28	cc	O	_
-26	várias	várias	DET	_	Gender=Fem|Number=Plur|PronType=Ind	28	det	O	_
+26	várias	vário	DET	_	Gender=Fem|Number=Plur|PronType=Ind	28	det	O	_
 27	outras	outro	DET	_	Gender=Fem|Number=Plur|PronType=Ind	28	det	O	_
 28	propriedades	propriedade	NOUN	_	Gender=Fem|Number=Plur	15	conj	O	_
 29-30	do	_	_	_	_	_	_	O	_
```

## det filho de nummod -- erro?

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu May 13 02:06:45 2021 -0300
* Lines changed: 22
* Commit: [cada8310640e99453c71506dac6c337a584fd1f5](https://github.com/alvelvis/meu-mestrado/commit/cada8310640e99453c71506dac6c337a584fd1f5)
* Patch file: [2021_5_13_02:06:45-cada8310640e99453c71506dac6c337a584fd1f5.patch](patch/2021_5_13_02:06:45-cada8310640e99453c71506dac6c337a584fd1f5.patch)

det filho de nummod -- erro?

```diff
 47	,	,	PUNCT	_	_	40	punct	O	_
 48-49	destes	_	_	_	_	_	_	O	_
 48	de	de	ADP	_	_	50	case	O	_
-49	estes	este	DET	_	Gender=Masc|Number=Plur|PronType=Dem	50	det	O	_
+49	estes	este	DET	_	Gender=Masc|Number=Plur|PronType=Dem	52	det	O	_
 50	278	278	NUM	_	NumType=Card	52	nummod	O	_
 51	048	048	NUM	_	NumType=Card	52	nummod	O	_
 52	Km²	Km²	PROPN	_	Gender=Masc|Number=Plur	54	nsubj	O	_
```

## fix det and its head gender and number

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu May 13 03:09:43 2021 -0300
* Lines changed: 8
* Commit: [53d707a5cf2507383795458666e33450730e6012](https://github.com/alvelvis/meu-mestrado/commit/53d707a5cf2507383795458666e33450730e6012)
* Patch file: [2021_5_13_03:09:43-53d707a5cf2507383795458666e33450730e6012.patch](patch/2021_5_13_03:09:43-53d707a5cf2507383795458666e33450730e6012.patch)

fix det and its head gender and number

```diff
 3-4	do	_	_	_	_	_	_	O	_
 3	de	de	ADP	_	_	5	case	O	_
 4	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	5	det	O	_
-5	Paraná	Paraná	PROPN	_	Number=Sing	2	nmod	B=BACIA	_
+5	Paraná	Paraná	PROPN	_	Gender=Masc|Number=Sing	2	nmod	B=BACIA	_
 # text = A Bacia Sedimentar do Paraná (Figura 6) se localiza no Continente Sul-Americano nas porções territoriais do Brasil meridional, Paraguai oriental, nordeste da Argentina e norte do Uruguai, totalizando uma área próxima de 1,5 milhão de quilômetros quadrados..
 # sent_id = 247-20140910-MONOGRAFIA_0-82
```

## "um de" indicates PRON PronType=Ind

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu May 13 06:35:52 2021 -0300
* Lines changed: 132
* Commit: [b7f3d42913ca7db33f3c2927609ba56ecc3efa5c](https://github.com/alvelvis/meu-mestrado/commit/b7f3d42913ca7db33f3c2927609ba56ecc3efa5c)
* Patch file: [2021_5_13_06:35:52-b7f3d42913ca7db33f3c2927609ba56ecc3efa5c.patch](patch/2021_5_13_06:35:52-b7f3d42913ca7db33f3c2927609ba56ecc3efa5c.patch)

"um de" indicates PRON PronType=Ind

```diff
 27	Província	Província	PROPN	_	Gender=Fem|Number=Sing	22	nmod	O	_
 28	Mantiqueira	Mantiqueira	PROPN	_	Number=Sing	27	flat:name	O	_
 29	e	e	CCONJ	_	_	30	cc	O	_
-30	um	um	NUM	_	NumType=Card	27	conj	O	_
+30	um	um	PRON	_	Gender=Masc|Number=Sing|PronType=Ind	22	conj	O	_
 31-32	dos	_	_	_	_	_	_	O	_
 31	de	de	ADP	_	_	34	case	O	_
 32	os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	34	det	O	_
```

## visto que, já que

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Mon May 17 00:41:34 2021 -0300
* Lines changed: 222
* Commit: [725b3da4d82a47ed5757524c3bb8fd4d2048b127](https://github.com/alvelvis/meu-mestrado/commit/725b3da4d82a47ed5757524c3bb8fd4d2048b127)
* Patch file: [2021_5_17_00:41:34-725b3da4d82a47ed5757524c3bb8fd4d2048b127.patch](patch/2021_5_17_00:41:34-725b3da4d82a47ed5757524c3bb8fd4d2048b127.patch)

visto que, já que

```diff
 15	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	16	det	O	_
 16	geólogo	geólogo	NOUN	_	Gender=Masc|Number=Sing	8	obl	O	_
 17	,	,	PUNCT	_	_	8	punct	O	_
-18	já	já	SCONJ	_	_	20	mark	O	_
+18	já	já	ADV	_	_	20	mark	O	MWEPOS=SCONJ
 19	que	que	SCONJ	_	_	18	fixed	O	_
 20	proporciona	proporcionar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	6	advcl	O	_
 21	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	22	det	O	_
```

## abservar is not a word

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Mon May 17 03:45:07 2021 -0300
* Lines changed: 45
* Commit: [ad450c4185a5c03beff93a817b997a7963165059](https://github.com/alvelvis/meu-mestrado/commit/ad450c4185a5c03beff93a817b997a7963165059)
* Patch file: [2021_5_17_03:45:07-ad450c4185a5c03beff93a817b997a7963165059.patch](patch/2021_5_17_03:45:07-ad450c4185a5c03beff93a817b997a7963165059.patch)

abservar is not a word

```diff
 # text = Observa-se que as emulsões asfálticas modificadas com vermiculita não apresentaram partículas retidas na peneira ASTM 20, mostrando a eficiência do processo de moagem realizado no moinho coloidal durante a obtenção da emulsão asfáltica..
 # sent_id = 241-20140227-MONOGRAFIA_0-208
 1-2	Observa-se	_	_	_	_	_	_	O	_
-1	Abserva	abservar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
+1	Observa	observar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
 2	se	se	PRON	_	Case=Acc|Gender=Unsp|PronType=Prs	1	nsubj	O	_
 3	que	que	SCONJ	_	_	11	mark	O	_
 4	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	5	det	O	_
```

## a_partir_de MWEPOS=ADP, partir VERB

* Maria Clara Castro
* Date:   Mon May 17 23:24:14 2021 -0300
* Lines changed: 481
* Commit: [fd9f01fe910ed8a9b7d23f66181b65939a961906](https://github.com/alvelvis/meu-mestrado/commit/fd9f01fe910ed8a9b7d23f66181b65939a961906)
* Patch file: [2021_5_17_23:24:14-fd9f01fe910ed8a9b7d23f66181b65939a961906.patch](patch/2021_5_17_23:24:14-fd9f01fe910ed8a9b7d23f66181b65939a961906.patch)

a_partir_de MWEPOS=ADP, partir VERB

```diff
 2	caracterização	caracterização	NOUN	_	Gender=Fem|Number=Sing	4	nsubj:pass	O	_
 3	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	4	aux:pass	O	_
 4	realizada	realizar	VERB	_	Gender=Fem|Number=Sing|VerbForm=Part|Voice=Pass	0	root	O	_
-5	a	a	ADP	_	_	9	case	O	_
+5	a	a	ADP	_	_	9	case	O	MWEPOS=ADP
 6	partir	partir	VERB	_	VerbForm=Inf	5	fixed	O	_
 7-8	da	_	_	_	_	_	_	O	_
 7	de	de	ADP	_	_	5	fixed	O	_
```

## fácies as NOUN, lemma fácies; DET with same features as its head or the other way round if PronType=Art or Dem

* Tatiana Cavalcanti
* Date:   Wed May 19 14:44:56 2021 -0300
* Lines changed: 539
* Commit: [4dfd6de383be7b49ffb7005907919a1096bf3855](https://github.com/alvelvis/meu-mestrado/commit/4dfd6de383be7b49ffb7005907919a1096bf3855)
* Patch file: [2021_5_19_14:44:56-4dfd6de383be7b49ffb7005907919a1096bf3855.patch](patch/2021_5_19_14:44:56-4dfd6de383be7b49ffb7005907919a1096bf3855.patch)

fácies as NOUN, lemma fácies; DET with same features as its head or the other way round if PronType=Art or Dem

```diff
 49	–	–	PUNCT	_	_	50	punct	O	_
 50	composto	compor	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	47	acl	O	_
 51-52	pelas	_	_	_	_	_	_	O	_
-51	por	por	ADP	_	_	54	case	O	_
-52	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	54	det	O	_
-53	fácies	fácie	ADJ	_	Gender=Fem|Number=Plur	54	amod	B=LITOLOGIA	_
-54	siliciclásticas	siliciclástica	NOUN	_	Gender=Fem|Number=Plur	50	obl:agent	O	_
+51	por	por	ADP	_	_	53	case	O	_
+52	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	53	det	O	_
+53	fácies	fácies	NOUN	_	Gender=Fem|Number=Plur	50	obl:agent	B=LITOLOGIA	_
+54	siliciclásticas	siliciclástica	ADJ	_	Gender=Fem|Number=Plur	53	amod	O	_
 55-56	da	_	_	_	_	_	_	O	_
 55	de	de	ADP	_	_	57	case	O	_
 56	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	57	det	O	_
-57	Formação	Formação	PROPN	_	Gender=Fem|Number=Sing	54	nmod	B=UNIDADE_LITOESTRATIGRÁFICA	_
+57	Formação	Formação	PROPN	_	Gender=Fem|Number=Sing	53	nmod	B=UNIDADE_LITOESTRATIGRÁFICA	_
 58	Cassino	Cassino	PROPN	_	Number=Sing	57	flat:name	I=UNIDADE_LITOESTRATIGRÁFICA	_
 59	,	,	PUNCT	_	_	60	punct	O	_
 60	constituindo	constituir	VERB	_	VerbForm=Ger	50	advcl	O	_
```

## correções elvis petroles_3

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed May 19 18:39:28 2021 -0300
* Lines changed: 71
* Commit: [72ad91acb6b2dbcec9b8cc850ddda9fa39c36645](https://github.com/alvelvis/meu-mestrado/commit/72ad91acb6b2dbcec9b8cc850ddda9fa39c36645)
* Patch file: [2021_5_19_18:39:28-72ad91acb6b2dbcec9b8cc850ddda9fa39c36645.patch](patch/2021_5_19_18:39:28-72ad91acb6b2dbcec9b8cc850ddda9fa39c36645.patch)

correções elvis petroles_3

```diff
 22	a	a	ADP	_	_	24	case	O	_
 23	seu	seu	DET	_	Gender=Masc|Number=Sing|PronType=Prs	24	det	O	_
 24	respeito	respeito	NOUN	_	Gender=Masc|Number=Sing	21	obj	O	_
-25	se	se	PRON	_	Case=Acc|Gender=Fem|Number=Sing|Person=3|PronType=Prs	26	expl	O	_
-26	comparada	comparar	VERB	_	Gender=Fem|Number=Sing|VerbForm=Part	20	acl	O	_
+25	se	se	SCONJ	_	_	26	mark	O	_
+26	comparada	comparar	VERB	_	Gender=Fem|Number=Sing|VerbForm=Part	18	advcl	O	_
 27-28	às	_	_	_	_	_	_	O	_
 27	a	a	ADP	_	_	30	case	O	_
 28	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	30	det	O	_
```

## correções mclara petroles_3

* Maria Clara Castro
* Date:   Wed May 19 18:40:27 2021 -0300
* Lines changed: 73
* Commit: [eb928fd2e4709a6df8385ab0e0b6b60a3b223564](https://github.com/alvelvis/meu-mestrado/commit/eb928fd2e4709a6df8385ab0e0b6b60a3b223564)
* Patch file: [2021_5_19_18:40:27-eb928fd2e4709a6df8385ab0e0b6b60a3b223564.patch](patch/2021_5_19_18:40:27-eb928fd2e4709a6df8385ab0e0b6b60a3b223564.patch)

correções mclara petroles_3

```diff
 42	2000	2000	NUM	_	NumType=Card	38	nmod:appos	O	_
 43	)	)	PUNCT	_	_	42	punct	O	_
 44	,	,	PUNCT	_	_	47	punct	O	_
-45	além	além	ADV	_	_	47	cc	O	_
+45	além	além	ADV	_	_	47	cc	O	MWE=além_de|MWEPOS=CCONJ
 46	de	de	ADP	_	_	45	fixed	O	_
-47	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	24	conj	B=INSTRUMENTO	_
+47	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	11	conj	B=INSTRUMENTO	_
 48	gravimétrico	gravimétrico	ADJ	_	Gender=Masc|Number=Sing	47	amod	O	_
 49	e	e	CCONJ	_	_	50	cc	O	_
 50	aeromagnetométrico	aeromagnetométrico	ADJ	_	Gender=Masc|Number=Sing	48	conj	O	_
-51	.	.	PUNCT	_	_	47	punct	O	_
+51	.	.	PUNCT	_	_	10	punct	O	_
 52	.	.	PUNCT	_	_	10	punct	O	_
 # text = Figura 1: Localização da Bacia de Pelotas
```

## correções aline

* Aline Silveira
* Date:   Wed May 19 19:08:30 2021 -0300
* Lines changed: 47
* Commit: [50824b0432986749b03a99255f32e71da23d6d79](https://github.com/alvelvis/meu-mestrado/commit/50824b0432986749b03a99255f32e71da23d6d79)
* Patch file: [2021_5_19_19:08:30-50824b0432986749b03a99255f32e71da23d6d79.patch](patch/2021_5_19_19:08:30-50824b0432986749b03a99255f32e71da23d6d79.patch)

correções aline

```diff
 15	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	16	det	O	_
 16	continente	continente	NOUN	_	Gender=Masc|Number=Sing	13	nmod	O	_
 17	com	com	ADP	_	_	18	case	O	_
-18	dados	dado	NOUN	_	Gender=Masc|Number=Plur	4	obl	O	_
+18	dados	dado	NOUN	_	Gender=Masc|Number=Plur	9	nmod	O	_
 19	de	de	ADP	_	_	20	case	O	_
 20	subsuperfície	subsuperfície	NOUN	_	Gender=Fem|Number=Sing	18	nmod	B=LOCAL:GEO	_
 21	(	(	PUNCT	_	_	22	punct	O	_
```

## fácies sedimentar

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jun 9 13:20:48 2021 -0300
* Lines changed: 16
* Commit: [51713966b5603e3e4f2c04fc63f436788212b63d](https://github.com/alvelvis/meu-mestrado/commit/51713966b5603e3e4f2c04fc63f436788212b63d)
* Patch file: [2021_6_9_13:20:48-51713966b5603e3e4f2c04fc63f436788212b63d.patch](patch/2021_6_9_13:20:48-51713966b5603e3e4f2c04fc63f436788212b63d.patch)

fácies sedimentar

```diff
 1	Análise	Análise	NOUN	_	Gender=Fem|Number=Sing	0	root	O	_
 2	de	de	ADP	_	_	3	case	O	_
 3	fácies	fácies	NOUN	_	Gender=Masc|Number=Plur	1	nmod	B=LITOLOGIA	_
-4	sedimentares	sedimentar	ADJ	_	Gender=Masc|Number=Plur	3	compound	I=LITOLOGIA	_
+4	sedimentares	sedimentar	ADJ	_	Gender=Masc|Number=Plur	3	amod	I=LITOLOGIA	_
 # text = A análise de fácies é um método fundamental de caracterização de rocha com atributos litológicos, físicos e biológicos singulares e distintos das demais..
 # sent_id = 284-20150917-MONOGRAFIA_0-43
```

## feats de fácies

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jun 9 14:02:51 2021 -0300
* Lines changed: 157
* Commit: [7fc9bff36097f635effbfd32b37b8f46d6c5a792](https://github.com/alvelvis/meu-mestrado/commit/7fc9bff36097f635effbfd32b37b8f46d6c5a792)
* Patch file: [2021_6_9_14:02:51-7fc9bff36097f635effbfd32b37b8f46d6c5a792.patch](patch/2021_6_9_14:02:51-7fc9bff36097f635effbfd32b37b8f46d6c5a792.patch)

feats de fácies

```diff
 3	em	em	ADP	_	_	5	case	O	_
 4	este	este	DET	_	Gender=Masc|Number=Sing|PronType=Dem	5	det	O	_
 5	trabalho	trabalho	NOUN	_	Gender=Masc|Number=Sing	2	obl	O	_
-6	técnicas	técnico	ADJ	_	Gender=Fem|Number=Plur	5	amod	O	_
+6	técnicas	técnica	NOUN	_	Gender=Fem|Number=Plur	2	nsubj:pass	O	_
 7	e	e	CCONJ	_	_	8	cc	O	_
-8	métodos	método	NOUN	_	Gender=Masc|Number=Plur	5	conj	B=MÉTODO	_
+8	métodos	método	NOUN	_	Gender=Masc|Number=Plur	6	conj	B=MÉTODO	_
 9	de	de	ADP	_	_	10	case	O	_
 10	descrição	descrição	NOUN	_	Gender=Fem|Number=Sing	8	nmod	O	_
 11	de	de	ADP	_	_	12	case	O	_
-12	fácies	fácies	NOUN	_	Gender=Masc|Number=Plur	10	nmod	B=LITOLOGIA	_
+12	fácies	fácies	NOUN	_	Gender=Fem|Number=Plur	10	nmod	B=LITOLOGIA	_
 13	e	e	CCONJ	_	_	14	cc	O	_
-14	análise	análise	NOUN	_	Gender=Fem|Number=Sing	12	conj	O	_
+14	análise	análise	NOUN	_	Gender=Fem|Number=Sing	6	conj	O	_
 15-16	da	_	_	_	_	_	_	_	_
 15	de	de	ADP	_	_	17	case	O	_
 16	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	17	det	O	_
```

## conglomerados e sustentados

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jun 9 14:34:53 2021 -0300
* Lines changed: 27
* Commit: [7c9d2d38d0cb2df14cef14a0d03dd0ea3f2169e4](https://github.com/alvelvis/meu-mestrado/commit/7c9d2d38d0cb2df14cef14a0d03dd0ea3f2169e4)
* Patch file: [2021_6_9_14:34:53-7c9d2d38d0cb2df14cef14a0d03dd0ea3f2169e4.patch](patch/2021_6_9_14:34:53-7c9d2d38d0cb2df14cef14a0d03dd0ea3f2169e4.patch)

conglomerados e sustentados

```diff
 2	,	,	PUNCT	_	_	3	punct	O	_
 3	siltitos	siltito	NOUN	_	Gender=Masc|Number=Plur	1	conj	B=LITOLOGIA	_
 4	e	e	CCONJ	_	_	5	cc	O	_
-5	conglomerados	conglomerar	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part	1	conj	O	_
+5	conglomerados	conglomerado	NOUN	_	Gender=Masc|Number=Plur	1	conj	O	_
 6	com	com	ADP	_	_	7	case	O	_
 7	seixos	seixo	NOUN	_	Gender=Masc|Number=Plur	5	obl	O	_
 8	de	de	ADP	_	_	9	case	O	_
```

## abserva-se e outros erros de contrações iniciais

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jun 9 15:17:37 2021 -0300
* Lines changed: 101
* Commit: [c603e4d70c1ba8e8a12c3c0bc1c3352f889dd2bf](https://github.com/alvelvis/meu-mestrado/commit/c603e4d70c1ba8e8a12c3c0bc1c3352f889dd2bf)
* Patch file: [2021_6_9_15:17:37-c603e4d70c1ba8e8a12c3c0bc1c3352f889dd2bf.patch](patch/2021_6_9_15:17:37-c603e4d70c1ba8e8a12c3c0bc1c3352f889dd2bf.patch)

abserva-se e outros erros de contrações iniciais

```diff
 # text = Busca-se analisar as estruturas continentais que possam apresentar continuidade na bacia de Pelotas (“Lineamento Tibagi” e “Sinclinal de Torres”), verificando sua influência na evolução e deformação da mesma..
 # sent_id = 247-20140910-MONOGRAFIA_0-11
 1-2	Busca-se	_	_	_	_	_	_	_	_
-1	Dusca	doscar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
+1	Busca	buscar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
 2	se	se	PRON	_	Case=Acc|Gender=Unsp|PronType=Prs	1	expl	O	_
 3	analisar	analisar	VERB	_	VerbForm=Inf	1	xcomp	O	_
 4	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	5	det	O	_
```

## sincronizar correções da tati atrasadas

* Tatiana Cavalcanti
* Date:   Wed Jun 9 21:03:18 2021 -0300
* Lines changed: 679
* Commit: [4ed0c6e32b75471d714d0ef81305b15c9979467a](https://github.com/alvelvis/meu-mestrado/commit/4ed0c6e32b75471d714d0ef81305b15c9979467a)
* Patch file: [2021_6_9_21:03:18-4ed0c6e32b75471d714d0ef81305b15c9979467a.patch](patch/2021_6_9_21:03:18-4ed0c6e32b75471d714d0ef81305b15c9979467a.patch)

sincronizar correções da tati atrasadas

```diff
 39	poço	poço	NOUN	_	Gender=Masc|Number=Sing	37	nmod	O	_
 40	,	,	PUNCT	_	_	41	punct	O	_
 41	perfil	perfil	NOUN	_	Gender=Masc|Number=Sing	30	conj	O	_
-42	composto	compor	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	41	acl	O	_
+42	composto	composto	ADJ	_	Gender=Masc|Number=Sing	41	amod	O	_
 43	,	,	PUNCT	_	_	44	punct	O	_
 44	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	30	conj	B=INSTRUMENTO	_
 45	gravimétrico	gravimétrico	ADJ	_	Gender=Masc|Number=Sing	44	amod	O	_
```

## aspas não podem ser head

* Aline Silveira
* Date:   Tue Jun 15 20:00:31 2021 -0300
* Lines changed: 192
* Commit: [8f088149d87aa346b817a9360f5bc4b03e25cdad](https://github.com/alvelvis/meu-mestrado/commit/8f088149d87aa346b817a9360f5bc4b03e25cdad)
* Patch file: [2021_6_15_20:00:31-8f088149d87aa346b817a9360f5bc4b03e25cdad.patch](patch/2021_6_15_20:00:31-8f088149d87aa346b817a9360f5bc4b03e25cdad.patch)

aspas não podem ser head

```diff
 27	(	(	PUNCT	_	_	28	punct	O	_
 28	2012	2012	NUM	_	NumType=Card	24	nmod:appos	O	_
 29	)	)	PUNCT	_	_	28	punct	O	_
-30	e	e	CCONJ	_	_	31	cc	O	_
-31	“	“	PROPN	_	Gender=Masc|Number=Sing	24	conj	O	_
-32	Sinclinal	Sinclinal	PROPN	_	Number=Sing	31	flat:name	O	_
-33	”	”	PROPN	_	Number=Sing	31	flat:name	O	_
-34	de	de	ADP	_	_	31	flat:name	O	_
-35	Torres	Torres	PROPN	_	Gender=Masc|Number=Sing	31	flat:name	O	_
-36	caracterizado	caracterizar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	31	acl	O	_
+30	e	e	CCONJ	_	_	32	cc	O	_
+31	“	"	PUNCT	_	Gender=Masc|Number=Sing	32	punct	O	_
+32	Sinclinal	Sinclinal	PROPN	_	Number=Sing	24	conj	O	_
+33	”	"	PUNCT	_	Number=Sing	32	punct	O	_
+34	de	de	ADP	_	_	35	case	O	_
+35	Torres	Torres	PROPN	_	Gender=Masc|Number=Sing	32	nmod	O	_
+36	caracterizado	caracterizar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	32	acl	O	_
 37	por	por	ADP	_	_	38	case	O	_
 38	Vitorello	Vitorello	PROPN	_	Gender=Masc|Number=Sing	36	obl:agent	O	_
 39	e	e	CCONJ	_	_	38	flat:name	O	_
```

## quando, como, enquanto

* Maria Clara Castro
* Date:   Fri Jun 18 00:27:44 2021 -0300
* Lines changed: 505
* Commit: [df297cc3dfdf90a23e54ad72c18e23d25833ff4d](https://github.com/alvelvis/meu-mestrado/commit/df297cc3dfdf90a23e54ad72c18e23d25833ff4d)
* Patch file: [2021_6_18_00:27:44-df297cc3dfdf90a23e54ad72c18e23d25833ff4d.patch](patch/2021_6_18_00:27:44-df297cc3dfdf90a23e54ad72c18e23d25833ff4d.patch)

quando, como, enquanto

```diff
 37	pouco	pouco	ADV	_	_	38	advmod	O	_
 38	deformado	deformar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	35	conj	O	_
 39	,	,	PUNCT	_	_	41	punct	O	_
-40	quando	quando	ADV	_	_	41	advmod	O	_
+40	quando	quando	SCONJ	_	_	41	mark	O	_
 41	comparado	comparar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	32	advcl	O	_
 42-43	às	_	_	_	_	_	_	_	_
 42	a	a	ADP	_	_	45	case	O	_
```

## MWE a_seguir

* Maria Clara Castro
* Date:   Wed Jun 23 20:06:54 2021 -0300
* Lines changed: 191
* Commit: [a5334dd7e0cacedc64cf32ef16fc19ce4f0807d8](https://github.com/alvelvis/meu-mestrado/commit/a5334dd7e0cacedc64cf32ef16fc19ce4f0807d8)
* Patch file: [2021_6_23_20:06:54-a5334dd7e0cacedc64cf32ef16fc19ce4f0807d8.patch](patch/2021_6_23_20:06:54-a5334dd7e0cacedc64cf32ef16fc19ce4f0807d8.patch)

MWE a_seguir

```diff
 # text = A seguir, são apresentadas as etapas e a metodologia que foi adotada no trabalho..
 # sent_id = 247-20140910-MONOGRAFIA_0-16
-1	A	a	SCONJ	_	_	2	mark	O	_
-2	seguir	seguir	VERB	_	VerbForm=Inf	5	advcl	O	_
+1	A	a	ADP	_	_	5	obl	O	MWEPOS=ADV
+2	seguir	seguir	VERB	_	VerbForm=Inf	1	fixed	O	_
 3	,	,	PUNCT	_	_	2	punct	O	_
 4	são	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	5	aux:pass	O	_
 5	apresentadas	apresentar	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass	0	root	O	_
```

## MWE como também

* Maria Clara Castro
* Date:   Wed Jun 23 20:07:51 2021 -0300
* Lines changed: 48
* Commit: [7592c05dfaa5cb42cd1e7e19406fd69dc3b50c09](https://github.com/alvelvis/meu-mestrado/commit/7592c05dfaa5cb42cd1e7e19406fd69dc3b50c09)
* Patch file: [2021_6_23_20:07:51-7592c05dfaa5cb42cd1e7e19406fd69dc3b50c09.patch](patch/2021_6_23_20:07:51-7592c05dfaa5cb42cd1e7e19406fd69dc3b50c09.patch)

MWE como também

```diff
 13	vetor	vetor	NOUN	_	Gender=Masc|Number=Sing	10	nmod	O	_
 14	resultante	resultante	ADJ	_	Gender=Masc|Number=Sing	13	amod	O	_
 15	,	,	PUNCT	_	_	19	punct	O	_
-16	como	como	ADV	_	_	19	cc	O	_
-17	também	também	ADV	_	_	19	advmod	O	_
+16	como	como	ADV	_	_	19	cc	O	MWEPOS=CCONJ
+17	também	também	ADV	_	_	16	fixed	O	_
 18	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	19	det	O	_
 19	dispersão	dispersão	NOUN	_	Gender=Fem|Number=Sing	10	conj	O	_
 20	original	original	ADJ	_	Gender=Fem|Number=Sing	19	amod	O	_
```

## MWE devido a

* Maria Clara Castro
* Date:   Wed Jun 23 20:09:06 2021 -0300
* Lines changed: 544
* Commit: [ae013a1a98a4396f8021b29641810686f6184b95](https://github.com/alvelvis/meu-mestrado/commit/ae013a1a98a4396f8021b29641810686f6184b95)
* Patch file: [2021_6_23_20:09:06-ae013a1a98a4396f8021b29641810686f6184b95.patch](patch/2021_6_23_20:09:06-ae013a1a98a4396f8021b29641810686f6184b95.patch)

MWE devido a

```diff
 6	direção	direção	NOUN	_	Gender=Fem|Number=Sing	3	obl	O	_
 7	NE-SW	NE-SW	PROPN	_	Gender=Fem|Number=Sing	6	nmod	O	_
 8	,	,	PUNCT	_	_	3	punct	O	_
-9	devido	devido	ADV	_	_	12	case	O	MWEPOS=ADP
+9	devido	dever	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	12	case	O	MWEPOS=ADP
 10-11	à	_	_	_	_	_	_	_	_
-10	a	a	ADP	_	_	12	case	O	_
+10	a	a	ADP	_	_	9	fixed	O	_
 11	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	12	det	O	_
 12	colisão	colisão	NOUN	_	Gender=Fem|Number=Sing	1	obl	O	_
 13	continental	continental	ADJ	_	Gender=Fem|Number=Sing	12	amod	O	_
```

## MWE bem como

* Maria Clara Castro
* Date:   Wed Jun 23 20:10:18 2021 -0300
* Lines changed: 116
* Commit: [ffd4df9f5ef3d04b08ab9d1a08fce31160931c34](https://github.com/alvelvis/meu-mestrado/commit/ffd4df9f5ef3d04b08ab9d1a08fce31160931c34)
* Patch file: [2021_6_23_20:10:18-ffd4df9f5ef3d04b08ab9d1a08fce31160931c34.patch](patch/2021_6_23_20:10:18-ffd4df9f5ef3d04b08ab9d1a08fce31160931c34.patch)

MWE bem como

```diff
 19	conteúdo	conteúdo	NOUN	_	Gender=Masc|Number=Sing	12	obl	O	_
 20	fossilífero	fossilífero	ADJ	_	Gender=Masc|Number=Sing	19	amod	O	_
 21	,	,	PUNCT	_	_	26	punct	O	_
-22	bem	bem	ADP	_	_	26	cc	O	_
-23	como	como	ADV	_	_	22	fixed	O	_
+22	bem	bem	ADV	_	_	26	cc	O	MWEPOS=CCONJ
+23	como	como	ADP	_	_	22	fixed	O	_
 24	por	por	ADP	_	_	26	case	O	_
 25	sua	seu	DET	_	Gender=Fem|Number=Sing|PronType=Prs	26	det	O	_
 26	complexidade	complexidade	NOUN	_	Gender=Fem|Number=Sing	19	conj	O	_
```

## Alterações pulverizadas de amod, punct, flat:name e com boa parte de appos, especialmente apposXconj

* Aline Silveira
* Date:   Fri Jun 25 02:15:03 2021 -0300
* Lines changed: 364
* Commit: [c29dfd7a6814c8974961e8777ad4b1af44ab13fb](https://github.com/alvelvis/meu-mestrado/commit/c29dfd7a6814c8974961e8777ad4b1af44ab13fb)
* Patch file: [2021_6_25_02:15:03-c29dfd7a6814c8974961e8777ad4b1af44ab13fb.patch](patch/2021_6_25_02:15:03-c29dfd7a6814c8974961e8777ad4b1af44ab13fb.patch)

Alterações pulverizadas de amod, punct, flat:name e com boa parte de appos, especialmente apposXconj

```diff
 22-23	da	_	_	_	_	_	_	_	_
 22	de	de	ADP	_	_	24	case	O	_
 23	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	24	det	O	_
-24	porção	porção	NOUN	_	Gender=Fem|Number=Sing	13	conj	O	_
+24	porção	porção	NOUN	_	Gender=Fem|Number=Sing	8	nmod	O	_
 25	norte	norte	ADJ	_	Gender=Fem|Number=Sing	24	amod	O	_
 26-27	da	_	_	_	_	_	_	_	_
 26	de	de	ADP	_	_	28	case	O	_
```

## features dos verbos bugados "abserva-se"

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jul 7 05:24:26 2021 -0300
* Lines changed: 102
* Commit: [c9bbc9f21f13bd0769fd03ee752d7e4fba9fffa2](https://github.com/alvelvis/meu-mestrado/commit/c9bbc9f21f13bd0769fd03ee752d7e4fba9fffa2)
* Patch file: [2021_7_7_05:24:26-c9bbc9f21f13bd0769fd03ee752d7e4fba9fffa2.patch](patch/2021_7_7_05:24:26-c9bbc9f21f13bd0769fd03ee752d7e4fba9fffa2.patch)

features dos verbos bugados "abserva-se"

```diff
 # text = Busca-se analisar as estruturas continentais que possam apresentar continuidade na bacia de Pelotas (“Lineamento Tibagi” e “Sinclinal de Torres”), verificando sua influência na evolução e deformação da mesma..
 # sent_id = 247-20140910-MONOGRAFIA_0-11
 1-2	Busca-se	_	_	_	_	_	_	_	_
-1	Dusca	doscar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
+1	Busca	buscar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
 2	se	se	PRON	_	Case=Acc|Gender=Unsp|PronType=Prs	1	expl	O	_
 3	analisar	analisar	VERB	_	VerbForm=Inf	1	xcomp	O	_
 4	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	5	det	O	_
```

## Alterações nas duas direções

* Aline Silveira
* Date:   Thu Jul 8 01:26:46 2021 -0300
* Lines changed: 353
* Commit: [09a94714b7669dedf946d33d1b334eca352aef58](https://github.com/alvelvis/meu-mestrado/commit/09a94714b7669dedf946d33d1b334eca352aef58)
* Patch file: [2021_7_8_01:26:46-09a94714b7669dedf946d33d1b334eca352aef58.patch](patch/2021_7_8_01:26:46-09a94714b7669dedf946d33d1b334eca352aef58.patch)

Alterações nas duas direções
apposXparataxis
apposXnmod:appos
apposXnsubj
apposXnmod
amodXxcomp

```diff
 # sent_id = 247-20140910-MONOGRAFIA_0-87
 1	Ordovício-Siluriana	Ordovício-Siluriana	PROPN	_	Gender=Fem|Number=Sing	0	root	O	_
 2	(	(	PUNCT	_	_	3	punct	O	_
-3	Supersequência	Supersequência	PROPN	_	Gender=Fem|Number=Sing	1	appos	O	_
+3	Supersequência	Supersequência	PROPN	_	Gender=Fem|Number=Sing	1	parataxis	O	_
 4	Rio	Rio	PROPN	_	Number=Sing	3	flat:name	O	_
 5	Ivaí	Ivaí	PROPN	_	Number=Sing	3	flat:name	O	_
 6	)	)	PUNCT	_	_	3	flat:name	O	_
```

## alem_de

* Maria Clara Castro
* Date:   Thu Jul 8 01:29:09 2021 -0300
* Lines changed: 221
* Commit: [b4593ae3ca54af6ecaeb898481c8df332d902f84](https://github.com/alvelvis/meu-mestrado/commit/b4593ae3ca54af6ecaeb898481c8df332d902f84)
* Patch file: [2021_7_8_01:29:09-b4593ae3ca54af6ecaeb898481c8df332d902f84.patch](patch/2021_7_8_01:29:09-b4593ae3ca54af6ecaeb898481c8df332d902f84.patch)

alem_de

```diff
 35	e	e	CCONJ	_	_	36	cc	O	_
 36	lístricas	lístrico	ADJ	_	Gender=Fem|Number=Plur	32	conj	O	_
 37	,	,	PUNCT	_	_	41	punct	O	_
-38	além	além	ADV	_	_	41	cc	O	_
+38	além	além	ADV	_	_	41	cc	O	MWEPOS=CCONJ
 39-40	da	_	_	_	_	_	_	_	_
 39	de	de	ADP	_	_	38	fixed	O	_
 40	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	41	det	O	_
```

## assim_como

* Maria Clara Castro
* Date:   Thu Jul 8 01:29:46 2021 -0300
* Lines changed: 98
* Commit: [3bedc0e8d1dcc3f29a5fcc9a598359310eafc495](https://github.com/alvelvis/meu-mestrado/commit/3bedc0e8d1dcc3f29a5fcc9a598359310eafc495)
* Patch file: [2021_7_8_01:29:46-3bedc0e8d1dcc3f29a5fcc9a598359310eafc495.patch](patch/2021_7_8_01:29:46-3bedc0e8d1dcc3f29a5fcc9a598359310eafc495.patch)

assim_como

```diff
 3	de	de	ADP	_	_	2	flat:name	O	_
 4	Pelotas	Pelotas	PROPN	_	Number=Sing	2	flat:name	B=BACIA	_
 5	,	,	PUNCT	_	_	10	punct	O	_
-6	assim	assim	ADV	_	_	10	advmod	O	_
+6	assim	assim	ADV	_	_	10	cc	O	MWEPOS=CCONJ
 7	como	como	ADP	_	_	6	fixed	O	_
 8	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	10	det	O	_
 9	demais	demais	DET	_	Gender=Fem|Number=Plur|PronType=Ind	10	det	O	_
-10	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	2	nmod:appos	B=BACIA:TIPO	_
+10	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	2	conj	B=BACIA:TIPO	_
 11-12	da	_	_	_	_	_	_	_	_
 11	de	de	ADP	_	_	13	case	O	_
 12	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	13	det	O	_
```

## através_de

* Maria Clara Castro
* Date:   Thu Jul 8 01:30:43 2021 -0300
* Lines changed: 882
* Commit: [a0647e49f63d8c9b7e6b38449c89c07ea9457f1a](https://github.com/alvelvis/meu-mestrado/commit/a0647e49f63d8c9b7e6b38449c89c07ea9457f1a)
* Patch file: [2021_7_8_01:30:43-a0647e49f63d8c9b7e6b38449c89c07ea9457f1a.patch](patch/2021_7_8_01:30:43-a0647e49f63d8c9b7e6b38449c89c07ea9457f1a.patch)

através_de

```diff
 12	Pelotas	Pelotas	PROPN	_	Number=Sing	10	flat:name	B=BACIA	_
 13	foi	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	14	aux:pass	O	_
 14	realizada	realizar	VERB	_	Gender=Fem|Number=Sing|VerbForm=Part|Voice=Pass	0	root	O	_
-15	através	através	ADV	_	_	14	advmod	O	_
-16	de	de	ADP	_	_	18	case	O	_
+15	através	através	ADV	_	_	18	case	O	MWEPOS=ADP
+16	de	de	ADP	_	_	15	fixed	O	_
 17	17	17	NUM	_	NumType=Card	18	nummod	O	_
-18	seções	seção	NOUN	_	Gender=Fem|Number=Plur	15	obl	O	_
+18	seções	seção	NOUN	_	Gender=Fem|Number=Plur	14	obl	O	_
 19	sísmicas	sísmico	ADJ	_	Gender=Fem|Number=Plur	18	amod	O	_
 20	,	,	PUNCT	_	_	14	punct	O	_
 21	onde	onde	PRON	_	Gender=Fem|Number=Sing|PronType=Rel	23	obl	O	_
```

## com_vistas_a

* Maria Clara Castro
* Date:   Thu Jul 8 01:34:29 2021 -0300
* Lines changed: 72
* Commit: [d05c5a8ed8190af9b716fc202aa29970e5fb40c7](https://github.com/alvelvis/meu-mestrado/commit/d05c5a8ed8190af9b716fc202aa29970e5fb40c7)
* Patch file: [2021_7_8_01:34:29-d05c5a8ed8190af9b716fc202aa29970e5fb40c7.patch](patch/2021_7_8_01:34:29-d05c5a8ed8190af9b716fc202aa29970e5fb40c7.patch)

com_vistas_a

```diff
 32-33	à	_	_	_	_	_	_	_	_
 32	a	a	ADP	_	_	30	fixed	O	_
 33	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	34	det	O	_
-34	valoração	valoração	NOUN	_	Gender=Fem|Number=Sing	26	nmod	O	_
+34	valoração	valoração	NOUN	_	Gender=Fem|Number=Sing	9	obl	O	_
 35-36	dos	_	_	_	_	_	_	_	_
 35	de	de	ADP	_	_	37	case	O	_
 36	os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	37	det	O	_
```

## quanto_a

* Maria Clara Castro
* Date:   Thu Jul 8 01:34:53 2021 -0300
* Lines changed: 93
* Commit: [c16ee551855c7a24ef2da56120afc3d947ca2b3b](https://github.com/alvelvis/meu-mestrado/commit/c16ee551855c7a24ef2da56120afc3d947ca2b3b)
* Patch file: [2021_7_8_01:34:53-c16ee551855c7a24ef2da56120afc3d947ca2b3b.patch](patch/2021_7_8_01:34:53-c16ee551855c7a24ef2da56120afc3d947ca2b3b.patch)

quanto_a

```diff
 10	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	11	det	O	_
 11	emulsão	emulsão	NOUN	_	Gender=Fem|Number=Sing	8	nmod	B=QUÍMICA	_
 12	asfáltica	asfáltico	ADJ	_	Gender=Fem|Number=Sing	11	amod	B=LITOLOGIA	_
-13	quanto	quanto	ADP	_	_	15	case	O	MWE=quanto_a|MWEPOS=ADP
+13	quanto	quanto	ADV	_	_	15	case	O	MWE=quanto_a|MWEPOS=ADP
 14	a	a	ADP	_	_	13	fixed	O	_
 15	sedimentação	sedimentação	NOUN	_	Gender=Fem|Number=Sing	11	nmod	O	_
 16	,	,	PUNCT	_	_	17	punct	O	_
```

## acl deve ter mesmo gênero de seu pai

* Tatiana Cavalcanti
* Date:   Thu Jul 8 01:37:00 2021 -0300
* Lines changed: 530
* Commit: [b00f290675e51bc4f0b2a20ec30d645cd1b7b6ef](https://github.com/alvelvis/meu-mestrado/commit/b00f290675e51bc4f0b2a20ec30d645cd1b7b6ef)
* Patch file: [2021_7_8_01:37:00-b00f290675e51bc4f0b2a20ec30d645cd1b7b6ef.patch](patch/2021_7_8_01:37:00-b00f290675e51bc4f0b2a20ec30d645cd1b7b6ef.patch)

acl deve ter mesmo gênero de seu pai

```diff
 34	)	)	PUNCT	_	_	32	punct	O	_
 35	,	,	PUNCT	_	_	36	punct	O	_
 36	matriz	matriz	NOUN	_	Gender=Fem|Number=Sing	30	conj	O	_
-37	sustentados	sustentar	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part	36	acl	O	_
+37	sustentados	sustentado	ADJ	_	Gender=Masc|Number=Plur	36	compound	O	_
 38	a	a	ADP	_	_	39	case	O	_
 39	arenitos	arenito	NOUN	_	Gender=Masc|Number=Plur	37	obl	B=LITOLOGIA	_
 40	muito	muito	ADV	_	_	41	advmod	O	_
```

## obl_nmod .*nte e .*vel

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jul 7 04:24:14 2021 -0300
* Lines changed: 236
* Commit: [112e3457b2d37aeb9c27d320698c8a960ac0a997](https://github.com/alvelvis/meu-mestrado/commit/112e3457b2d37aeb9c27d320698c8a960ac0a997)
* Patch file: [2021_7_7_04:24:14-112e3457b2d37aeb9c27d320698c8a960ac0a997.patch](patch/2021_7_7_04:24:14-112e3457b2d37aeb9c27d320698c8a960ac0a997.patch)

obl_nmod .*nte e .*vel
NOUN filho de NOUN, caso haja amod .*nte ou .*vel, provavelmente deverá ser obl desse adjetivo
partial obl_nmod elvis
squash

```diff
 4-5	no	_	_	_	_	_	_	_	_
 4	em	em	ADP	_	_	6	case	O	_
 5	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	6	det	O	_
-6	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	2	nmod	B=INSTRUMENTO	_
+6	mapa	mapa	NOUN	_	Gender=Masc|Number=Sing	3	obl	B=INSTRUMENTO	_
 7	foram	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	8	aux:pass	O	_
 8	interpretadas	interpretar	VERB	_	Gender=Fem|Number=Plur|VerbForm=Part|Voice=Pass	0	root	O	_
 9	com	com	ADP	_	_	11	case	O	_
```

## correções de "referente"

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Jul 8 04:23:29 2021 -0300
* Lines changed: 73
* Commit: [977fa059d86f22188023c1a360045b2380c54cd0](https://github.com/alvelvis/meu-mestrado/commit/977fa059d86f22188023c1a360045b2380c54cd0)
* Patch file: [2021_7_8_04:23:29-977fa059d86f22188023c1a360045b2380c54cd0.patch](patch/2021_7_8_04:23:29-977fa059d86f22188023c1a360045b2380c54cd0.patch)

correções de "referente"

```diff
 8	banco	banco	NOUN	_	Gender=Masc|Number=Sing	5	obl	O	_
 9	de	de	ADP	_	_	10	case	O	_
 10	dados	dado	NOUN	_	Gender=Masc|Number=Plur	8	nmod	O	_
-11	referente	referente	ADV	_	_	4	advmod	O	_
+11	referente	referente	ADJ	_	Gender=Masc|Number=Sing	8	amod	O	_
 12-13	ao	_	_	_	_	_	_	_	_
 12	a	a	ADP	_	_	14	case	O	_
 13	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	14	det	O	_
```

## correções de obl e nmod

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sat Jul 10 05:21:23 2021 -0300
* Lines changed: 57
* Commit: [dfa248aeea78409c6418689d1168a49fe42efd8c](https://github.com/alvelvis/meu-mestrado/commit/dfa248aeea78409c6418689d1168a49fe42efd8c)
* Patch file: [2021_7_10_05:21:23-dfa248aeea78409c6418689d1168a49fe42efd8c.patch](patch/2021_7_10_05:21:23-dfa248aeea78409c6418689d1168a49fe42efd8c.patch)

correções de obl e nmod

```diff
 # sent_id = 247-20140910-MONOGRAFIA_0-50
 1	Onde	onde	PRON	_	Gender=Masc|Number=Sing|PronType=Rel	3	parataxis	O	_
 2	:	:	PUNCT	_	_	3	punct	O	_
-3	V=	V=	PROPN	_	Gender=Masc|Number=Sing	0	root	O	_
+3	V=	V=	PROPN	_	Gender=Masc|Number=Sing	0	root	O	tokenização
 4	velocidade	velocidade	NOUN	_	Gender=Fem|Number=Sing	3	flat:name	O	_
 5	,	,	PUNCT	_	_	6	punct	O	_
-6	∆	∆	NOUN	_	Gender=Masc|Number=Sing	3	appos	O	_
+6	∆	∆	NOUN	_	Gender=Masc|Number=Sing	3	conj	O	_
 7	S=	S=	PROPN	_	Number=Sing	6	flat:name	O	_
 8	espessura	espessura	NOUN	_	Gender=Fem|Number=Sing	6	nmod	O	_
 9-10	da	_	_	_	_	_	_	_	_
```

## cunha(s) NOUN

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sun Jul 11 02:32:30 2021 -0300
* Lines changed: 9
* Commit: [2d66ae1805ed6b38581c60e3b0e37fbc0a9d2cdc](https://github.com/alvelvis/meu-mestrado/commit/2d66ae1805ed6b38581c60e3b0e37fbc0a9d2cdc)
* Patch file: [2021_7_11_02:32:30-2d66ae1805ed6b38581c60e3b0e37fbc0a9d2cdc.patch](patch/2021_7_11_02:32:30-2d66ae1805ed6b38581c60e3b0e37fbc0a9d2cdc.patch)

cunha(s) NOUN

```diff
 11	identificar	identificar	VERB	_	VerbForm=Inf	10	csubj	O	_
 12	com	com	ADP	_	_	14	case	O	_
 13	maior	grande	ADJ	_	Gender=Fem|Number=Sing	14	amod	O	_
-14	facilidade	facilidade	NOUN	_	Gender=Fem|Number=Sing	11	obj	O	_
-15	cunhas	cunho	ADJ	_	Gender=Fem|Number=Plur	14	amod	O	_
-16	clásticas	clástico	ADJ	_	Gender=Fem|Number=Plur	14	amod	O	_
-17	progradantes	progradante	ADJ	_	Gender=Fem|Number=Plur	14	amod	O	_
+14	facilidade	facilidade	NOUN	_	Gender=Fem|Number=Sing	11	obl	O	_
+15	cunhas	cunha	NOUN	_	Gender=Fem|Number=Plur	11	obj	O	_
+16	clásticas	clástico	ADJ	_	Gender=Fem|Number=Plur	15	amod	O	_
+17	progradantes	progradante	ADJ	_	Gender=Fem|Number=Plur	15	amod	O	_
 18	que	que	PRON	_	Gender=Fem|Number=Plur|PronType=Rel	19	nsubj	O	_
-19	passaram	passar	VERB	_	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	14	acl:relcl	O	_
+19	passaram	passar	VERB	_	Mood=Ind|Number=Plur|Person=3|VerbForm=Fin	15	acl:relcl	O	_
 20	por	por	ADP	_	_	21	case	O	_
 21	períodos	período	NOUN	_	Gender=Masc|Number=Plur	19	obl	O	_
 22	retrogradacionais	retrogradacional	ADJ	_	Gender=Masc|Number=Plur	21	amod	O	_
```

## "se" não pode ser nsubj

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Sun Jul 11 07:18:10 2021 -0300
* Lines changed: 361
* Commit: [33a378890a443a91b16d48593bbd231a92bd7890](https://github.com/alvelvis/meu-mestrado/commit/33a378890a443a91b16d48593bbd231a92bd7890)
* Patch file: [2021_7_11_07:18:10-33a378890a443a91b16d48593bbd231a92bd7890.patch](patch/2021_7_11_07:18:10-33a378890a443a91b16d48593bbd231a92bd7890.patch)

"se" não pode ser nsubj

```diff
 5	campo	campo	NOUN	_	Gender=Masc|Number=Sing	3	nmod	B=CAMPO:TIPO	_
 6-7	constatou-se	_	_	_	_	_	_	_	_
 6	constatou	constatar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	O	_
-7	se	se	PRON	_	Case=Acc|Gender=Unsp|PronType=Prs	6	nsubj	O	_
+7	se	se	PRON	_	_	6	expl	O	_
 8	que	que	SCONJ	_	_	16	mark	O	_
 9-10	na	_	_	_	_	_	_	_	_
 9	em	em	ADP	_	_	11	case	O	_
```

## "se" seguido de particípio

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Jul 13 19:50:12 2021 -0300
* Lines changed: 121
* Commit: [0c8a30478e21598b6445c174024deb210bde8628](https://github.com/alvelvis/meu-mestrado/commit/0c8a30478e21598b6445c174024deb210bde8628)
* Patch file: [2021_7_13_19:50:12-0c8a30478e21598b6445c174024deb210bde8628.patch](patch/2021_7_13_19:50:12-0c8a30478e21598b6445c174024deb210bde8628.patch)

"se" seguido de particípio
"se" SCONJ/mark
"se" provavelmente será SCONJ/mark se dependente de token não verbal (e não auxiliar) ou se VerbForm=Part

```diff
 13	tratado	tratar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	17	advcl	O	_
 14	,	,	PUNCT	_	_	13	punct	O	_
 15	tenha	ter	AUX	_	Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	17	aux	O	_
-16	se	se	PRON	_	Case=Acc|Gender=Masc|Number=Sing|Person=3|PronType=Prs	17	expl	O	_
+16	se	se	PRON	_	_	17	expl	O	_
 17	deteriorado	deteriorar	VERB	_	VerbForm=Part	1	ccomp	O	_
 18	,	,	PUNCT	_	_	19	punct	O	_
 19	ocasionando	ocasionar	VERB	_	VerbForm=Ger	17	advcl	O	_
```

## Segundo_ADP

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jul 14 09:28:27 2021 -0300
* Lines changed: 78
* Commit: [36c40d555e50791ebc581305f64bd676347bb7ef](https://github.com/alvelvis/meu-mestrado/commit/36c40d555e50791ebc581305f64bd676347bb7ef)
* Patch file: [2021_7_14_09:28:27-36c40d555e50791ebc581305f64bd676347bb7ef.patch](patch/2021_7_14_09:28:27-36c40d555e50791ebc581305f64bd676347bb7ef.patch)

Segundo_ADP

```diff
 # text = Segundo Bauer (1999), a emulsão asfáltica é uma dispersão composta de 50 a 70% de cimento asfáltico, pequenas frações de emulsificante (1 a 2%) e o restante de água..
 # sent_id = 241-20140227-MONOGRAFIA_0-65
 1	Segundo	segundo	ADP	_	_	2	case	O	_
-2	Bauer	Bauer	PROPN	_	Gender=Masc|Number=Sing	12	nmod	O	_
+2	Bauer	Bauer	PROPN	_	Gender=Masc|Number=Sing	12	obl	O	_
 3	(	(	PUNCT	_	_	2	flat:name	O	_
 4	1999	1999	NUM	_	NumType=Card	2	flat:name	O	_
 5	)	)	PUNCT	_	_	2	flat:name	O	_
```

## de acordo com

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jul 14 16:05:27 2021 -0300
* Lines changed: 416
* Commit: [77a9e25ebef1a6752374b9f1e5f71cf2c309d379](https://github.com/alvelvis/meu-mestrado/commit/77a9e25ebef1a6752374b9f1e5f71cf2c309d379)
* Patch file: [2021_7_14_16:05:27-77a9e25ebef1a6752374b9f1e5f71cf2c309d379.patch](patch/2021_7_14_16:05:27-77a9e25ebef1a6752374b9f1e5f71cf2c309d379.patch)

de acordo com

```diff
 # text = De acordo com Luiz & Silva (1995), frequentemente os lineamentos observados nos mapas magnéticos são paralelos às direções estruturais como zonas de cisalhamento, falhas, fraturas e dobras..
 # sent_id = 247-20140910-MONOGRAFIA_0-32
-1	De	de	ADP	_	_	4	case	O	_
+1	De	de	ADP	_	_	4	case	O	MWEPOS=ADP
 2	acordo	acordo	NOUN	_	Gender=Masc|Number=Sing	1	fixed	O	_
 3	com	com	ADP	_	_	1	fixed	O	_
 4	Luiz	Luiz	PROPN	_	Gender=Masc|Number=Sing	20	obl	O	_
```

## acl concordância de número

* Maria Clara Castro
* Date:   Sat Jul 10 05:37:02 2021 -0300
* Lines changed: 298
* Commit: [2becf77d15758fc6e768f12011e4506c558af0d0](https://github.com/alvelvis/meu-mestrado/commit/2becf77d15758fc6e768f12011e4506c558af0d0)
* Patch file: [2021_7_10_05:37:02-2becf77d15758fc6e768f12011e4506c558af0d0.patch](patch/2021_7_10_05:37:02-2becf77d15758fc6e768f12011e4506c558af0d0.patch)

acl concordância de número

```diff
 31	dados	dado	NOUN	_	Gender=Masc|Number=Plur	4	obl	O	_
 32	de	de	ADP	_	_	33	case	O	_
 33	poço	poço	NOUN	_	Gender=Masc|Number=Sing	31	nmod	O	_
-34	perfurado	perfurar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	31	acl	O	_
+34	perfurado	perfurar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	33	acl	O	_
 35-36	pela	_	_	_	_	_	_	_	_
 35	por	por	ADP	_	_	37	case	O	_
 36	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	37	det	O	_
```

## amod concordância de gênero

* Maria Clara Castro
* Date:   Tue Jul 13 20:18:34 2021 -0300
* Lines changed: 440
* Commit: [61d2b9897427c345e4c23f1269293b2037de336a](https://github.com/alvelvis/meu-mestrado/commit/61d2b9897427c345e4c23f1269293b2037de336a)
* Patch file: [2021_7_13_20:18:34-61d2b9897427c345e4c23f1269293b2037de336a.patch](patch/2021_7_13_20:18:34-61d2b9897427c345e4c23f1269293b2037de336a.patch)

amod concordância de gênero

```diff
 15	formações	formação	NOUN	_	Gender=Fem|Number=Plur	13	obj	O	_
 16	Furnas	Furnas	PROPN	_	Gender=Fem|Number=Sing	15	nmod	O	_
 17	(	(	PUNCT	_	_	18	punct	O	_
-18	arenitos	arenito	ADJ	_	Gender=Masc|Number=Plur	15	amod	B=LITOLOGIA	_
+18	arenitos	arenito	NOUN	_	Gender=Masc|Number=Plur	16	nmod:appos	B=LITOLOGIA	_
 19	branco-amarelados	branco-amarelado	ADJ	_	Gender=Masc|Number=Plur	18	amod	O	_
 20	,	,	PUNCT	_	_	21	punct	O	_
 21	cauliníticos	caulinítico	ADJ	_	Gender=Masc|Number=Plur	18	conj	O	_
```

## erros de concordância envolvendo acl:relcl

* Tatiana Cavalcanti
* Date:   Wed Jul 14 19:01:04 2021 -0300
* Lines changed: 264
* Commit: [4f870471a1989745f7ac65405c047a954b82cc5c](https://github.com/alvelvis/meu-mestrado/commit/4f870471a1989745f7ac65405c047a954b82cc5c)
* Patch file: [2021_7_14_19:01:04-4f870471a1989745f7ac65405c047a954b82cc5c.patch](patch/2021_7_14_19:01:04-4f870471a1989745f7ac65405c047a954b82cc5c.patch)

erros de concordância envolvendo acl:relcl

```diff
 56	formação	formação	NOUN	_	Gender=Fem|Number=Sing	53	nmod	B=UNIDADE_LITOESTRATIGRÁFICA	_
 57	Atlântida	Atlântida	PROPN	_	Gender=Fem|Number=Sing	56	nmod	I=UNIDADE_LITOESTRATIGRÁFICA	_
 58	que	que	PRON	_	Gender=Fem|Number=Plur|PronType=Rel	59	nsubj	O	_
-59	recobrem	recobrir	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	56	acl:relcl	O	_
+59	recobrem	recobrir	VERB	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	53	acl:relcl	O	_
 60	em	em	ADP	_	_	61	case	O	_
 61	discordância	discordância	NOUN	_	Gender=Fem|Number=Sing	59	obl	B=LITOLOGIA	_
 62	os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	63	det	O	_
```

## Matriz de confusão

* Aline Silveira
* Date:   Wed Jul 14 21:03:40 2021 -0300
* Lines changed: 539
* Commit: [2e56e7e11881c62b3f388221c512713416a8ef0e](https://github.com/alvelvis/meu-mestrado/commit/2e56e7e11881c62b3f388221c512713416a8ef0e)
* Patch file: [2021_7_14_21:03:40-2e56e7e11881c62b3f388221c512713416a8ef0e.patch](patch/2021_7_14_21:03:40-2e56e7e11881c62b3f388221c512713416a8ef0e.patch)

Matriz de confusão
Normas ABNT flat:name
sigla de estados brasileiros como nmod:appos
amodXnmod
caseXflat:name
detXflat:name
caseXfixed
caseXadvmod(um lado só)
caseXmark(um lado só)

```diff
 52	a	a	ADP	_	_	54	case	O	_
 53	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	54	det	O	_
 54	porção	porção	NOUN	_	Gender=Fem|Number=Sing	50	nmod	O	_
-55	Sul	Sul	ADJ	_	Gender=Fem|Number=Sing	54	amod	O	_
+55	Sul	Sul	NOUN	_	Gender=Fem|Number=Sing	54	nmod	O	_
 56-57	do	_	_	_	_	_	_	_	_
 56	de	de	ADP	_	_	58	case	O	_
 57	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	58	det	O	_
```

## Modificações de obl com base no sema e preposições

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Jul 21 06:38:44 2021 -0300
* Lines changed: 19
* Commit: [4c704207fadaaaa56c96b2f6b0d2eb30bcb9e517](https://github.com/alvelvis/meu-mestrado/commit/4c704207fadaaaa56c96b2f6b0d2eb30bcb9e517)
* Patch file: [2021_7_21_06:38:44-4c704207fadaaaa56c96b2f6b0d2eb30bcb9e517.patch](patch/2021_7_21_06:38:44-4c704207fadaaaa56c96b2f6b0d2eb30bcb9e517.patch)

Modificações de obl com base no sema e preposições
- Se pai das preposições "em" e "entre", os seguintes semas devem ser obl: LOCAL CAMPO BACIA LITOESTRATIGRÁFICA POÇO
- Se pai das preposições "em" e "entre", os seguintes semas devem ser obl: GEOCRONOLOGIA
- Se pai das preposições "após durante enquanto há", deve ser obl
No primeiro caso, posteriormente serão obl:lmod
No segundo e terceiro casos, obl:tmod

```diff
 11	ocorreu	ocorrer	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	O	_
 12	após	após	ADP	_	_	14	case	O	_
 13	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	14	det	O	_
-14	separação	separação	NOUN	_	Gender=Fem|Number=Sing	11	obj	O	_
+14	separação	separação	NOUN	_	Gender=Fem|Number=Sing	11	obl	O	_
 15-16	dos	_	_	_	_	_	_	_	_
 15	de	de	ADP	_	_	17	case	O	_
 16	os	o	DET	_	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	17	det	O	_
```

## Correção de preposições erradas

* Aline Silveira
* Date:   Thu Jul 22 18:54:41 2021 -0300
* Lines changed: 94
* Commit: [5eba1aa6265970f3e1275bcc5a10adc8b305aa39](https://github.com/alvelvis/meu-mestrado/commit/5eba1aa6265970f3e1275bcc5a10adc8b305aa39)
* Patch file: [2021_7_22_18:54:41-5eba1aa6265970f3e1275bcc5a10adc8b305aa39.patch](patch/2021_7_22_18:54:41-5eba1aa6265970f3e1275bcc5a10adc8b305aa39.patch)

Correção de preposições erradas

```diff
 15-16	nas	_	_	_	_	_	_	_	_
 15	em	em	ADP	_	_	17	case	O	_
 16	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	17	det	O	_
-17	rochas	rocha	NOUN	_	Gender=Fem|Number=Plur	14	obj	B=LITOLOGIA	_
+17	rochas	rocha	NOUN	_	Gender=Fem|Number=Plur	14	obl	B=LITOLOGIA	_
 18-19	da	_	_	_	_	_	_	_	_
 18	de	de	ADP	_	_	20	case	O	_
 19	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	20	det	O	_
```

## Obl ou obj: lista de verbos seguidos de "em"

* Aline Silveira
* Date:   Thu Jul 22 18:11:42 2021 -0300
* Lines changed: 325
* Commit: [410c27dc87938d516418e108e96efe631fb24513](https://github.com/alvelvis/meu-mestrado/commit/410c27dc87938d516418e108e96efe631fb24513)
* Patch file: [2021_7_22_18:11:42-410c27dc87938d516418e108e96efe631fb24513.patch](patch/2021_7_22_18:11:42-410c27dc87938d516418e108e96efe631fb24513.patch)

Obl ou obj: lista de verbos seguidos de "em"

```diff
 15-16	nas	_	_	_	_	_	_	_	_
 15	em	em	ADP	_	_	17	case	O	_
 16	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	17	det	O	_
-17	rochas	rocha	NOUN	_	Gender=Fem|Number=Plur	14	obj	B=LITOLOGIA	_
+17	rochas	rocha	NOUN	_	Gender=Fem|Number=Plur	14	obl	B=LITOLOGIA	_
 18-19	da	_	_	_	_	_	_	_	_
 18	de	de	ADP	_	_	20	case	O	_
 19	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	20	det	O	_
```

## amod concordância de número

* Maria Clara Castro
* Date:   Fri Jul 23 10:29:37 2021 -0300
* Lines changed: 251
* Commit: [b10877d0a741e2b78e7b7f7e5da9ed3191afcef2](https://github.com/alvelvis/meu-mestrado/commit/b10877d0a741e2b78e7b7f7e5da9ed3191afcef2)
* Patch file: [2021_7_23_10:29:37-b10877d0a741e2b78e7b7f7e5da9ed3191afcef2.patch](patch/2021_7_23_10:29:37-b10877d0a741e2b78e7b7f7e5da9ed3191afcef2.patch)

amod concordância de número

```diff
 31	de	de	ADP	_	_	32	case	O	_
 32	margem	margem	NOUN	_	Gender=Fem|Number=Sing	30	nmod	O	_
 33	continental	continental	ADJ	_	Gender=Fem|Number=Sing	32	amod	O	_
-34	brasileiras	brasileiro	ADJ	_	Gender=Fem|Number=Plur	32	amod	O	_
+34	brasileiras	brasileiro	ADJ	_	Gender=Fem|Number=Plur	30	amod	O	_
 35	.	.	PUNCT	_	_	8	punct	O	_
 36	.	.	PUNCT	_	_	8	punct	O	_
```

## Correções de matriz de confusão -- Maria Clara

* Maria Clara Castro
* Date:   Fri Jul 23 11:12:19 2021 -0300
* Lines changed: 653
* Commit: [f774355e99b6a6d8ec14354f48e1aeb02d1c5174](https://github.com/alvelvis/meu-mestrado/commit/f774355e99b6a6d8ec14354f48e1aeb02d1c5174)
* Patch file: [2021_7_23_11:12:19-f774355e99b6a6d8ec14354f48e1aeb02d1c5174.patch](patch/2021_7_23_11:12:19-f774355e99b6a6d8ec14354f48e1aeb02d1c5174.patch)

Correções de matriz de confusão -- Maria Clara
Advmod x case
Advmod x cc - cc x advmod
Advmod x conj
Advmod x fixed - Fixed x advmod
Advmod x mark
Advmod x amod
Advmod x flat:name
Cc x flat:name
Cc x case
Cc x punct
Conj x flat:name

```diff
 49	bacia	bacia	NOUN	_	Gender=Fem|Number=Sing	9	obl	B=BACIA:TIPO	_
 50	de	de	ADP	_	_	51	case	O	_
 51	Pelotas	Pelotas	PROPN	_	Gender=Masc|Number=Sing	49	nmod	B=BACIA	_
-52	e	e	CCONJ	_	_	51	flat:name	O	_
-53	Milani	Milani	PROPN	_	Gender=Masc|Number=Sing	51	flat:name	O	_
-54	et	et	PROPN	_	Number=Sing	51	flat:name	O	_
-55	al	al	PROPN	_	Number=Sing	51	flat:name	O	_
+52	e	e	CCONJ	_	_	53	cc	O	_
+53	Milani	Milani	PROPN	_	Gender=Masc|Number=Sing	10	conj	O	_
+54	et	et	PROPN	_	Number=Sing	53	flat:name	O	_
+55	al	al	PROPN	_	Number=Sing	53	flat:name	O	_
 56	(	(	PUNCT	_	_	57	punct	O	_
-57	1994	1994	NUM	_	NumType=Card	51	nmod:appos	O	_
+57	1994	1994	NUM	_	NumType=Card	53	nmod:appos	O	_
 58	)	)	PUNCT	_	_	57	punct	O	_
 59	e	e	CCONJ	_	_	60	cc	O	_
-60	Zalan	Zalan	PROPN	_	Gender=Masc|Number=Sing	51	conj	O	_
+60	Zalan	Zalan	PROPN	_	Gender=Masc|Number=Sing	53	conj	O	_
 61	et	et	PROPN	_	Number=Sing	60	flat:name	O	_
 62	al.	al.	PROPN	_	Number=Sing	60	flat:name	O	_
 63	(	(	PUNCT	_	_	60	punct	O	_
```

## Correções de matriz de confusão -- Aline

* Aline Silveira
* Date:   Thu Jul 22 19:09:38 2021 -0300
* Lines changed: 76
* Commit: [7f85f7b70d947c08f4424bf614b5d66bb6d9a0ac](https://github.com/alvelvis/meu-mestrado/commit/7f85f7b70d947c08f4424bf614b5d66bb6d9a0ac)
* Patch file: [2021_7_22_19:09:38-7f85f7b70d947c08f4424bf614b5d66bb6d9a0ac.patch](patch/2021_7_22_19:09:38-7f85f7b70d947c08f4424bf614b5d66bb6d9a0ac.patch)

Correções de matriz de confusão -- Aline
nmodXcompound
nummodXflat:name --> fazer por regra
amodXadvcl
amodXobl

```diff
 # text = Figura 1: Localização da Bacia de Pelotas
 # sent_id = 247-20140910-MONOGRAFIA_0-7
 1	Figura	Figura	PROPN	_	Gender=Fem|Number=Sing	0	root	O	_
-2	1	1	PROPN	_	Number=Sing	1	flat:name	O	_
+2	1	1	NUM	_	Number=Sing	1	nummod	O	_
 3	:	:	PUNCT	_	_	4	punct	O	_
-4	Localização	Localização	PROPN	_	Gender=Fem|Number=Sing	1	appos	O	_
+4	Localização	Localização	PROPN	_	Gender=Fem|Number=Sing	1	parataxis	O	_
 5-6	da	_	_	_	_	_	_	_	_
 5	de	de	ADP	_	_	4	flat:name	O	_
 6	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	4	flat:name	O	_
```

## Obl ou obj: lista de verbos seguidos de "com"

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Mon Jul 26 18:59:17 2021 -0300
* Lines changed: 131
* Commit: [ca33a636f86240ac7be24337dde588cf3e7a6177](https://github.com/alvelvis/meu-mestrado/commit/ca33a636f86240ac7be24337dde588cf3e7a6177)
* Patch file: [2021_7_26_18:59:17-ca33a636f86240ac7be24337dde588cf3e7a6177.patch](patch/2021_7_26_18:59:17-ca33a636f86240ac7be24337dde588cf3e7a6177.patch)

Obl ou obj: lista de verbos seguidos de "com"

```diff
 8	realizado	realizar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part	7	acl	O	_
 9	contou	contar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Past|VerbForm=Fin	0	root	O	_
 10	com	com	ADP	_	_	11	case	O	_
-11	banco	banco	NOUN	_	Gender=Masc|Number=Sing	9	obl	O	_
+11	banco	banco	NOUN	_	Gender=Masc|Number=Sing	9	obj	O	_
 12	de	de	ADP	_	_	13	case	O	_
 13	dados	dado	NOUN	_	Gender=Masc|Number=Plur	11	nmod	O	_
 14	possuindo	possuir	VERB	_	VerbForm=Ger	9	advcl	O	_
```

## Obl ou obj: lista de verbos seguidos de "a"

* Aline Silveira
* Date:   Mon Jul 26 14:16:16 2021 -0300
* Lines changed: 474
* Commit: [e53424fe13dafb1408ab182d05778daba423d23c](https://github.com/alvelvis/meu-mestrado/commit/e53424fe13dafb1408ab182d05778daba423d23c)
* Patch file: [2021_7_26_14:16:16-e53424fe13dafb1408ab182d05778daba423d23c.patch](patch/2021_7_26_14:16:16-e53424fe13dafb1408ab182d05778daba423d23c.patch)

Obl ou obj: lista de verbos seguidos de "a"

```diff
 21	publicados	publicar	VERB	_	Gender=Masc|Number=Plur|VerbForm=Part	20	acl	O	_
 22	a	a	ADP	_	_	24	case	O	_
 23	seu	seu	DET	_	Gender=Masc|Number=Sing|PronType=Prs	24	det	O	_
-24	respeito	respeito	NOUN	_	Gender=Masc|Number=Sing	21	obj	O	_
+24	respeito	respeito	NOUN	_	Gender=Masc|Number=Sing	21	obl	O	_
 25	se	se	SCONJ	_	_	26	mark	O	_
 26	comparada	comparar	VERB	_	Gender=Fem|Number=Sing|VerbForm=Part	18	advcl	O	_
 27-28	às	_	_	_	_	_	_	_	_
```

## Obl ou obj: lista de verbos seguidos de "para"

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Jul 27 11:29:45 2021 -0300
* Lines changed: 41
* Commit: [7df80c015c7842dc385df998d3f8233610eb9da4](https://github.com/alvelvis/meu-mestrado/commit/7df80c015c7842dc385df998d3f8233610eb9da4)
* Patch file: [2021_7_27_11:29:45-7df80c015c7842dc385df998d3f8233610eb9da4.patch](patch/2021_7_27_11:29:45-7df80c015c7842dc385df998d3f8233610eb9da4.patch)

Obl ou obj: lista de verbos seguidos de "para"

```diff
 25	transformado	transformar	VERB	_	Gender=Masc|Number=Sing|VerbForm=Part|Voice=Pass	3	conj	O	_
 26	para	para	ADP	_	_	28	case	O	_
 27	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	28	det	O	_
-28	tempo	tempo	NOUN	_	Gender=Masc|Number=Sing	25	obl	O	_
+28	tempo	tempo	NOUN	_	Gender=Masc|Number=Sing	25	obj	O	_
 29	duplo	duplo	ADJ	_	Gender=Masc|Number=Sing	28	amod	O	_
 30	para	para	SCONJ	_	_	31	mark	O	_
 31	calibrar	calibrar	VERB	_	VerbForm=Inf	25	advcl	O	_
```

## Obl ou obj: lista de verbos seguidos de "por"

* Maria Clara Castro
* Date:   Tue Jul 27 11:31:01 2021 -0300
* Lines changed: 33
* Commit: [2beb4fece79cf40fa68889ea0f297be7b284f67c](https://github.com/alvelvis/meu-mestrado/commit/2beb4fece79cf40fa68889ea0f297be7b284f67c)
* Patch file: [2021_7_27_11:31:01-2beb4fece79cf40fa68889ea0f297be7b284f67c.patch](patch/2021_7_27_11:31:01-2beb4fece79cf40fa68889ea0f297be7b284f67c.patch)

Obl ou obj: lista de verbos seguidos de "por"

```diff
 4-5	pelo	_	_	_	_	_	_	_	_
 4	por	por	ADP	_	_	6	case	O	_
 5	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	6	det	O	_
-6	fato	fato	NOUN	_	Gender=Masc|Number=Sing	3	obj	O	_
+6	fato	fato	NOUN	_	Gender=Masc|Number=Sing	3	obl	O	_
 7-8	da	_	_	_	_	_	_	_	_
 7	de	de	ADP	_	_	9	case	O	_
 8	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	9	det	O	_
```

## Obl ou obj: lista de verbos seguidos de "sobre", "entre" e outros

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Tue Jul 27 16:00:57 2021 -0300
* Lines changed: 39
* Commit: [423ae3bd04bb63dd111c0afc2a888e5f3e375913](https://github.com/alvelvis/meu-mestrado/commit/423ae3bd04bb63dd111c0afc2a888e5f3e375913)
* Patch file: [2021_7_27_16:00:57-423ae3bd04bb63dd111c0afc2a888e5f3e375913.patch](patch/2021_7_27_16:00:57-423ae3bd04bb63dd111c0afc2a888e5f3e375913.patch)

Obl ou obj: lista de verbos seguidos de "sobre", "entre" e outros

```diff
 5	sobre	sobre	ADP	_	_	8	case	O	_
 6	uma	um	DET	_	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	8	det	O	_
 7	antiga	antigo	ADJ	_	Gender=Fem|Number=Sing	8	amod	O	_
-8	zona	zona	NOUN	_	Gender=Fem|Number=Sing	4	obj	O	_
+8	zona	zona	NOUN	_	Gender=Fem|Number=Sing	4	obl	O	_
 9	de	de	ADP	_	_	10	case	O	_
 10	fraqueza	fraqueza	NOUN	_	Gender=Fem|Number=Sing	8	nmod	O	_
 11	,	,	PUNCT	_	_	14	punct	O	_
```

## Comparativas: de_o_que

* Maria Clara Castro
* Date:   Tue Jul 27 21:35:03 2021 -0300
* Lines changed: 52
* Commit: [77289808694d336985848be47702c1bc30c392e1](https://github.com/alvelvis/meu-mestrado/commit/77289808694d336985848be47702c1bc30c392e1)
* Patch file: [2021_7_27_21:35:03-77289808694d336985848be47702c1bc30c392e1.patch](patch/2021_7_27_21:35:03-77289808694d336985848be47702c1bc30c392e1.patch)

Comparativas: de_o_que

```diff
 50	de	de	ADP	_	_	53	case	O	_
 51	o	o	PRON	_	Gender=Masc|Number=Sing|PronType=Dem	50	fixed	O	_
 52	que	que	PRON	_	Gender=Masc|Number=Sing|PronType=Rel	50	fixed	O	_
-53	areia	areia	NOUN	_	Gender=Fem|Number=Sing	44	nmod	B=LITOLOGIA	_
+53	areia	areia	NOUN	_	Gender=Fem|Number=Sing	49	obl	B=LITOLOGIA	_
 54	fina	fino	ADJ	_	Gender=Fem|Number=Sing	53	amod	O	_
 55	e	e	CCONJ	_	_	56	cc	O	_
-56	maior	grande	ADJ	_	Gender=Fem|Number=Sing	54	conj	O	_
+56	maior	grande	ADJ	_	Gender=Fem|Number=Sing	49	conj	O	_
 57-58	do	_	_	_	_	_	_	_	_
 57	de	de	ADP	_	_	60	case	O	_
 58	o	o	PRON	_	Gender=Masc|Number=Sing|PronType=Dem	57	fixed	O	_
 59	que	que	PRON	_	Gender=Masc|Number=Sing|PronType=Rel	57	fixed	O	_
-60	argila	argila	NOUN	_	Gender=Fem|Number=Sing	54	obl	B=LITOLOGIA	_
+60	argila	argila	NOUN	_	Gender=Fem|Number=Sing	56	obl	B=LITOLOGIA	_
 61	e	e	CCONJ	_	_	75	cc	O	_
 62	que	que	PRON	_	Gender=Masc|Number=Sing|PronType=Rel	75	nsubj	O	_
 63-64	na	_	_	_	_	_	_	_	_
```

## Obl ou obj: lista de verbos seguidos de "de"

* Tatiana Cavalcanti
* Date:   Wed Jul 28 14:02:52 2021 -0300
* Lines changed: 222
* Commit: [ee405eb0077f11e3544e022f08b54e38e43cc1a0](https://github.com/alvelvis/meu-mestrado/commit/ee405eb0077f11e3544e022f08b54e38e43cc1a0)
* Patch file: [2021_7_28_14:02:52-ee405eb0077f11e3544e022f08b54e38e43cc1a0.patch](patch/2021_7_28_14:02:52-ee405eb0077f11e3544e022f08b54e38e43cc1a0.patch)

Obl ou obj: lista de verbos seguidos de "de"

```diff
 7-8	do	_	_	_	_	_	_	_	_
 7	de	de	ADP	_	_	9	case	O	_
 8	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	9	det	O	_
-9	sul	sul	NOUN	_	Gender=Masc|Number=Sing	6	obj	O	_
+9	sul	sul	NOUN	_	Gender=Masc|Number=Sing	6	obl	O	_
 10-11	do	_	_	_	_	_	_	_	_
 10	de	de	ADP	_	_	12	case	O	_
 11	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	12	det	O	_
```

## Verbos com lema errado

* Maria Clara Castro
* Date:   Thu Jul 29 17:56:46 2021 -0300
* Lines changed: 251
* Commit: [f62c009cd6744c841225f1631d3c34cc7e655798](https://github.com/alvelvis/meu-mestrado/commit/f62c009cd6744c841225f1631d3c34cc7e655798)
* Patch file: [2021_7_29_17:56:46-f62c009cd6744c841225f1631d3c34cc7e655798.patch](patch/2021_7_29_17:56:46-f62c009cd6744c841225f1631d3c34cc7e655798.patch)

Verbos com lema errado
A correção faz parte do lote de "obj/obl", portanto só foram verificados os verbos seguidos de preposição

```diff
 # text = Boa parte das associações metassedimentares neoproterozóicas do Orógeno Ribeira são de depósitos de margem passiva..
 # sent_id = 247-20140910-MONOGRAFIA_0-76
 1	Boa	bom	ADJ	_	Gender=Fem|Number=Sing	2	amod	O	_
-2	parte	parte	NOUN	_	Gender=Fem|Number=Sing	6	nsubj	O	_
+2	parte	parte	NOUN	_	Gender=Fem|Number=Sing	14	nsubj	O	_
 3-4	das	_	_	_	_	_	_	_	_
 3	de	de	ADP	_	_	5	case	O	_
 4	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	5	det	O	_
 5	associações	associação	NOUN	_	Gender=Fem|Number=Plur	2	nmod	O	_
-6	metassedimentares	metassedimentar	VERB	_	Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
-7	neoproterozóicas	neoproterozóica	NOUN	_	Gender=Fem|Number=Plur	6	obj	O	_
+6	metassedimentares	metassedimentar	ADJ	_	Gender=Fem|Number=Plur	5	amod	O	_
+7	neoproterozóicas	neoproterozóico	ADJ	_	Gender=Fem|Number=Plur	5	amod	O	_
 8-9	do	_	_	_	_	_	_	_	_
 8	de	de	ADP	_	_	10	case	O	_
 9	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	10	det	O	_
-10	Orógeno	Orógeno	PROPN	_	Gender=Masc|Number=Sing	7	nmod	O	_
+10	Orógeno	Orógeno	PROPN	_	Gender=Masc|Number=Sing	5	nmod	O	_
 11	Ribeira	Ribeira	PROPN	_	Number=Sing	10	flat:name	O	_
 12	são	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	14	cop	O	_
 13	de	de	ADP	_	_	14	case	O	_
-14	depósitos	depósito	NOUN	_	Gender=Masc|Number=Plur	6	obl	B=LOCAL:GEO	_
+14	depósitos	depósito	NOUN	_	Gender=Masc|Number=Plur	0	root	B=LOCAL:GEO	_
 15	de	de	ADP	_	_	16	case	O	_
 16	margem	margem	NOUN	_	Gender=Fem|Number=Sing	14	nmod	O	_
 17	passiva	passivo	ADJ	_	Gender=Fem|Number=Sing	16	amod	O	_
```

## Correções de matriz de confusão -- Maria Clara

* Maria Clara Castro
* Date:   Thu Jul 29 18:00:03 2021 -0300
* Lines changed: 33
* Commit: [e12dc3278cb2f818e47a553832c6fb017d27a699](https://github.com/alvelvis/meu-mestrado/commit/e12dc3278cb2f818e47a553832c6fb017d27a699)
* Patch file: [2021_7_29_18:00:03-e12dc3278cb2f818e47a553832c6fb017d27a699.patch](patch/2021_7_29_18:00:03-e12dc3278cb2f818e47a553832c6fb017d27a699.patch)

Correções de matriz de confusão -- Maria Clara
Coisas que ficaram pra trás em: Advmod x case, advmod x cc, compound x nmod e compound x amod.

```diff
 34	forte	forte	ADJ	_	Gender=Masc|Number=Sing	35	amod	O	_
 35	controle	controle	NOUN	_	Gender=Masc|Number=Sing	32	obj	O	_
 36	geomorfológico	geomorfológico	ADJ	_	Gender=Masc|Number=Sing	35	amod	O	_
-37	como	como	ADV	_	_	39	cc	O	_
+37	como	como	SCONJ	_	_	39	mark	O	_
 38	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	39	cop	O	_
-39	possível	possível	ADJ	_	Gender=Masc|Number=Sing	32	conj	O	_
+39	possível	possível	ADJ	_	Gender=Masc|Number=Sing	32	advcl	O	_
 40	visualizar	visualizar	VERB	_	VerbForm=Inf	39	csubj	O	_
 41-42	na	_	_	_	_	_	_	_	_
 41	em	em	ADP	_	_	43	case	O	_
```

## Regra de correção de número(nummod) atrelado a figuras, tabelas, etc

* Aline Silveira
* Date:   Wed Jul 28 15:59:22 2021 -0300
* Lines changed: 1023
* Commit: [a3b245334b32c17efe08509eb9f06c63828598f8](https://github.com/alvelvis/meu-mestrado/commit/a3b245334b32c17efe08509eb9f06c63828598f8)
* Patch file: [2021_7_28_15:59:22-a3b245334b32c17efe08509eb9f06c63828598f8.patch](patch/2021_7_28_15:59:22-a3b245334b32c17efe08509eb9f06c63828598f8.patch)

Regra de correção de número(nummod) atrelado a figuras, tabelas, etc

```diff
 12	brasileira	brasileiro	ADJ	_	Gender=Fem|Number=Sing	11	amod	O	_
 13	(	(	PUNCT	_	_	14	punct	O	_
 14	Figura	Figura	PROPN	_	Gender=Fem|Number=Sing	11	appos	O	_
-15	1	1	PROPN	_	Number=Sing	14	flat:name	O	_
+15	1	1	NUM	_	NumType=Card	14	nummod	O	_
 16	)	)	PUNCT	_	_	14	punct	O	_
 17	e	e	CCONJ	_	_	18	cc	O	_
 18	apresenta	apresentar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	8	conj	O	_
```

## Confusões obl e nmod

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Fri Jul 30 12:46:12 2021 -0300
* Lines changed: 35
* Commit: [4ee4a880b18bf53a004c02240c668bfee158d425](https://github.com/alvelvis/meu-mestrado/commit/4ee4a880b18bf53a004c02240c668bfee158d425)
* Patch file: [2021_7_30_12:46:12-4ee4a880b18bf53a004c02240c668bfee158d425.patch](patch/2021_7_30_12:46:12-4ee4a880b18bf53a004c02240c668bfee158d425.patch)

Confusões obl e nmod

```diff
 26-27	na	_	_	_	_	_	_	_	_
 26	em	em	ADP	_	_	28	case	O	_
 27	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	28	det	O	_
-28	porção	porção	NOUN	_	Gender=Fem|Number=Sing	6	obl	O	_
+28	porção	porção	NOUN	_	Gender=Fem|Number=Sing	18	nmod	O	_
 29	emersa	emerso	ADJ	_	Gender=Fem|Number=Sing	28	amod	O	_
 30	e	e	CCONJ	_	_	32	cc	O	_
 31	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	32	det	O	_
```

## Correções de frases com 2 nsubj, obj ou obl:agent

* Tatiana Cavalcanti
* Date:   Fri Jul 30 12:48:03 2021 -0300
* Lines changed: 738
* Commit: [bcb2f34b6e1ed8e73d303d566a60b151b2622981](https://github.com/alvelvis/meu-mestrado/commit/bcb2f34b6e1ed8e73d303d566a60b151b2622981)
* Patch file: [2021_7_30_12:48:03-bcb2f34b6e1ed8e73d303d566a60b151b2622981.patch](patch/2021_7_30_12:48:03-bcb2f34b6e1ed8e73d303d566a60b151b2622981.patch)

Correções de frases com 2 nsubj, obj ou obl:agent

```diff
 9	6	6	NUM	_	NumType=Card	10	nummod	O	_
 10	camadas	camada	NOUN	_	Gender=Fem|Number=Plur	6	nmod	O	_
 11	sedimentares	sedimentar	ADJ	_	Gender=Fem|Number=Plur	10	amod	O	_
-12	mais	mais	ADV	_	_	14	advmod	O	_
+12	mais	mais	CCONJ	_	_	14	cc	O	_
 13	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	14	det	O	_
-14	tempo	tempo	NOUN	_	Gender=Masc|Number=Sing	4	nsubj:pass	O	_
+14	tempo	tempo	NOUN	_	Gender=Masc|Number=Sing	6	conj	O	_
 15	duplo	duplo	ADJ	_	Gender=Masc|Number=Sing	14	amod	O	_
 16-17	da	_	_	_	_	_	_	_	_
 16	de	de	ADP	_	_	18	case	O	_
 17	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	18	det	O	_
 18	lâmina	lâmina	NOUN	_	Gender=Fem|Number=Sing	14	nmod	O	_
-19	d’água	doáguo	ADJ	_	Gender=Fem|Number=Sing	18	amod	O	_
+19	d’água	d’água	NOUN	_	Gender=Fem|Number=Sing	18	nmod	O	_
 20	.	.	PUNCT	_	_	4	punct	O	_
 21	.	.	PUNCT	_	_	4	punct	O	_
```

## Confusões obl (Stanza) e nmod (UDPipe)

* Maria Clara Castro
* Date:   Mon Aug 2 15:07:18 2021 -0300
* Lines changed: 330
* Commit: [bb6114657ab12253c243e7e22aff8588c93fc81a](https://github.com/alvelvis/meu-mestrado/commit/bb6114657ab12253c243e7e22aff8588c93fc81a)
* Patch file: [2021_8_2_15:07:18-bb6114657ab12253c243e7e22aff8588c93fc81a.patch](patch/2021_8_2_15:07:18-bb6114657ab12253c243e7e22aff8588c93fc81a.patch)

Confusões obl (Stanza) e nmod (UDPipe)

```diff
 16-17	ao	_	_	_	_	_	_	_	_
 16	a	a	ADP	_	_	18	case	O	_
 17	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	18	det	O	_
-18	norte	norte	NOUN	_	Gender=Masc|Number=Sing	6	obl	O	_
+18	norte	norte	NOUN	_	Gender=Masc|Number=Sing	9	nmod	O	_
 19-20	do	_	_	_	_	_	_	_	_
 19	de	de	ADP	_	_	21	case	O	_
 20	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	21	det	O	_
```

## Confusões nmod (Stanza) e obl (UDPipe)

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Aug 4 22:49:15 2021 -0300
* Lines changed: 107
* Commit: [86a4251333c19eb12aa68f92f07d1496288fc456](https://github.com/alvelvis/meu-mestrado/commit/86a4251333c19eb12aa68f92f07d1496288fc456)
* Patch file: [2021_8_4_22:49:15-86a4251333c19eb12aa68f92f07d1496288fc456.patch](patch/2021_8_4_22:49:15-86a4251333c19eb12aa68f92f07d1496288fc456.patch)

Confusões nmod (Stanza) e obl (UDPipe)
Confusões nas teses 411 e 243

```diff
 60	acidentes	acidente	NOUN	_	Gender=Masc|Number=Plur	58	nmod	O	_
 61	contra	contra	ADP	_	_	63	case	O	_
 62	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	63	det	O	_
-63	ecossistema	ecossistema	NOUN	_	Gender=Masc|Number=Sing	58	nmod	O	_
+63	ecossistema	ecossistema	NOUN	_	Gender=Masc|Number=Sing	60	nmod	O	_
 64	..	..	PUNCT	_	_	13	punct	O	_
 # text = O petróleo pode ser liberado no mar de diversas formas, como acidentes durante o percurso dos navios transportadores, durante a lavagem dos tanques dos navios, devido a acidentes nos dutos que o conduzem aos tanques de refino ou por causa de vazamentos nas zonas de extração (GOMES, 2013)..
```

## Confusões nmod (Stanza) e obl (UDPipe)

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Wed Aug 4 23:32:11 2021 -0300
* Lines changed: 35
* Commit: [e9c6ed451f9782b8638081709609ebaaf1fb76bc](https://github.com/alvelvis/meu-mestrado/commit/e9c6ed451f9782b8638081709609ebaaf1fb76bc)
* Patch file: [2021_8_4_23:32:11-e9c6ed451f9782b8638081709609ebaaf1fb76bc.patch](patch/2021_8_4_23:32:11-e9c6ed451f9782b8638081709609ebaaf1fb76bc.patch)

Confusões nmod (Stanza) e obl (UDPipe)
Confusões na tese 391

```diff
 12-13	ao	_	_	_	_	_	_	_	_
 12	a	a	ADP	_	_	14	case	O	_
 13	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	14	det	O	_
-14	meio	meio	NOUN	_	Gender=Masc|Number=Sing	10	nmod	O	_
+14	meio	meio	NOUN	_	Gender=Masc|Number=Sing	11	obl	O	_
 15	ambiente	ambiente	NOUN	_	Gender=Masc|Number=Sing	14	nmod	O	_
 16	é	ser	AUX	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	18	cop	O	_
 17	um	um	DET	_	Definite=Ind|Gender=Masc|Number=Sing|PronType=Art	18	det	O	_
```

## Confusões nmod (Stanza) e obl (UDPipe)

* Aline Silveira
* Date:   Thu Aug 5 09:52:23 2021 -0300
* Lines changed: 450
* Commit: [ebfdad7e50eb29e1a57f831905a2eca5502c8e1a](https://github.com/alvelvis/meu-mestrado/commit/ebfdad7e50eb29e1a57f831905a2eca5502c8e1a)
* Patch file: [2021_8_5_09:52:23-ebfdad7e50eb29e1a57f831905a2eca5502c8e1a.patch](patch/2021_8_5_09:52:23-ebfdad7e50eb29e1a57f831905a2eca5502c8e1a.patch)

Confusões nmod (Stanza) e obl (UDPipe)

```diff
 66	,	,	PUNCT	_	_	69	punct	O	_
 67	para	para	ADP	_	_	69	case	O	_
 68	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	69	det	O	_
-69	bacia	bacia	NOUN	_	Gender=Fem|Number=Sing	60	nmod	B=BACIA:TIPO	_
+69	bacia	bacia	NOUN	_	Gender=Fem|Number=Sing	9	obl	B=BACIA:TIPO	_
 70-71	do	_	_	_	_	_	_	_	_
 70	de	de	ADP	_	_	72	case	O	_
 71	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	72	det	O	_
```

## Confusões nmod (Stanza) e obl (UDPipe)

* Tatiana Cavalcanti
* Date:   Thu Aug 5 09:53:27 2021 -0300
* Lines changed: 544
* Commit: [4ad2b951e1003db40f1a30aa204abacca8dc4c14](https://github.com/alvelvis/meu-mestrado/commit/4ad2b951e1003db40f1a30aa204abacca8dc4c14)
* Patch file: [2021_8_5_09:53:27-4ad2b951e1003db40f1a30aa204abacca8dc4c14.patch](patch/2021_8_5_09:53:27-4ad2b951e1003db40f1a30aa204abacca8dc4c14.patch)

Confusões nmod (Stanza) e obl (UDPipe)

```diff
 15	)	)	PUNCT	_	_	14	punct	O	_
 16	,	,	PUNCT	_	_	18	punct	O	_
 17	em	em	ADP	_	_	18	case	O	_
-18	segundos	segundo	ADJ	_	Gender=Masc|NumType=Ord|Number=Plur	4	obl	O	_
+18	segundos	segundo	ADJ	_	Gender=Masc|NumType=Ord|Number=Plur	12	nmod	O	_
 19	,	,	PUNCT	_	_	24	punct	O	_
 20	e	e	CCONJ	_	_	24	cc	O	_
 21	após	após	ADP	_	_	23	case	O	_
```

## Transformação de obj preposicionados em obl:arg

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Aug 5 10:53:55 2021 -0300
* Lines changed: 1609
* Commit: [57b1696cbaadd3e2877d7685d5d9652cc1ba81ef](https://github.com/alvelvis/meu-mestrado/commit/57b1696cbaadd3e2877d7685d5d9652cc1ba81ef)
* Patch file: [2021_8_5_10:53:55-57b1696cbaadd3e2877d7685d5d9652cc1ba81ef.patch](patch/2021_8_5_10:53:55-57b1696cbaadd3e2877d7685d5d9652cc1ba81ef.patch)

Transformação de obj preposicionados em obl:arg

```diff
 27	a	a	ADP	_	_	30	case	O	_
 28	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	30	det	O	_
 29	outras	outro	DET	_	Gender=Fem|Number=Plur|PronType=Ind	30	det	O	_
-30	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	26	obj	B=BACIA:TIPO	_
+30	bacias	bacia	NOUN	_	Gender=Fem|Number=Plur	26	obl:arg	B=BACIA:TIPO	_
 31	de	de	ADP	_	_	32	case	O	_
 32	margem	margem	NOUN	_	Gender=Fem|Number=Sing	30	nmod	O	_
 33	continental	continental	ADJ	_	Gender=Fem|Number=Sing	32	amod	O	_
```

## Correções de 'tem' como AUX

* Tatiana Cavalcanti
* Date:   Thu Aug 5 13:05:26 2021 -0300
* Lines changed: 141
* Commit: [7ff2ee15b2a0ed18c7cce19f026fb5099b75cc90](https://github.com/alvelvis/meu-mestrado/commit/7ff2ee15b2a0ed18c7cce19f026fb5099b75cc90)
* Patch file: [2021_8_5_13:05:26-7ff2ee15b2a0ed18c7cce19f026fb5099b75cc90.patch](patch/2021_8_5_13:05:26-7ff2ee15b2a0ed18c7cce19f026fb5099b75cc90.patch)

Correções de 'tem' como AUX

```diff
 8	não	não	ADV	_	Polarity=Neg	11	advmod	O	_
 9	tenha	ter	AUX	_	Mood=Sub|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	11	aux	O	_
 10	sido	ser	AUX	_	VerbForm=Part	11	aux	O	_
-11	o	o	PRON	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Dem	1	ccomp	O	_
-12	bastante	bastante	ADJ	_	_	11	amod	O	_
+11	o	o	PRON	_	Gender=Masc|Number=Sing|PronType=Dem	1	ccomp	O	_
+12	bastante	bastante	ADJ	_	Gender=Masc|Number=Sing	11	amod	O	_
 13	para	para	SCONJ	_	_	14	mark	O	_
 14	homogeneizar	homogeneizar	VERB	_	VerbForm=Inf	12	advcl	O	_
 15	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	16	det	O	_
 16	mistura	mistura	NOUN	_	Gender=Fem|Number=Sing	14	obj	O	_
 17	100	100	NUM	_	NumType=Card	18	nummod	O	_
-18	%	%	SYM	_	_	16	nmod	O	_
+18	%	%	SYM	_	_	14	obl	O	_
 19	,	,	PUNCT	_	_	20	punct	O	_
 20	fazendo	fazer	VERB	_	VerbForm=Ger	11	advcl	O	_
 21	com	com	SCONJ	_	_	27	mark	O	_
```

## Correções de root e ciclo

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Aug 5 13:17:15 2021 -0300
* Lines changed: 30
* Commit: [3dc61b031f1841b76092d1464d836ebc81c1c60d](https://github.com/alvelvis/meu-mestrado/commit/3dc61b031f1841b76092d1464d836ebc81c1c60d)
* Patch file: [2021_8_5_13:17:15-3dc61b031f1841b76092d1464d836ebc81c1c60d.patch](patch/2021_8_5_13:17:15-3dc61b031f1841b76092d1464d836ebc81c1c60d.patch)

Correções de root e ciclo

```diff
 4	embasamento	embasamento	NOUN	_	Gender=Masc|Number=Sing	2	nmod	B=UNIDADE_LITOESTRATIGRÁFICA	_
 5	são	ser	AUX	_	Mood=Ind|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	6	aux	O	_
 6-7	subparalelas	_	_	_	_	_	_	_	_
-6	subparale	subparalelo	ADJ	_	Gender=Fem|Number=Plur	0	amod	O	tokenização
+6	subparale	subparalelo	ADJ	_	Gender=Fem|Number=Plur	0	root	O	tokenização
 7	las	elas	PRON	_	Case=Acc|Gender=Fem|Number=Plur|Person=3|PronType=Prs	6	obj	O	_
 8-9	à	_	_	_	_	_	_	_	_
 8	a	a	ADP	_	_	10	case	O	_
```

## Correção do metadado text de algumas sentenças

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Aug 5 13:19:45 2021 -0300
* Lines changed: 204
* Commit: [84ac80a4e62ed96e5343069a819f7293c7398868](https://github.com/alvelvis/meu-mestrado/commit/84ac80a4e62ed96e5343069a819f7293c7398868)
* Patch file: [2021_8_5_13:19:45-84ac80a4e62ed96e5343069a819f7293c7398868.patch](patch/2021_8_5_13:19:45-84ac80a4e62ed96e5343069a819f7293c7398868.patch)

Correção do metadado text de algumas sentenças
Sentenças que foram acopladas durante a fase de sentenciação não tiveram o metadado text atualizado. Com esse pós-processamento, todos os tokens aparecem separados por espaço no metadado text, como vírgulas e pontos finais, mas o problema do acoplamento foi resolvido.
Sentenças modificadas:
241-20140227-MONOGRAFIA_0-17|241-20140227-MONOGRAFIA_0-19|241-20140227-MONOGRAFIA_0-102|241-20140227-MONOGRAFIA_0-115|241-20140227-MONOGRAFIA_0-116|241-20140227-MONOGRAFIA_0-156|241-20140227-MONOGRAFIA_0-195|241-20140227-MONOGRAFIA_0-255|398-20160721-MONOGRAFIA_0-72|398-20160721-MONOGRAFIA_0-74|398-20160721-MONOGRAFIA_0-76|398-20160721-MONOGRAFIA_0-78|398-20160721-MONOGRAFIA_0-80|398-20160721-MONOGRAFIA_0-83|398-20160721-MONOGRAFIA_0-89|398-20160721-MONOGRAFIA_0-91|398-20160721-MONOGRAFIA_0-93|398-20160721-MONOGRAFIA_0-97|398-20160721-MONOGRAFIA_0-103|398-20160721-MONOGRAFIA_0-127|398-20160721-MONOGRAFIA_0-153|398-20160721-MONOGRAFIA_0-173|398-20160721-MONOGRAFIA_0-206|398-20160721-MONOGRAFIA_0-211|398-20160721-MONOGRAFIA_0-392|398-20160721-MONOGRAFIA_0-405|24-20150122-MONOGRAFIA_0-36|24-20150122-MONOGRAFIA_0-37|24-20150122-MONOGRAFIA_0-109|24-20150122-MONOGRAFIA_0-202|24-20150122-MONOGRAFIA_0-276|24-20150122-MONOGRAFIA_0-297|24-20150122-MONOGRAFIA_0-308|24-20150122-MONOGRAFIA_0-354|24-20150122-MONOGRAFIA_0-376|24-20150122-MONOGRAFIA_0-380|24-20150122-MONOGRAFIA_0-594|161-20150810-MONOGRAFIA_0-103|161-20150810-MONOGRAFIA_0-123|161-20150810-MONOGRAFIA_0-234|161-20150810-MONOGRAFIA_0-235|161-20150810-MONOGRAFIA_0-286|161-20150810-MONOGRAFIA_0-288|161-20150810-MONOGRAFIA_0-290|161-20150810-MONOGRAFIA_0-291|161-20150810-MONOGRAFIA_0-320|161-20150810-MONOGRAFIA_0-342|161-20150810-MONOGRAFIA_0-409|161-20150810-MONOGRAFIA_0-410|161-20150810-MONOGRAFIA_0-435|161-20150810-MONOGRAFIA_0-442|161-20150810-MONOGRAFIA_0-447|161-20150810-MONOGRAFIA_0-463|161-20150810-MONOGRAFIA_0-465|161-20150810-MONOGRAFIA_0-505|161-20150810-MONOGRAFIA_0-527|161-20150810-MONOGRAFIA_0-558|161-20150810-MONOGRAFIA_0-596|161-20150810-MONOGRAFIA_0-597|161-20150810-MONOGRAFIA_0-598|161-20150810-MONOGRAFIA_0-609|161-20150810-MONOGRAFIA_0-613|161-20150810-MONOGRAFIA_0-614|161-20150810-MONOGRAFIA_0-616|161-20150810-MONOGRAFIA_0-618|161-20150810-MONOGRAFIA_0-619|161-20150810-MONOGRAFIA_0-633|161-20150810-MONOGRAFIA_0-641|161-20150810-MONOGRAFIA_0-650|161-20150810-MONOGRAFIA_0-670|161-20150810-MONOGRAFIA_0-780|161-20150810-MONOGRAFIA_0-800|161-20150810-MONOGRAFIA_0-814|161-20150810-MONOGRAFIA_0-820|161-20150810-MONOGRAFIA_0-879|334-20150521-MONOGRAFIA_0-36|334-20150521-MONOGRAFIA_0-47|334-20150521-MONOGRAFIA_0-164|334-20150521-MONOGRAFIA_0-165|334-20150521-MONOGRAFIA_0-190|334-20150521-MONOGRAFIA_0-227|334-20150521-MONOGRAFIA_0-266|334-20150521-MONOGRAFIA_0-267|334-20150521-MONOGRAFIA_0-423|334-20150521-MONOGRAFIA_0-424|334-20150521-MONOGRAFIA_0-441|334-20150521-MONOGRAFIA_0-453|334-20150521-MONOGRAFIA_0-503|334-20150521-MONOGRAFIA_0-536|334-20150521-MONOGRAFIA_0-715|202-20140404-MONOGRAFIA_0-41|202-20140404-MONOGRAFIA_0-43|202-20140404-MONOGRAFIA_0-44|258-20160602-TESEMSC_0-26|258-20160602-TESEMSC_0-98|258-20160602-TESEMSC_0-336|258-20160602-TESEMSC_0-343|258-20160602-TESEMSC_0-346|258-20160602-TESEMSC_0-360|258-20160602-TESEMSC_0-362|77-20141209-TESEMSC_0-21|77-20141209-TESEMSC_0-22|77-20141209-TESEMSC_0-186|77-20141209-TESEMSC_0-336|77-20141209-TESEMSC_0-446|279-20140530-MONOGRAFIA_0-23|279-20140530-MONOGRAFIA_0-109|279-20140530-MONOGRAFIA_0-126|279-20140530-MONOGRAFIA_0-145|279-20140530-MONOGRAFIA_0-148|279-20140530-MONOGRAFIA_0-152|279-20140530-MONOGRAFIA_0-215|279-20140530-MONOGRAFIA_0-219|279-20140530-MONOGRAFIA_0-224|279-20140530-MONOGRAFIA_0-243|279-20140530-MONOGRAFIA_0-246|271-20150810-MONOGRAFIA_0-173|271-20150810-MONOGRAFIA_0-179|271-20150810-MONOGRAFIA_0-306|271-20150810-MONOGRAFIA_0-323|271-20150810-MONOGRAFIA_0-333|271-20150810-MONOGRAFIA_0-500|271-20150810-MONOGRAFIA_0-501|391-20160914-MONOGRAFIA_0-97|391-20160914-MONOGRAFIA_0-109|391-20160914-MONOGRAFIA_0-138|391-20160914-MONOGRAFIA_0-184|391-20160914-MONOGRAFIA_0-187|25-20150123-MONOGRAFIA_0-4|25-20150123-MONOGRAFIA_0-19|25-20150123-MONOGRAFIA_0-20|25-20150123-MONOGRAFIA_0-22|25-20150123-MONOGRAFIA_0-24|25-20150123-MONOGRAFIA_0-25|25-20150123-MONOGRAFIA_0-27|25-20150123-MONOGRAFIA_0-28|25-20150123-MONOGRAFIA_0-31|25-20150123-MONOGRAFIA_0-275|25-20150123-MONOGRAFIA_0-276|25-20150123-MONOGRAFIA_0-277|25-20150123-MONOGRAFIA_0-392|20-20140904-TESEDSC_0-42|20-20140904-TESEDSC_0-43|20-20140904-TESEDSC_0-45|20-20140904-TESEDSC_0-48|20-20140904-TESEDSC_0-56|20-20140904-TESEDSC_0-312|20-20140904-TESEDSC_0-380|20-20140904-TESEDSC_0-629|20-20140904-TESEDSC_0-635|20-20140904-TESEDSC_0-1225|20-20140904-TESEDSC_0-1321|119-20141209-TESEMSC_0-33|119-20141209-TESEMSC_0-89|119-20141209-TESEMSC_0-91|119-20141209-TESEMSC_0-116|119-20141209-TESEMSC_0-133|119-20141209-TESEMSC_0-169|119-20141209-TESEMSC_0-170|119-20141209-TESEMSC_0-171|119-20141209-TESEMSC_0-174|119-20141209-TESEMSC_0-290|119-20141209-TESEMSC_0-293|119-20141209-TESEMSC_0-314|119-20141209-TESEMSC_0-345|119-20141209-TESEMSC_0-382|119-20141209-TESEMSC_0-383|119-20141209-TESEMSC_0-389|119-20141209-TESEMSC_0-390|119-20141209-TESEMSC_0-391|119-20141209-TESEMSC_0-407|119-20141209-TESEMSC_0-409|119-20141209-TESEMSC_0-419|119-20141209-TESEMSC_0-424|119-20141209-TESEMSC_0-434|119-20141209-TESEMSC_0-438|119-20141209-TESEMSC_0-463|119-20141209-TESEMSC_0-476|119-20141209-TESEMSC_0-477|119-20141209-TESEMSC_0-478|119-20141209-TESEMSC_0-590|240-20140220-MONOGRAFIA_0-29|240-20140220-MONOGRAFIA_0-35|240-20140220-MONOGRAFIA_0-147|240-20140220-MONOGRAFIA_0-171|240-20140220-MONOGRAFIA_0-175|240-20140220-MONOGRAFIA_0-176|240-20140220-MONOGRAFIA_0-289|240-20140220-MONOGRAFIA_0-302|240-20140220-MONOGRAFIA_0-304|240-20140220-MONOGRAFIA_0-305|240-20140220-MONOGRAFIA_0-306|240-20140220-MONOGRAFIA_0-307|240-20140220-MONOGRAFIA_0-382|240-20140220-MONOGRAFIA_0-399|411-20150702-MONOGRAFIA_0-70|411-20150702-MONOGRAFIA_0-138|411-20150702-MONOGRAFIA_0-161|411-20150702-MONOGRAFIA_0-166|411-20150702-MONOGRAFIA_0-206|411-20150702-MONOGRAFIA_0-242|411-20150702-MONOGRAFIA_0-244|411-20150702-MONOGRAFIA_0-261|243-20141015-MONOGRAFIA_1-14

```diff
 10	:	:	PUNCT	_	_	11	punct	O	_
 11	1..	1..	NUM	_	NumType=Card	0	root	O	_
-# text = Formação do aluno na área de asfaltos;
+# text = Formação do aluno na área de asfaltos ; 2. - Realizar revisão bibliográfica sobre asfaltos e emulsões ; 3. - Preparar asfaltos modificados por vermiculita e avaliar os produtos obtidos fazendo uso dos seguintes ensaios : penetração , ponto de fulgor , ponto de amolecimento , ductilidade e viscosidade Saybolt-Furol . .
 # sent_id = 241-20140227-MONOGRAFIA_0-17
 1	Formação	formação	NOUN	_	Gender=Fem|Number=Sing	0	root	O	_
 2-3	do	_	_	_	_	_	_	_	_
```

## Remoção de pontos finais duplicados -- ponto final seguido de ponto final

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Aug 5 13:29:50 2021 -0300
* Lines changed: 8798
* Commit: [8236a9314137a98221d538bf495e38366eef60e6](https://github.com/alvelvis/meu-mestrado/commit/8236a9314137a98221d538bf495e38366eef60e6)
* Patch file: [2021_8_5_13:29:50-8236a9314137a98221d538bf495e38366eef60e6.patch](patch/2021_8_5_13:29:50-8236a9314137a98221d538bf495e38366eef60e6.patch)

Remoção de pontos finais duplicados -- ponto final seguido de ponto final

```diff
 3	-	-	PUNCT	_	_	4	punct	O	_
 4	INTRODUÇÃO	introdução	NOUN	_	Gender=Fem|Number=Sing	0	root	O	_
-# text = A Bacia de Pelotas é a mais meridional na costa brasileira (Figura 1) e apresenta poucos trabalhos publicados a seu respeito se comparada às outras bacias de margem continental brasileiras..
+# text = A Bacia de Pelotas é a mais meridional na costa brasileira (Figura 1) e apresenta poucos trabalhos publicados a seu respeito se comparada às outras bacias de margem continental brasileiras.
 # sent_id = 247-20140910-MONOGRAFIA_0-2
 1	A	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	O	_
 2	Bacia	bacia	PROPN	_	Gender=Fem|Number=Sing	8	nsubj	B=BACIA:TIPO	_
```

## Remoção de pontos finais duplicados -- tokens de word ".."

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Aug 5 14:08:49 2021 -0300
* Lines changed: 742
* Commit: [fa18597f93b58665bf6775c81c6a26281b195834](https://github.com/alvelvis/meu-mestrado/commit/fa18597f93b58665bf6775c81c6a26281b195834)
* Patch file: [2021_8_5_14:08:49-fa18597f93b58665bf6775c81c6a26281b195834.patch](patch/2021_8_5_14:08:49-fa18597f93b58665bf6775c81c6a26281b195834.patch)

Remoção de pontos finais duplicados -- tokens de word ".."

```diff
 13	de	de	ADP	_	_	15	case	O	_
 14	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	15	det	O	_
 15	Terra	terra	NOUN	_	Gender=Fem|Number=Sing	11	nmod	O	_
-16	..	..	PUNCT	_	_	2	punct	O	_
+16	.	.	PUNCT	_	_	2	punct	O	_
 # text = Estas anomalias podem ser detectadas de modo a fornecer informações sobre a subsuperfície.
 # sent_id = 247-20140910-MONOGRAFIA_0-30
```

## Remoção de pontos finais duplicados -- tokens terminados com ".."

* Tatiana Cavalcanti
* Date:   Thu Aug 5 16:30:49 2021 -0300
* Lines changed: 1037
* Commit: [ea800f94dd0dc29b7c1e151088aca11494e313d4](https://github.com/alvelvis/meu-mestrado/commit/ea800f94dd0dc29b7c1e151088aca11494e313d4)
* Patch file: [2021_8_5_16:30:49-ea800f94dd0dc29b7c1e151088aca11494e313d4.patch](patch/2021_8_5_16:30:49-ea800f94dd0dc29b7c1e151088aca11494e313d4.patch)

Remoção de pontos finais duplicados -- tokens terminados com ".."

```diff
 18	se	se	PRON	_	Case=Acc|Gender=Unsp|Number=Sing|Person=3|PronType=Prs	17	expl	O	_
 19	o	o	DET	_	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	20	det	O	_
 20	programa	programa	NOUN	_	Gender=Masc|Number=Sing	17	obj	O	_
-21	Geographix-Landmark..	Geographix-Landmark..	PROPN	_	Gender=Masc|Number=Sing	20	nmod	O	_
+21	Geographix-Landmark	Geographix-Landmark	PROPN	_	Gender=Masc|Number=Sing	20	nmod	O	_
+22	.	.	PUNCT	_	_	4	punct	_	_
 # text = Após carregar os dados no software Geographix-Landmark, foi realizada a calibração dos poços com o horizonte sísmico através do perfil sônico.
 # sent_id = 247-20140910-MONOGRAFIA_0-47
```

## Remoção de frases mal sentenciadas ou tokenizadas

* Author: Elvis de Souza <elvis.desouza99@gmail.com>
* Date:   Thu Aug 5 17:59:37 2021 -0300
* Lines changed: 0
* Commit: [6e410b3b94c4b36f7cbab1388c444cde823a20a3](https://github.com/alvelvis/meu-mestrado/commit/6e410b3b94c4b36f7cbab1388c444cde823a20a3)
* Patch file: [2021_8_5_17:59:37-6e410b3b94c4b36f7cbab1388c444cde823a20a3.patch](patch/2021_8_5_17:59:37-6e410b3b94c4b36f7cbab1388c444cde823a20a3.patch)

Remoção de frases mal sentenciadas ou tokenizadas
Frases que foram removidas:
119-20141209-TESEMSC_0-412|25-20150123-MONOGRAFIA_0-149|161-20150810-MONOGRAFIA_0-351|258-20160602-TESEMSC_0-173|258-20160602-TESEMSC_0-22|258-20160602-TESEMSC_0-332|258-20160602-TESEMSC_0-269|258-20160602-TESEMSC_0-169|258-20160602-TESEMSC_0-525|20-20140904-TESEDSC_0-312|258-20160602-TESEMSC_0-328|258-20160602-TESEMSC_0-211|258-20160602-TESEMSC_0-60|258-20160602-TESEMSC_0-96|161-20150810-MONOGRAFIA_0-597|258-20160602-TESEMSC_0-131|20-20140904-TESEDSC_0-633|398-20160721-MONOGRAFIA_0-390|258-20160602-TESEMSC_0-145|119-20141209-TESEMSC_0-33|283-20150917-MONOGRAFIA_0-78|258-20160602-TESEMSC_0-302|334-20150521-MONOGRAFIA_0-164|258-20160602-TESEMSC_0-311|283-20150917-MONOGRAFIA_0-96|161-20150810-MONOGRAFIA_0-748|258-20160602-TESEMSC_0-28|271-20150810-MONOGRAFIA_0-323|258-20160602-TESEMSC_0-465|258-20160602-TESEMSC_0-139|258-20160602-TESEMSC_0-184|161-20150810-MONOGRAFIA_0-841|77-20141209-TESEMSC_0-12|25-20150123-MONOGRAFIA_0-152|271-20150810-MONOGRAFIA_0-158|258-20160602-TESEMSC_0-364|258-20160602-TESEMSC_0-322|25-20150123-MONOGRAFIA_0-322|258-20160602-TESEMSC_0-412|247-20140910-MONOGRAFIA_0-239|258-20160602-TESEMSC_0-273|334-20150521-MONOGRAFIA_0-261|202-20140404-MONOGRAFIA_0-59|258-20160602-TESEMSC_0-181|20-20140904-TESEDSC_0-508|411-20150702-MONOGRAFIA_0-341|161-20150810-MONOGRAFIA_0-595|258-20160602-TESEMSC_0-309|258-20160602-TESEMSC_0-47|258-20160602-TESEMSC_0-523|77-20141209-TESEMSC_0-376|279-20140530-MONOGRAFIA_0-215|391-20160914-MONOGRAFIA_0-140|161-20150810-MONOGRAFIA_0-583|258-20160602-TESEMSC_0-80|258-20160602-TESEMSC_0-393|271-20150810-MONOGRAFIA_0-173|258-20160602-TESEMSC_0-154|258-20160602-TESEMSC_0-229|258-20160602-TESEMSC_0-307|258-20160602-TESEMSC_0-303|258-20160602-TESEMSC_0-522|258-20160602-TESEMSC_0-433|119-20141209-TESEMSC_0-178|240-20140220-MONOGRAFIA_0-330|258-20160602-TESEMSC_0-494|271-20150810-MONOGRAFIA_0-43|258-20160602-TESEMSC_0-63|258-20160602-TESEMSC_0-268|258-20160602-TESEMSC_0-326|258-20160602-TESEMSC_0-23|258-20160602-TESEMSC_0-479|258-20160602-TESEMSC_0-382|283-20150917-MONOGRAFIA_0-175|258-20160602-TESEMSC_0-443|258-20160602-TESEMSC_0-357|398-20160721-MONOGRAFIA_0-104|25-20150123-MONOGRAFIA_0-223|258-20160602-TESEMSC_0-249|258-20160602-TESEMSC_0-509|258-20160602-TESEMSC_0-458|243-20141015-MONOGRAFIA_1-277|20-20140904-TESEDSC_0-346|247-20140910-MONOGRAFIA_0-261|279-20140530-MONOGRAFIA_0-51|119-20141209-TESEMSC_0-169|258-20160602-TESEMSC_0-232|284-20150917-MONOGRAFIA_0-96|243-20141015-MONOGRAFIA_1-247|24-20150122-MONOGRAFIA_0-595|334-20150521-MONOGRAFIA_0-400|258-20160602-TESEMSC_0-425|24-20150122-MONOGRAFIA_0-101|283-20150917-MONOGRAFIA_0-77|241-20140227-MONOGRAFIA_0-21|119-20141209-TESEMSC_0-356|279-20140530-MONOGRAFIA_0-46|20-20140904-TESEDSC_0-501|258-20160602-TESEMSC_0-392|258-20160602-TESEMSC_0-290|258-20160602-TESEMSC_0-490|258-20160602-TESEMSC_0-343|258-20160602-TESEMSC_0-439|279-20140530-MONOGRAFIA_0-26|77-20141209-TESEMSC_0-439|258-20160602-TESEMSC_0-375|202-20140404-MONOGRAFIA_0-162|258-20160602-TESEMSC_0-227|271-20150810-MONOGRAFIA_0-215|283-20150917-MONOGRAFIA_0-479|411-20150702-MONOGRAFIA_0-161|411-20150702-MONOGRAFIA_0-162|258-20160602-TESEMSC_0-493|258-20160602-TESEMSC_0-237|258-20160602-TESEMSC_0-151|258-20160602-TESEMSC_0-386|24-20150122-MONOGRAFIA_0-632|258-20160602-TESEMSC_0-384|334-20150521-MONOGRAFIA_0-729|334-20150521-MONOGRAFIA_0-701|258-20160602-TESEMSC_0-339|334-20150521-MONOGRAFIA_0-417|25-20150123-MONOGRAFIA_0-194|20-20140904-TESEDSC_0-1250|119-20141209-TESEMSC_0-425|258-20160602-TESEMSC_0-174|271-20150810-MONOGRAFIA_0-161|284-20150917-MONOGRAFIA_0-182|283-20150917-MONOGRAFIA_0-294|271-20150810-MONOGRAFIA_0-102|258-20160602-TESEMSC_0-219|161-20150810-MONOGRAFIA_0-341|283-20150917-MONOGRAFIA_0-310|258-20160602-TESEMSC_0-18|258-20160602-TESEMSC_0-517|202-20140404-MONOGRAFIA_0-21|24-20150122-MONOGRAFIA_0-215|258-20160602-TESEMSC_0-369|258-20160602-TESEMSC_0-440|258-20160602-TESEMSC_0-349|411-20150702-MONOGRAFIA_0-241|77-20141209-TESEMSC_0-456|25-20150123-MONOGRAFIA_0-347|258-20160602-TESEMSC_0-261|258-20160602-TESEMSC_0-308|258-20160602-TESEMSC_0-324|258-20160602-TESEMSC_0-167|161-20150810-MONOGRAFIA_0-586|20-20140904-TESEDSC_0-555|119-20141209-TESEMSC_0-317|258-20160602-TESEMSC_0-297|258-20160602-TESEMSC_0-158|284-20150917-MONOGRAFIA_0-204|258-20160602-TESEMSC_0-195|258-20160602-TESEMSC_0-11|391-20160914-MONOGRAFIA_0-249|271-20150810-MONOGRAFIA_0-186|161-20150810-MONOGRAFIA_0-641|77-20141209-TESEMSC_0-375|258-20160602-TESEMSC_0-300|161-20150810-MONOGRAFIA_0-284|284-20150917-MONOGRAFIA_0-170|20-20140904-TESEDSC_0-535|258-20160602-TESEMSC_0-491|258-20160602-TESEMSC_0-532|24-20150122-MONOGRAFIA_0-220|258-20160602-TESEMSC_0-427|25-20150123-MONOGRAFIA_0-451|258-20160602-TESEMSC_0-452|20-20140904-TESEDSC_0-109|119-20141209-TESEMSC_0-332|24-20150122-MONOGRAFIA_0-52|258-20160602-TESEMSC_0-105|271-20150810-MONOGRAFIA_0-306|258-20160602-TESEMSC_0-101|334-20150521-MONOGRAFIA_0-707|20-20140904-TESEDSC_0-815|258-20160602-TESEMSC_0-171|20-20140904-TESEDSC_0-1132|258-20160602-TESEMSC_0-350|258-20160602-TESEMSC_0-430|161-20150810-MONOGRAFIA_0-173|258-20160602-TESEMSC_0-76|25-20150123-MONOGRAFIA_0-164|258-20160602-TESEMSC_0-444|258-20160602-TESEMSC_0-374|271-20150810-MONOGRAFIA_0-550|20-20140904-TESEDSC_0-50|258-20160602-TESEMSC_0-388|411-20150702-MONOGRAFIA_0-189|258-20160602-TESEMSC_0-24|258-20160602-TESEMSC_0-9|258-20160602-TESEMSC_0-88|258-20160602-TESEMSC_0-178|258-20160602-TESEMSC_0-225|258-20160602-TESEMSC_0-86|247-20140910-MONOGRAFIA_0-67|258-20160602-TESEMSC_0-344|271-20150810-MONOGRAFIA_0-187|119-20141209-TESEMSC_0-397|258-20160602-TESEMSC_0-183|20-20140904-TESEDSC_0-892|334-20150521-MONOGRAFIA_0-699|258-20160602-TESEMSC_0-104|258-20160602-TESEMSC_0-356|258-20160602-TESEMSC_0-508|283-20150917-MONOGRAFIA_0-189|20-20140904-TESEDSC_0-390|258-20160602-TESEMSC_0-54|283-20150917-MONOGRAFIA_0-346|240-20140220-MONOGRAFIA_0-41|258-20160602-TESEMSC_0-59|258-20160602-TESEMSC_0-516|258-20160602-TESEMSC_0-391|258-20160602-TESEMSC_0-4|258-20160602-TESEMSC_0-135|258-20160602-TESEMSC_0-106|258-20160602-TESEMSC_0-157|283-20150917-MONOGRAFIA_0-227|258-20160602-TESEMSC_0-265|258-20160602-TESEMSC_0-469|258-20160602-TESEMSC_0-351|20-20140904-TESEDSC_0-851|334-20150521-MONOGRAFIA_0-598|258-20160602-TESEMSC_0-353|258-20160602-TESEMSC_0-202|77-20141209-TESEMSC_0-455|334-20150521-MONOGRAFIA_0-538|24-20150122-MONOGRAFIA_0-99|334-20150521-MONOGRAFIA_0-165|202-20140404-MONOGRAFIA_0-140|398-20160721-MONOGRAFIA_0-132|258-20160602-TESEMSC_0-222|258-20160602-TESEMSC_0-39|411-20150702-MONOGRAFIA_0-79|25-20150123-MONOGRAFIA_0-308|119-20141209-TESEMSC_0-676|258-20160602-TESEMSC_0-65|119-20141209-TESEMSC_0-357|258-20160602-TESEMSC_0-447|284-20150917-MONOGRAFIA_0-292|258-20160602-TESEMSC_0-282|411-20150702-MONOGRAFIA_0-68|119-20141209-TESEMSC_0-390|258-20160602-TESEMSC_0-150|258-20160602-TESEMSC_0-435|258-20160602-TESEMSC_0-209|258-20160602-TESEMSC_0-335|25-20150123-MONOGRAFIA_0-456|258-20160602-TESEMSC_0-112|391-20160914-MONOGRAFIA_0-110|258-20160602-TESEMSC_0-345|258-20160602-TESEMSC_0-506|258-20160602-TESEMSC_0-472|161-20150810-MONOGRAFIA_0-533|119-20141209-TESEMSC_0-358|398-20160721-MONOGRAFIA_0-233|258-20160602-TESEMSC_0-464|258-20160602-TESEMSC_0-120|20-20140904-TESEDSC_0-504|258-20160602-TESEMSC_0-368|24-20150122-MONOGRAFIA_0-382|77-20141209-TESEMSC_0-21|279-20140530-MONOGRAFIA_0-243|25-20150123-MONOGRAFIA_0-111|240-20140220-MONOGRAFIA_0-147|258-20160602-TESEMSC_0-453|24-20150122-MONOGRAFIA_0-454|258-20160602-TESEMSC_0-276|398-20160721-MONOGRAFIA_0-187|119-20141209-TESEMSC_0-781|334-20150521-MONOGRAFIA_0-332|258-20160602-TESEMSC_0-281|258-20160602-TESEMSC_0-367|24-20150122-MONOGRAFIA_0-229|283-20150917-MONOGRAFIA_0-452|25-20150123-MONOGRAFIA_0-97|258-20160602-TESEMSC_0-220|334-20150521-MONOGRAFIA_0-697|20-20140904-TESEDSC_0-1083|258-20160602-TESEMSC_0-319|258-20160602-TESEMSC_0-336|258-20160602-TESEMSC_0-114|161-20150810-MONOGRAFIA_0-462|25-20150123-MONOGRAFIA_0-145|258-20160602-TESEMSC_0-215|241-20140227-MONOGRAFIA_0-121|20-20140904-TESEDSC_0-543|398-20160721-MONOGRAFIA_0-331|119-20141209-TESEMSC_0-116|258-20160602-TESEMSC_0-128|258-20160602-TESEMSC_0-240|161-20150810-MONOGRAFIA_0-463|258-20160602-TESEMSC_0-441|283-20150917-MONOGRAFIA_0-167|398-20160721-MONOGRAFIA_0-173|258-20160602-TESEMSC_0-69|258-20160602-TESEMSC_0-334|258-20160602-TESEMSC_0-252|258-20160602-TESEMSC_0-77|258-20160602-TESEMSC_0-161|258-20160602-TESEMSC_0-164|25-20150123-MONOGRAFIA_0-123|258-20160602-TESEMSC_0-485|258-20160602-TESEMSC_0-524|258-20160602-TESEMSC_0-306|258-20160602-TESEMSC_0-223|334-20150521-MONOGRAFIA_0-541|161-20150810-MONOGRAFIA_0-651|258-20160602-TESEMSC_0-132|411-20150702-MONOGRAFIA_0-285|258-20160602-TESEMSC_0-323|258-20160602-TESEMSC_0-395|258-20160602-TESEMSC_0-73|243-20141015-MONOGRAFIA_1-240|24-20150122-MONOGRAFIA_0-490|258-20160602-TESEMSC_0-197|271-20150810-MONOGRAFIA_0-539|258-20160602-TESEMSC_0-347|258-20160602-TESEMSC_0-513|24-20150122-MONOGRAFIA_0-464|258-20160602-TESEMSC_0-348|279-20140530-MONOGRAFIA_0-230|258-20160602-TESEMSC_0-313|258-20160602-TESEMSC_0-446|258-20160602-TESEMSC_0-510|258-20160602-TESEMSC_0-399|258-20160602-TESEMSC_0-199|24-20150122-MONOGRAFIA_0-137|119-20141209-TESEMSC_0-143|24-20150122-MONOGRAFIA_0-34|258-20160602-TESEMSC_0-400|258-20160602-TESEMSC_0-419|258-20160602-TESEMSC_0-480|258-20160602-TESEMSC_0-408|258-20160602-TESEMSC_0-267|161-20150810-MONOGRAFIA_0-598|258-20160602-TESEMSC_0-437|243-20141015-MONOGRAFIA_1-213|334-20150521-MONOGRAFIA_0-243|258-20160602-TESEMSC_0-210|258-20160602-TESEMSC_0-483|258-20160602-TESEMSC_0-380|258-20160602-TESEMSC_0-474|258-20160602-TESEMSC_0-251|283-20150917-MONOGRAFIA_0-345|258-20160602-TESEMSC_0-445|271-20150810-MONOGRAFIA_0-212|24-20150122-MONOGRAFIA_0-211|20-20140904-TESEDSC_0-400|119-20141209-TESEMSC_0-602|258-20160602-TESEMSC_0-36|161-20150810-MONOGRAFIA_0-288|411-20150702-MONOGRAFIA_0-203|258-20160602-TESEMSC_0-238|398-20160721-MONOGRAFIA_0-405|258-20160602-TESEMSC_0-117|258-20160602-TESEMSC_0-192|77-20141209-TESEMSC_0-140|271-20150810-MONOGRAFIA_0-304|258-20160602-TESEMSC_0-162|258-20160602-TESEMSC_0-507|258-20160602-TESEMSC_0-451|20-20140904-TESEDSC_0-500|20-20140904-TESEDSC_0-510|258-20160602-TESEMSC_0-420|24-20150122-MONOGRAFIA_0-143|271-20150810-MONOGRAFIA_0-527|161-20150810-MONOGRAFIA_0-279|258-20160602-TESEMSC_0-448|240-20140220-MONOGRAFIA_0-170|258-20160602-TESEMSC_0-294|258-20160602-TESEMSC_0-239|241-20140227-MONOGRAFIA_0-255|20-20140904-TESEDSC_0-891|258-20160602-TESEMSC_0-404|258-20160602-TESEMSC_0-213|258-20160602-TESEMSC_0-521|258-20160602-TESEMSC_0-16|258-20160602-TESEMSC_0-160|20-20140904-TESEDSC_0-1043|271-20150810-MONOGRAFIA_0-29|258-20160602-TESEMSC_0-45|119-20141209-TESEMSC_0-419|258-20160602-TESEMSC_0-214|25-20150123-MONOGRAFIA_0-118|258-20160602-TESEMSC_0-429|258-20160602-TESEMSC_0-143|258-20160602-TESEMSC_0-274|258-20160602-TESEMSC_0-299|258-20160602-TESEMSC_0-305|334-20150521-MONOGRAFIA_0-129|258-20160602-TESEMSC_0-109|25-20150123-MONOGRAFIA_0-402|258-20160602-TESEMSC_0-461|258-20160602-TESEMSC_0-89|283-20150917-MONOGRAFIA_0-5|119-20141209-TESEMSC_0-469|258-20160602-TESEMSC_0-37|258-20160602-TESEMSC_0-20|24-20150122-MONOGRAFIA_0-129|258-20160602-TESEMSC_0-191|258-20160602-TESEMSC_0-228|258-20160602-TESEMSC_0-177|247-20140910-MONOGRAFIA_0-151|119-20141209-TESEMSC_0-391|334-20150521-MONOGRAFIA_0-342|247-20140910-MONOGRAFIA_0-193|258-20160602-TESEMSC_0-193|258-20160602-TESEMSC_0-255|258-20160602-TESEMSC_0-108|77-20141209-TESEMSC_0-186|258-20160602-TESEMSC_0-301|258-20160602-TESEMSC_0-21|258-20160602-TESEMSC_0-100|411-20150702-MONOGRAFIA_0-287|271-20150810-MONOGRAFIA_0-439|258-20160602-TESEMSC_0-428|20-20140904-TESEDSC_0-865|161-20150810-MONOGRAFIA_0-832|20-20140904-TESEDSC_0-1123|258-20160602-TESEMSC_0-246|334-20150521-MONOGRAFIA_0-692|243-20141015-MONOGRAFIA_1-228|411-20150702-MONOGRAFIA_0-248|258-20160602-TESEMSC_0-317|241-20140227-MONOGRAFIA_0-168|20-20140904-TESEDSC_0-995|258-20160602-TESEMSC_0-2|398-20160721-MONOGRAFIA_0-406|258-20160602-TESEMSC_0-259|20-20140904-TESEDSC_0-864|398-20160721-MONOGRAFIA_0-346|258-20160602-TESEMSC_0-470|161-20150810-MONOGRAFIA_0-103|258-20160602-TESEMSC_0-68|258-20160602-TESEMSC_0-423|202-20140404-MONOGRAFIA_0-88|240-20140220-MONOGRAFIA_0-273|20-20140904-TESEDSC_0-647|258-20160602-TESEMSC_0-85|258-20160602-TESEMSC_0-127|161-20150810-MONOGRAFIA_0-694|258-20160602-TESEMSC_0-497|119-20141209-TESEMSC_0-179|258-20160602-TESEMSC_0-526|258-20160602-TESEMSC_0-296|334-20150521-MONOGRAFIA_0-59|119-20141209-TESEMSC_0-547|411-20150702-MONOGRAFIA_0-156|258-20160602-TESEMSC_0-463|243-20141015-MONOGRAFIA_1-166|258-20160602-TESEMSC_0-530|258-20160602-TESEMSC_0-438|20-20140904-TESEDSC_0-88|258-20160602-TESEMSC_0-329|258-20160602-TESEMSC_0-241|119-20141209-TESEMSC_0-48|271-20150810-MONOGRAFIA_0-211|283-20150917-MONOGRAFIA_0-338|258-20160602-TESEMSC_0-185|24-20150122-MONOGRAFIA_0-376|258-20160602-TESEMSC_0-271|258-20160602-TESEMSC_0-385|334-20150521-MONOGRAFIA_0-709|258-20160602-TESEMSC_0-519|334-20150521-MONOGRAFIA_0-49|20-20140904-TESEDSC_0-1186|258-20160602-TESEMSC_0-138|25-20150123-MONOGRAFIA_0-192|258-20160602-TESEMSC_0-406|258-20160602-TESEMSC_0-14|161-20150810-MONOGRAFIA_0-780|161-20150810-MONOGRAFIA_0-527|391-20160914-MONOGRAFIA_0-250|334-20150521-MONOGRAFIA_0-651|161-20150810-MONOGRAFIA_0-558|258-20160602-TESEMSC_0-168|258-20160602-TESEMSC_0-110|258-20160602-TESEMSC_0-95|411-20150702-MONOGRAFIA_0-206|20-20140904-TESEDSC_0-531|279-20140530-MONOGRAFIA_0-223|283-20150917-MONOGRAFIA_0-249|243-20141015-MONOGRAFIA_1-35|161-20150810-MONOGRAFIA_0-566|258-20160602-TESEMSC_0-487|283-20150917-MONOGRAFIA_0-229|258-20160602-TESEMSC_0-531|258-20160602-TESEMSC_0-293|258-20160602-TESEMSC_0-512|398-20160721-MONOGRAFIA_0-133|25-20150123-MONOGRAFIA_0-190|161-20150810-MONOGRAFIA_0-742|161-20150810-MONOGRAFIA_0-555|258-20160602-TESEMSC_0-346|258-20160602-TESEMSC_0-5|334-20150521-MONOGRAFIA_0-402|202-20140404-MONOGRAFIA_0-114|258-20160602-TESEMSC_0-119|283-20150917-MONOGRAFIA_0-408|119-20141209-TESEMSC_0-463|398-20160721-MONOGRAFIA_0-72|258-20160602-TESEMSC_0-341|391-20160914-MONOGRAFIA_0-246|258-20160602-TESEMSC_0-418|258-20160602-TESEMSC_0-31|283-20150917-MONOGRAFIA_0-42|411-20150702-MONOGRAFIA_0-71|258-20160602-TESEMSC_0-354|258-20160602-TESEMSC_0-492|77-20141209-TESEMSC_0-412|25-20150123-MONOGRAFIA_0-15|258-20160602-TESEMSC_0-304|258-20160602-TESEMSC_0-182|20-20140904-TESEDSC_0-248|391-20160914-MONOGRAFIA_0-233|24-20150122-MONOGRAFIA_0-44|258-20160602-TESEMSC_0-7|24-20150122-MONOGRAFIA_0-151|258-20160602-TESEMSC_0-196|258-20160602-TESEMSC_0-411|279-20140530-MONOGRAFIA_0-84|258-20160602-TESEMSC_0-13|258-20160602-TESEMSC_0-511|258-20160602-TESEMSC_0-288|283-20150917-MONOGRAFIA_0-308|258-20160602-TESEMSC_0-370|241-20140227-MONOGRAFIA_0-170|411-20150702-MONOGRAFIA_0-251|258-20160602-TESEMSC_0-1|77-20141209-TESEMSC_0-289|24-20150122-MONOGRAFIA_0-217|283-20150917-MONOGRAFIA_0-354|20-20140904-TESEDSC_0-1131|258-20160602-TESEMSC_0-124|24-20150122-MONOGRAFIA_0-102|202-20140404-MONOGRAFIA_0-137|119-20141209-TESEMSC_0-308|20-20140904-TESEDSC_0-357|258-20160602-TESEMSC_0-147|271-20150810-MONOGRAFIA_0-333|258-20160602-TESEMSC_0-149|247-20140910-MONOGRAFIA_0-124|334-20150521-MONOGRAFIA_0-720|258-20160602-TESEMSC_0-417|247-20140910-MONOGRAFIA_0-86|119-20141209-TESEMSC_0-316|258-20160602-TESEMSC_0-504|258-20160602-TESEMSC_0-289|258-20160602-TESEMSC_0-422|161-20150810-MONOGRAFIA_0-613|258-20160602-TESEMSC_0-325|258-20160602-TESEMSC_0-403|20-20140904-TESEDSC_0-1168|161-20150810-MONOGRAFIA_0-359|24-20150122-MONOGRAFIA_0-66|161-20150810-MONOGRAFIA_0-500|20-20140904-TESEDSC_0-352|271-20150810-MONOGRAFIA_0-347|258-20160602-TESEMSC_0-387|258-20160602-TESEMSC_0-321|279-20140530-MONOGRAFIA_0-224|20-20140904-TESEDSC_0-712|279-20140530-MONOGRAFIA_0-125|119-20141209-TESEMSC_0-571|258-20160602-TESEMSC_0-360|258-20160602-TESEMSC_0-156|258-20160602-TESEMSC_0-221|258-20160602-TESEMSC_0-190|258-20160602-TESEMSC_0-515|258-20160602-TESEMSC_0-398|161-20150810-MONOGRAFIA_0-381|20-20140904-TESEDSC_0-582|258-20160602-TESEMSC_0-514|24-20150122-MONOGRAFIA_0-594|258-20160602-TESEMSC_0-144|258-20160602-TESEMSC_0-310|258-20160602-TESEMSC_0-431|258-20160602-TESEMSC_0-333|241-20140227-MONOGRAFIA_0-123|119-20141209-TESEMSC_0-28|411-20150702-MONOGRAFIA_0-113|243-20141015-MONOGRAFIA_1-234|258-20160602-TESEMSC_0-498|271-20150810-MONOGRAFIA_0-160|258-20160602-TESEMSC_0-200|258-20160602-TESEMSC_0-3|411-20150702-MONOGRAFIA_0-77|119-20141209-TESEMSC_0-407|241-20140227-MONOGRAFIA_0-253|20-20140904-TESEDSC_0-452|119-20141209-TESEMSC_0-274|258-20160602-TESEMSC_0-43|334-20150521-MONOGRAFIA_0-47|258-20160602-TESEMSC_0-189|161-20150810-MONOGRAFIA_0-293|258-20160602-TESEMSC_0-454|258-20160602-TESEMSC_0-208|258-20160602-TESEMSC_0-456|258-20160602-TESEMSC_0-12|258-20160602-TESEMSC_0-155|161-20150810-MONOGRAFIA_0-469|161-20150810-MONOGRAFIA_0-800|243-20141015-MONOGRAFIA_1-246|258-20160602-TESEMSC_0-231|258-20160602-TESEMSC_0-283|258-20160602-TESEMSC_0-90|161-20150810-MONOGRAFIA_0-922|258-20160602-TESEMSC_0-489|161-20150810-MONOGRAFIA_0-372|258-20160602-TESEMSC_0-477|258-20160602-TESEMSC_0-278|161-20150810-MONOGRAFIA_0-691|258-20160602-TESEMSC_0-84|119-20141209-TESEMSC_0-590|258-20160602-TESEMSC_0-118|258-20160602-TESEMSC_0-94|258-20160602-TESEMSC_0-176|398-20160721-MONOGRAFIA_0-243|247-20140910-MONOGRAFIA_0-258|411-20150702-MONOGRAFIA_0-289|258-20160602-TESEMSC_0-254|258-20160602-TESEMSC_0-462|411-20150702-MONOGRAFIA_0-80|240-20140220-MONOGRAFIA_0-289|258-20160602-TESEMSC_0-230|258-20160602-TESEMSC_0-390|258-20160602-TESEMSC_0-130|258-20160602-TESEMSC_0-295|258-20160602-TESEMSC_0-142|258-20160602-TESEMSC_0-402|77-20141209-TESEMSC_0-440|334-20150521-MONOGRAFIA_0-503|258-20160602-TESEMSC_0-468|279-20140530-MONOGRAFIA_0-239|258-20160602-TESEMSC_0-258|258-20160602-TESEMSC_0-275|77-20141209-TESEMSC_0-22|161-20150810-MONOGRAFIA_0-292|334-20150521-MONOGRAFIA_0-542|20-20140904-TESEDSC_0-344|334-20150521-MONOGRAFIA_0-705|77-20141209-TESEMSC_0-457|258-20160602-TESEMSC_0-409|24-20150122-MONOGRAFIA_0-47|20-20140904-TESEDSC_0-37|284-20150917-MONOGRAFIA_0-53|283-20150917-MONOGRAFIA_0-176|258-20160602-TESEMSC_0-285|258-20160602-TESEMSC_0-79|258-20160602-TESEMSC_0-50|258-20160602-TESEMSC_0-527|258-20160602-TESEMSC_0-263|24-20150122-MONOGRAFIA_0-276|258-20160602-TESEMSC_0-363|24-20150122-MONOGRAFIA_0-42|258-20160602-TESEMSC_0-53|161-20150810-MONOGRAFIA_0-553|20-20140904-TESEDSC_0-36|258-20160602-TESEMSC_0-316|258-20160602-TESEMSC_0-481|334-20150521-MONOGRAFIA_0-695|258-20160602-TESEMSC_0-179|258-20160602-TESEMSC_0-46|258-20160602-TESEMSC_0-460|240-20140220-MONOGRAFIA_0-35|258-20160602-TESEMSC_0-87|334-20150521-MONOGRAFIA_0-51|258-20160602-TESEMSC_0-373|24-20150122-MONOGRAFIA_0-90|258-20160602-TESEMSC_0-434|258-20160602-TESEMSC_0-116|258-20160602-TESEMSC_0-224|161-20150810-MONOGRAFIA_0-814|258-20160602-TESEMSC_0-266|119-20141209-TESEMSC_0-605|411-20150702-MONOGRAFIA_0-283|258-20160602-TESEMSC_0-61|20-20140904-TESEDSC_0-1222|258-20160602-TESEMSC_0-499|258-20160602-TESEMSC_0-35|258-20160602-TESEMSC_0-70|77-20141209-TESEMSC_0-118|77-20141209-TESEMSC_0-460|240-20140220-MONOGRAFIA_0-357|258-20160602-TESEMSC_0-518|20-20140904-TESEDSC_0-538|258-20160602-TESEMSC_0-256|77-20141209-TESEMSC_0-426|20-20140904-TESEDSC_0-43|258-20160602-TESEMSC_0-243|258-20160602-TESEMSC_0-71|258-20160602-TESEMSC_0-407|240-20140220-MONOGRAFIA_0-20|258-20160602-TESEMSC_0-245|258-20160602-TESEMSC_0-207|279-20140530-MONOGRAFIA_0-42|258-20160602-TESEMSC_0-330|258-20160602-TESEMSC_0-442|258-20160602-TESEMSC_0-113|241-20140227-MONOGRAFIA_0-246|77-20141209-TESEMSC_0-442|258-20160602-TESEMSC_0-450|258-20160602-TESEMSC_0-74|258-20160602-TESEMSC_0-415|258-20160602-TESEMSC_0-29|258-20160602-TESEMSC_0-30|161-20150810-MONOGRAFIA_0-443|258-20160602-TESEMSC_0-180|258-20160602-TESEMSC_0-270|279-20140530-MONOGRAFIA_0-103|258-20160602-TESEMSC_0-257|258-20160602-TESEMSC_0-111|258-20160602-TESEMSC_0-244|391-20160914-MONOGRAFIA_0-26|258-20160602-TESEMSC_0-264|271-20150810-MONOGRAFIA_0-135|258-20160602-TESEMSC_0-292|161-20150810-MONOGRAFIA_0-702|258-20160602-TESEMSC_0-320|258-20160602-TESEMSC_0-72|20-20140904-TESEDSC_0-1241|258-20160602-TESEMSC_0-502|240-20140220-MONOGRAFIA_0-442|258-20160602-TESEMSC_0-342|258-20160602-TESEMSC_0-172|25-20150123-MONOGRAFIA_0-180|271-20150810-MONOGRAFIA_0-33|24-20150122-MONOGRAFIA_0-105|258-20160602-TESEMSC_0-475|258-20160602-TESEMSC_0-81|258-20160602-TESEMSC_0-242|258-20160602-TESEMSC_0-134|243-20141015-MONOGRAFIA_1-9|20-20140904-TESEDSC_0-176|284-20150917-MONOGRAFIA_0-75|258-20160602-TESEMSC_0-203|20-20140904-TESEDSC_0-948|258-20160602-TESEMSC_0-64|258-20160602-TESEMSC_0-206|258-20160602-TESEMSC_0-362|161-20150810-MONOGRAFIA_0-822|258-20160602-TESEMSC_0-366|258-20160602-TESEMSC_0-235|258-20160602-TESEMSC_0-389|25-20150123-MONOGRAFIA_0-112|258-20160602-TESEMSC_0-97|258-20160602-TESEMSC_0-102|258-20160602-TESEMSC_0-34|258-20160602-TESEMSC_0-66|271-20150810-MONOGRAFIA_0-529|258-20160602-TESEMSC_0-58|258-20160602-TESEMSC_0-455|20-20140904-TESEDSC_0-1333|258-20160602-TESEMSC_0-123|161-20150810-MONOGRAFIA_0-838|258-20160602-TESEMSC_0-277|119-20141209-TESEMSC_0-271|77-20141209-TESEMSC_0-92|161-20150810-MONOGRAFIA_0-614|258-20160602-TESEMSC_0-38|258-20160602-TESEMSC_0-218|258-20160602-TESEMSC_0-175|240-20140220-MONOGRAFIA_0-381|258-20160602-TESEMSC_0-186|240-20140220-MONOGRAFIA_0-65|20-20140904-TESEDSC_0-20|258-20160602-TESEMSC_0-298|258-20160602-TESEMSC_0-233|271-20150810-MONOGRAFIA_0-363|258-20160602-TESEMSC_0-26|258-20160602-TESEMSC_0-476|258-20160602-TESEMSC_0-51|119-20141209-TESEMSC_0-669|258-20160602-TESEMSC_0-478|247-20140910-MONOGRAFIA_0-174|119-20141209-TESEMSC_0-132|258-20160602-TESEMSC_0-457|161-20150810-MONOGRAFIA_0-395|161-20150810-MONOGRAFIA_0-342|119-20141209-TESEMSC_0-370|258-20160602-TESEMSC_0-205|247-20140910-MONOGRAFIA_0-44|258-20160602-TESEMSC_0-405|258-20160602-TESEMSC_0-52|279-20140530-MONOGRAFIA_0-236|258-20160602-TESEMSC_0-262|119-20141209-TESEMSC_0-738|258-20160602-TESEMSC_0-484|283-20150917-MONOGRAFIA_0-392|391-20160914-MONOGRAFIA_0-216|258-20160602-TESEMSC_0-361|334-20150521-MONOGRAFIA_0-721|119-20141209-TESEMSC_0-657|279-20140530-MONOGRAFIA_0-232|258-20160602-TESEMSC_0-201|161-20150810-MONOGRAFIA_0-677|271-20150810-MONOGRAFIA_0-369|20-20140904-TESEDSC_0-1129|25-20150123-MONOGRAFIA_0-220|119-20141209-TESEMSC_0-361|258-20160602-TESEMSC_0-188|25-20150123-MONOGRAFIA_0-244|258-20160602-TESEMSC_0-103|161-20150810-MONOGRAFIA_0-426|258-20160602-TESEMSC_0-424|258-20160602-TESEMSC_0-198|283-20150917-MONOGRAFIA_0-141|258-20160602-TESEMSC_0-284|247-20140910-MONOGRAFIA_0-235|240-20140220-MONOGRAFIA_0-191|20-20140904-TESEDSC_0-685|334-20150521-MONOGRAFIA_0-722|284-20150917-MONOGRAFIA_0-167|258-20160602-TESEMSC_0-236|398-20160721-MONOGRAFIA_0-174|258-20160602-TESEMSC_0-426|258-20160602-TESEMSC_0-248|258-20160602-TESEMSC_0-32|258-20160602-TESEMSC_0-40|24-20150122-MONOGRAFIA_0-43|258-20160602-TESEMSC_0-291|258-20160602-TESEMSC_0-505|258-20160602-TESEMSC_0-432|258-20160602-TESEMSC_0-163|258-20160602-TESEMSC_0-365|258-20160602-TESEMSC_0-98|161-20150810-MONOGRAFIA_0-830|20-20140904-TESEDSC_0-48|20-20140904-TESEDSC_0-56|258-20160602-TESEMSC_0-153|258-20160602-TESEMSC_0-136|258-20160602-TESEMSC_0-27|161-20150810-MONOGRAFIA_0-575|241-20140227-MONOGRAFIA_0-102|241-20140227-MONOGRAFIA_0-116|161-20150810-MONOGRAFIA_0-632|258-20160602-TESEMSC_0-396|258-20160602-TESEMSC_0-159|284-20150917-MONOGRAFIA_0-249|258-20160602-TESEMSC_0-529|161-20150810-MONOGRAFIA_0-361|161-20150810-MONOGRAFIA_0-821|258-20160602-TESEMSC_0-141|258-20160602-TESEMSC_0-133|258-20160602-TESEMSC_0-520|334-20150521-MONOGRAFIA_0-284|334-20150521-MONOGRAFIA_0-715|334-20150521-MONOGRAFIA_0-185|258-20160602-TESEMSC_0-376|258-20160602-TESEMSC_0-331|20-20140904-TESEDSC_0-391|258-20160602-TESEMSC_0-379|258-20160602-TESEMSC_0-44|334-20150521-MONOGRAFIA_0-710|283-20150917-MONOGRAFIA_0-350|258-20160602-TESEMSC_0-6|20-20140904-TESEDSC_0-1041|258-20160602-TESEMSC_0-41|258-20160602-TESEMSC_0-91|258-20160602-TESEMSC_0-358|258-20160602-TESEMSC_0-378|258-20160602-TESEMSC_0-165|283-20150917-MONOGRAFIA_0-464|398-20160721-MONOGRAFIA_0-211|258-20160602-TESEMSC_0-459|411-20150702-MONOGRAFIA_0-72|161-20150810-MONOGRAFIA_0-266|334-20150521-MONOGRAFIA_0-677|77-20141209-TESEMSC_0-150|258-20160602-TESEMSC_0-467|24-20150122-MONOGRAFIA_0-299|258-20160602-TESEMSC_0-280|258-20160602-TESEMSC_0-397|258-20160602-TESEMSC_0-194|119-20141209-TESEMSC_0-89|258-20160602-TESEMSC_0-401|258-20160602-TESEMSC_0-67|161-20150810-MONOGRAFIA_0-700|411-20150702-MONOGRAFIA_0-51|258-20160602-TESEMSC_0-187|258-20160602-TESEMSC_0-107|243-20141015-MONOGRAFIA_1-30|119-20141209-TESEMSC_0-476|271-20150810-MONOGRAFIA_0-291|20-20140904-TESEDSC_0-45|258-20160602-TESEMSC_0-473|20-20140904-TESEDSC_0-166|283-20150917-MONOGRAFIA_0-298|258-20160602-TESEMSC_0-371|258-20160602-TESEMSC_0-496|258-20160602-TESEMSC_0-140|25-20150123-MONOGRAFIA_0-321|25-20150123-MONOGRAFIA_0-92|241-20140227-MONOGRAFIA_0-195|258-20160602-TESEMSC_0-148|161-20150810-MONOGRAFIA_0-465|258-20160602-TESEMSC_0-15|283-20150917-MONOGRAFIA_0-219|24-20150122-MONOGRAFIA_0-128|20-20140904-TESEDSC_0-1212|258-20160602-TESEMSC_0-93|119-20141209-TESEMSC_0-351|258-20160602-TESEMSC_0-56|258-20160602-TESEMSC_0-170|258-20160602-TESEMSC_0-99|258-20160602-TESEMSC_0-495|283-20150917-MONOGRAFIA_0-357|20-20140904-TESEDSC_0-931|258-20160602-TESEMSC_0-315|258-20160602-TESEMSC_0-204|20-20140904-TESEDSC_0-624|258-20160602-TESEMSC_0-48|20-20140904-TESEDSC_0-101|20-20140904-TESEDSC_0-222|283-20150917-MONOGRAFIA_0-343|161-20150810-MONOGRAFIA_0-123|25-20150123-MONOGRAFIA_0-254|258-20160602-TESEMSC_0-83|284-20150917-MONOGRAFIA_0-263|258-20160602-TESEMSC_0-413|258-20160602-TESEMSC_0-10|202-20140404-MONOGRAFIA_0-131|258-20160602-TESEMSC_0-25|258-20160602-TESEMSC_0-381|258-20160602-TESEMSC_0-312|241-20140227-MONOGRAFIA_0-124|258-20160602-TESEMSC_0-338|258-20160602-TESEMSC_0-126|258-20160602-TESEMSC_0-394|24-20150122-MONOGRAFIA_0-627|119-20141209-TESEMSC_0-82|258-20160602-TESEMSC_0-115|258-20160602-TESEMSC_0-500|258-20160602-TESEMSC_0-416|258-20160602-TESEMSC_0-166|258-20160602-TESEMSC_0-260|247-20140910-MONOGRAFIA_0-294|283-20150917-MONOGRAFIA_0-394|258-20160602-TESEMSC_0-352|391-20160914-MONOGRAFIA_0-56|241-20140227-MONOGRAFIA_0-210|258-20160602-TESEMSC_0-410|258-20160602-TESEMSC_0-253|20-20140904-TESEDSC_0-1243|258-20160602-TESEMSC_0-340|258-20160602-TESEMSC_0-57|258-20160602-TESEMSC_0-212|161-20150810-MONOGRAFIA_0-281|258-20160602-TESEMSC_0-33|258-20160602-TESEMSC_0-234|247-20140910-MONOGRAFIA_0-11|258-20160602-TESEMSC_0-216|258-20160602-TESEMSC_0-8|24-20150122-MONOGRAFIA_0-104|119-20141209-TESEMSC_0-438|258-20160602-TESEMSC_0-152|20-20140904-TESEDSC_0-882|258-20160602-TESEMSC_0-279|25-20150123-MONOGRAFIA_0-392|258-20160602-TESEMSC_0-383|258-20160602-TESEMSC_0-129|258-20160602-TESEMSC_0-217|161-20150810-MONOGRAFIA_0-844|284-20150917-MONOGRAFIA_0-185|258-20160602-TESEMSC_0-250|411-20150702-MONOGRAFIA_0-286|161-20150810-MONOGRAFIA_0-66|258-20160602-TESEMSC_0-272|258-20160602-TESEMSC_0-327|258-20160602-TESEMSC_0-372|119-20141209-TESEMSC_0-470|119-20141209-TESEMSC_0-326|411-20150702-MONOGRAFIA_0-242|258-20160602-TESEMSC_0-62|258-20160602-TESEMSC_0-49|258-20160602-TESEMSC_0-121|279-20140530-MONOGRAFIA_0-126|258-20160602-TESEMSC_0-247|258-20160602-TESEMSC_0-287|258-20160602-TESEMSC_0-528|258-20160602-TESEMSC_0-146|202-20140404-MONOGRAFIA_0-116|258-20160602-TESEMSC_0-488|241-20140227-MONOGRAFIA_0-193|20-20140904-TESEDSC_0-636|334-20150521-MONOGRAFIA_0-578|258-20160602-TESEMSC_0-17|258-20160602-TESEMSC_0-122|161-20150810-MONOGRAFIA_0-294|284-20150917-MONOGRAFIA_0-25|20-20140904-TESEDSC_0-842|271-20150810-MONOGRAFIA_0-277|258-20160602-TESEMSC_0-42|271-20150810-MONOGRAFIA_0-196|258-20160602-TESEMSC_0-226|258-20160602-TESEMSC_0-318|247-20140910-MONOGRAFIA_0-50|258-20160602-TESEMSC_0-414|258-20160602-TESEMSC_0-377|258-20160602-TESEMSC_0-82|24-20150122-MONOGRAFIA_0-629|258-20160602-TESEMSC_0-359|258-20160602-TESEMSC_0-421|20-20140904-TESEDSC_0-42|284-20150917-MONOGRAFIA_0-324|258-20160602-TESEMSC_0-471|161-20150810-MONOGRAFIA_0-695|258-20160602-TESEMSC_0-125|284-20150917-MONOGRAFIA_0-425|20-20140904-TESEDSC_0-506|258-20160602-TESEMSC_0-355|271-20150810-MONOGRAFIA_0-240|258-20160602-TESEMSC_0-449|20-20140904-TESEDSC_0-912|334-20150521-MONOGRAFIA_0-253|243-20141015-MONOGRAFIA_1-274|20-20140904-TESEDSC_0-551|258-20160602-TESEMSC_0-337|258-20160602-TESEMSC_0-482|258-20160602-TESEMSC_0-19|77-20141209-TESEMSC_0-79|258-20160602-TESEMSC_0-75|25-20150123-MONOGRAFIA_0-278|334-20150521-MONOGRAFIA_0-394|258-20160602-TESEMSC_0-92|119-20141209-TESEMSC_0-253|258-20160602-TESEMSC_0-137|247-20140910-MONOGRAFIA_0-83|20-20140904-TESEDSC_0-1154|240-20140220-MONOGRAFIA_0-151|258-20160602-TESEMSC_0-501|243-20141015-MONOGRAFIA_1-238|119-20141209-TESEMSC_0-383|258-20160602-TESEMSC_0-466|20-20140904-TESEDSC_0-1006|258-20160602-TESEMSC_0-55|258-20160602-TESEMSC_0-503|279-20140530-MONOGRAFIA_0-27|258-20160602-TESEMSC_0-286|258-20160602-TESEMSC_0-314|258-20160602-TESEMSC_0-486|258-20160602-TESEMSC_0-436|284-20150917-MONOGRAFIA_0-154|398-20160721-MONOGRAFIA_0-188|258-20160602-TESEMSC_0-78|77-20141209-TESEMSC_0-458

```diff
 36	sísmica	sísmico	ADJ	_	Gender=Fem|Number=Sing	35	amod	B=MÉTODO	_
 37	.	.	PUNCT	_	_	4	punct	O	_
-# text = Busca-se analisar as estruturas continentais que possam apresentar continuidade na bacia de Pelotas (“Lineamento Tibagi” e “Sinclinal de Torres”), verificando sua influência na evolução e deformação da mesma.
-# sent_id = 247-20140910-MONOGRAFIA_0-11
-1-2	Busca-se	_	_	_	_	_	_	_	_
-1	Busca	buscar	VERB	_	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	O	_
-2	se	se	PRON	_	Case=Acc|Gender=Unsp|PronType=Prs	1	expl	O	_
-3	analisar	analisar	VERB	_	VerbForm=Inf	1	xcomp	O	_
-4	as	o	DET	_	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	5	det	O	_
-5	estruturas	estrutura	NOUN	_	Gender=Fem|Number=Plur	3	obj	O	_
-6	continentais	continental	ADJ	_	Gender=Fem|Number=Plur	5	amod	O	_
-7	que	que	PRON	_	Gender=Fem|Number=Plur|PronType=Rel	8	nsubj	O	_
-8	possam	poder	VERB	_	Mood=Sub|Number=Plur|Person=3|Tense=Pres|VerbForm=Fin	5	acl:relcl	O	_
-9	apresentar	apresentar	VERB	_	VerbForm=Inf	8	xcomp	O	_
-10	continuidade	continuidade	NOUN	_	Gender=Fem|Number=Sing	9	obj	O	_
-11-12	na	_	_	_	_	_	_	_	_
-11	em	em	ADP	_	_	13	case	O	_
-12	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	13	det	O	_
-13	bacia	bacia	NOUN	_	Gender=Fem|Number=Sing	9	obl	B=BACIA:TIPO	_
-14	de	de	ADP	_	_	15	case	O	_
-15	Pelotas	Pelotas	PROPN	_	Gender=Unsp|Number=Sing	13	nmod	B=BACIA	_
-16	(	(	PUNCT	_	_	17	punct	O	_
-17	“	“	PROPN	_	Gender=Masc|Number=Sing	15	appos	O	_
-18	Lineamento	Lineamento	PROPN	_	Gender=Masc|Number=Sing	17	flat:name	O	_
-19	Tibagi”	Tibagi”	PROPN	_	Number=Sing	17	flat:name	O	tokenização
-20	e	e	CCONJ	_	_	21	cc	O	_
-21	“	“	PROPN	_	Gender=Masc|Number=Sing	17	conj	O	_
-22	Sinclinal	Sinclinal	PROPN	_	Number=Sing	21	flat:name	O	_
-23	de	de	ADP	_	_	21	flat:name	O	_
-24	Torres”	Torres”	PROPN	_	Number=Sing	21	flat:name	O	tokenização
-25	)	)	PUNCT	_	_	17	punct	O	_
-26	,	,	PUNCT	_	_	27	punct	O	_
-27	verificando	verificar	VERB	_	VerbForm=Ger	9	advcl	O	_
-28	sua	seu	DET	_	Gender=Fem|Number=Sing|PronType=Prs	29	det	O	_
-29	influência	influência	NOUN	_	Gender=Fem|Number=Sing	27	obj	O	_
-30-31	na	_	_	_	_	_	_	_	_
-30	em	em	ADP	_	_	32	case	O	_
-31	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	32	det	O	_
-32	evolução	evolução	NOUN	_	Gender=Fem|Number=Sing	27	obl	O	_
-33	e	e	CCONJ	_	_	34	cc	O	_
-34	deformação	deformação	NOUN	_	Gender=Fem|Number=Sing	32	conj	O	_
-35-36	da	_	_	_	_	_	_	_	_
-35	de	de	ADP	_	_	37	case	O	_
-36	a	o	DET	_	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	37	det	O	_
-37	mesma	mesmo	PRON	_	Gender=Fem|Number=Sing|PronType=Dem	34	nmod	O	_
-38	.	.	PUNCT	_	_	1	punct	O	_
-
 # text = 3. - LOCALIZAÇÃO DA ÁREA DE ESTUDO
 # sent_id = 247-20140910-MONOGRAFIA_0-12
 1	3	3	NUM	_	NumType=Card	4	parataxis	O	_
```