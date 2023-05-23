# python-RSC-1985-c-C-46
Expert system for the Criminal Code of Canada in Python

I'm designing a program to interpret the Criminal Code of Canada. The program will translate statutes into Python functions that return true/false results when objects representing events are passed to them. The objects may be created manually or through an expert-system-style questionairre.

> Any legal decision has a factual and normative component.
> Jon Bing, _Computerized Legal Information Services: An Introduction_

Operating on this hypothesis, this project proposes to implement an expert legal system using predefined legislative and jurisprudential rules that interact with factual objects.

## Facts
At their base, criminal offences are premised in a factual matrix that the state alleges took place. 

1. **Universal elements.** Date/jurisdiction/ID, and other universal elements will need to be accounted for in a distinct function.
2. **Offence types.** To be able to create a factual matrix that can then be translated into a criminal offence, it will be necessary to identify many different components. Every offence has elements, and (almost) all distinct criminal offence have distinct elements. Many will share elements in common.
3. **Direction.** Rules should be adaptable to both deductive and inductive approaches.

## Rules

1. **Offence elements.** The most basic functionality will need rules to account for an offence's stated elements. Some offences will require digging into case law to highlight interpretive inconsistencies or additional legal tests used to establish whether a statutory condition has been met.
2. **Definitions.** Some words and phrases have set meanings, either through statutory definitions or through common-law interpretation. The program will need to rely on various dictionaries to properly account for these definitions.
3. **Procedural functions.** Some offences cannot be made out when there have been procedural deficiencies. The program should eventually flag procedurally unviable offences and identify the reason for the deficiency.
4. **Evidence.** Much like procedural functions, some offences cannot be made out due to evidentiary issues. The program should also eventually flag these issues and identify them as the reason for the deficient prosecution.
5. **Direction.** Rules should be adaptable to both deductive and inductive approaches.

## TODO

### Ongoing considerations

* Probability: can the expert system account for different probabilities and evaluate offences on that basis?
* Utility: what good will an expert system like this be able to do?
  * Trace statutory incompatibilities
  * Assess charge resolution alternatives (lesser included offences)
  * Identify case strengths and weaknesses
  * Automate minimum/maximum sentencing ranges and available non-custodial sanctions
