# Pseudoword generation

1. First idea: generate random strings of letter.


2. How to improve pseudwords generation?

    - respect  orthographic / morphological rules
    - respect  statistics of letter sequences 
    - both

---

# Lexical Frequency Distributions


* Download the text files from the `plain1` folder of <https://github.com/COST-ELTeC/ELTeC-fra>
* Write a python script that count the number of occurences of  letter string spearated by spaces, and plot the distribution.
* install the `wordfreq` python library; use to list the 100 most frequent french words
* Write a script that computes the frequencies of letters 
* Generate pseudowords that respect the frequecy of letters
* (skip it) Compute the frequency of bigrams (pair of letters), and generate words that respect the frquency of bigrams. 

Check the Unipseudo app from http://openlexicon.fr

---

# The Lexique database

The _Lexique database_ provides detailed inofmration for a 140k French words. 

To view it and query it interactively, use the _OpenlexiconApp_ from https://openlexicon.fr (To learn about **Regular Expressions**, see <https://pcbs.readthedocs.io/en/latest/regular_expressions.html>)

To query it from R, see <https://github.com/chrplr/openlexicon/blob/master/documents/Interroger-Lexique-avec-R/interroger-lexique-avec-R.pdf>

To query it from Python, check  <http://www.lexique.org/?page_id=76>


