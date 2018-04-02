# Summary

The Arabic UD treebank is based on the
[Prague Arabic Dependency Treebank](http://ufal.mff.cuni.cz/padt/) (PADT),
created at the Charles University in Prague.


# Introduction

http://universaldependencies.github.io/docs/ar/overview/introduction.html

The treebank consists of 7,664 sentences (282,384 tokens) and its domain is mainly newswire.
The annotation is licensed under the terms of
[CC BY-NC-SA 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/)
and its original (non-UD) version can be downloaded from
[http://hdl.handle.net/11858/00-097C-0000-0001-4872-3](http://hdl.handle.net/11858/00-097C-0000-0001-4872-3).

The morphological and syntactic annotation of the Arabic UD treebank is created through
conversion of PADT data. The conversion procedure has been designed by Dan Zeman.
The main coordinator of the original PADT project was Otakar Smrž.


# Acknowledgments

We wish to thank all of the contributors to the original PADT annotation effort, including
Otakar Smrž, Jan Hajič, Petr Zemánek, Petr Pajas, Jan Šnaidauf, Emanuel Beška, Jakub Kráčmar,
and Kamila Hassanová.

Further corrections of additional data (not part of PADT release 1.0) were done by
Shadi Saleh and Zdeněk Žabokrtský.


## References

* Jan Hajič, Otakar Smrž, Petr Zemánek, Petr Pajas, Jan Šnaidauf, Emanuel Beška, Jakub Kráčmar,
  Kamila Hassanová. 2009.
  Prague Arabic Dependency Treebank 1.0, LINDAT/CLARIN digital library at
  Institute of Formal and Applied Linguistics, Charles University in Prague,
  [http://hdl.handle.net/11858/00-097C-0000-0001-4872-3](http://hdl.handle.net/11858/00-097C-0000-0001-4872-3).
* Otakar Smrž, Viktor Bielický, Iveta Kouřilová, Jakub Kráčmar, Jan Hajič, Petr Zemánek. 2008.
  Prague Arabic Dependency Treebank: A Word on the Million Words.
  In: Proceedings of the Workshop on Arabic and Local Languages (LREC 2008), pp. 16–23.
  Marrakech, Morocco.


# Changelog

* 2017-03-01 v2.0
  * Converted to UD v2 guidelines.
  * Reconsidered PRON vs. DET.
  * Improved advmod vs. obl distinction.
  * Changed train-dev-test split to be compatible with UD_Arabic-NYUAD, which in turn follows Diab et al.
    (Mona Diab, Nizar Habash, Owen Rambow, Ryan Roth. 2013. LDC Arabic treebanks and associated corpora:
    Data divisions manual. arXiv preprint arXiv:1309.5652.)
    Some documents appear both in UD_Arabic and in UD_Arabic-NYUAD, and we want these to end up in the same section in both treebanks.

* 2016-05-15 v1.3
  * Unvocalized surface forms are now the main word forms in the FORM column. Fused tokens are shown. Vocalized forms available as MISC attributes.
  * Added lemmas, roots, transliteration and English glosses.
  * The _%_ symbols are now attached as `nmod` instead of `cc`.
  * Chains of auxiliaries have been removed as the negative copula لَيسَ / _laysa_ is now treated as copula and not as auxiliary verb.
  * Fixed adverbs that were attached as nmod; correct: advmod.
  * Fixed sentence ids.
  * Added the MISC attribute SpaceAfter=No.
  * Improved conversion of AuxY.

* 2015-11-15 v1.2
  * Modified version from HamleDT 3.0


=== Machine-readable metadata (DO NOT REMOVE!) ================================
Data available since: UD v1.2
License: CC BY-NC-SA 3.0
Includes text: yes
Genre: news
Lemmas: converted from manual
UPOS: converted from manual
XPOS: manual native
Features: converted from manual
Relations: converted from manual
Contributors: Zeman, Daniel; Žabokrtský, Zdeněk; Saleh, Shadi
Contributing: elsewhere
Contact: zeman@ufal.mff.cuni.cz
===============================================================================
