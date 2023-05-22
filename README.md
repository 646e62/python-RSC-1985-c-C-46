# python-RSC-1985-c-C-46
Expert system for the Criminal Code of Canada in Python

I'm designing a program to interpret the Criminal Code of Canada. The program will translate statutes into Python functions that return true/false results when objects representing events are passed to them. The objects may be created manually or through an expert-system-style questionairre.

<<<<<<< HEAD
> Any legal decision has a factual and normative component.
> Jon Bing, _Computerized Legal Information Services: An Introduction_

Operating on this hypothesis, this project proposes to implement an expert legal system using predefined legislative and jurisprudential rules that interact with factual objects.

## Facts object
At their base, criminal offences are premised in a factual matrix that the state alleges took place. 

### Offence types

The [Criminal Code's offence categorization](https://laws-lois.justice.gc.ca/eng/acts/C-46/) may not prove to be the best, but it serves as a starting point. 

## Expert systems

### Definitions

### Procedural functions

### Evidence

## Things to continue to look into

* Probability: can the expert system account for different probabilities and evaluate offences on that basis?
* Utility: what good will an expert system like this be able to do?
=======
## What could a program like this do?

* Trace statutory incompatibilities
* Assess charge resolution alternatives (lesser included offences)
* Identify case strengths and weaknesses
* Automate minimum/maximum sentencing ranges and available non-custodial sanctions

## Factual object

At their base, criminal offences are established from a factual matrix that's alleged to have occurred. Creating an object ... 

The [Criminal Code's offence categorization](https://laws-lois.justice.gc.ca/eng/acts/C-46/) may not prove to be the best, but it serves as a starting point.

To be able to create a factual matrix that can then be translated into a criminal offence, it will be necessary to identify many different components. Every offence has elements, and (almost) all distinct criminal offence have distinct elements. Many will share elements in common.

## TODO
* GPT integration: train GPT (or similar) to categorize text into categories that can then be fed into the data object
>>>>>>> 779d968 (0.0.1 prep)
