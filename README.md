Publications
============

This is a public repository for the shared development of
publications.  

How To
-------

To create a branch to hold a new publication you would like to start working 
on:

- have a GitHub account 
- be part of the ARFC GitHub group
- fork this repository
- clone your fork locally
- add this arfc fork as a remote
- create a new orphan branch (git checkout --orphan <branchname>)
- clear the working directory (git rm --cached -r .)
- create a readme.md file with a description of the publication you'll work on
- add and commit that readme.md file
- push or pull request this to your local fork and this arfc fork

When you create your branch, please note the naming convention below. As you 
start to write, note the available templates here and elsewhere for LaTeX 
documents.

Branches
--------

Each distinct publication will be generated in a separate bare branch. The 
naming convention for branches should be **YYYY-author-keyword-venue** where:

YYYY = the year of submission. 
author = the last name of the first author, lower case
keyword = the first word of the title or a distinguishing keyword, lower case
venue = (optional) an identifier for the publication venue, lower case


For example, let's consider the famous publication by Lise Meitner and Otto Frisch describing the theory of nuclear fission for the first time (neither scientist would receive the Nobel Prize for this work - their collaborator Otto Hahn was the sole recipient.)  

Meitner, L.; Frisch, O. R. (1939). "Disintegration of Uranium by Neutrons: A New Type of Nuclear Reaction". Nature. 143 (3615): 2. doi:10.1038/143239a0.

Work on this publication would have been in a branch called : **1939-meitner-disintegration-nature** .


Format Templates
----------------
Some of these branches will hold templates for certain common formats. These 
branches will be called 'template-name' such as 'template-ieee' or similar. 
Please add templates as you discover them.

Rather than duplicate them here, some other formats are found in their
own repo:

* [ANS Transactions](https://github.com/sethrj/anstrans) by Seth Johnson (@sethrj)
