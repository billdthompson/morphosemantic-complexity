# Summary

UD Estonian is a conversion of a subpart of Estonian Dependency Treebank (EDT), originally annotated in the Constraint Grammar (CG) annotation scheme, and consisting of genres of fiction, newspaper texts and scientific texts.

# Introduction

The Estonian UD v2.1 treebank contains a subpart of UD v1.3 treebank which has been automatically converted and then manually reviewed and reannotated.

The original texts belong to the following text genres:

* fiction (58504 tokens, 48175 tokens without punctuation, 5148 sentences): ilu_indrikson_ud2.conllu, ilu_kanep_ud2.conllu, ilu_kivirahk_ud2.conllu, ilu_maailm_ud2.conllu, ilu_orlau_ud2.conllu, ilu_remsu_ud2.conllu, ilu_ruben_ud2.conllu, ilu_valton_ud2.conllu, ilu_vilep_ud2.conllu; 

* newspapers (18179 tokens, 15089 tokens without punctuation, 1198 sentences): aja_epl20070812_ud2.conllu, aja_sloleht20071217_ud2.conllu; 

* scientific text (20362 tokens, 17683 tokens without punctuation, 1127 sentences): tea_toohoive_ud2.conllu.

* Also, the subpart of Estonian part of HamleDT 3.0 treebank has been reannotated and included in the treebank; it contains 9200 tokens.

The Estonian UD treebank is based on the [Estonian Dependency Treebank] (https://github.com/EstSyntax/) (EDT), created at the University of Tartu. The treebank consists of ca 430 000 tokens (punctuation included) in ca 30 000 sentences and covers 3 different genres, namely newspaper texts, fiction and scientific texts.

The current version, Estonian UD v 2.1 has been created by semi-automatic conversion of v 1.3 annotations; some constructions were also re-annotated manually. Among the most frequent of those needing manual effort one can name determing the heads of copular constructions.

# Acknowledgments

We wish to thank all of the contributors to the original EDT annotation effort, especially Eleri Aedmaa, Riin Kirt and Dage Särg. Also, we wish to thank Andriela Rääbis for her great job with v 2.1 annotations.

This work was financed by the National Programme for Estonian Language Technology (https://www.keeletehnoloogia.ee/en?set_language=en) and Estonian Ministery of Education and Research (grant 20-56 IUT20-56 "Computational models for Estonian").

# References

* Kadri Muischnek, Kaili Müürisep, Tiina Puolakainen, Eleri Aedmaa, Riin Kirt, Dage Särg.  2014.
  [Estonian Dependency Treebank and its annotation scheme](http://tlt13.sfs.uni-tuebingen.de/tlt13-proceedings.pdf).
  In: *Proceedings of the 13th Workshop on Treebanks and Linguistic Theories (TLT13),*
  pp. 285–291, ISBN 978-3-9809183-9-8, Tübingen, Germany.

* Kadri Muischnek, Kaili Müürisep and Tiina Puolakainen 2016. Estonian Dependency Treebank: from Constraint Grammar tagset to Universal Dependencies. - Proceedings of LREC 2016.

# Changelog

* UD v2.1: manual reannotation of copula sentences, names and appositions; semiautomatic reannotation of pronouns and determiners and coordinated structures; automatic reannotation of nmod and obl functions.

* UD v2.0: manual reannotation of copula sentences, names and appositions; semiautomatic reannotation of pronouns and determiners and coordinated structures; automatic reannotation of nmod and obl functions.

* UD v1.2 contained Arborest, a much smaller and older VISL-style treebank. It has been re-annotated and added to EDT for UD v1.3.

=== Machine-readable metadata =================================================
Documentation status: stub
Data source: semi-automatic
Data available since: UD v1.2
License: CC BY-NC-SA 4.0
Includes text: yes
Genre: fiction news nonfiction
Lemmas: converted from manual
UPOS: converted from manual
XPOS: converted from manual
Features: converted from manual
Relations: converted from manual
Contributing: here
Contributors: Muischnek, Kadri; Müürisep, Kaili; Puolakainen, Tiina
Contact: kadri.muischnek@ut.ee, kaili.muurisep@ut.ee
===============================================================================
