'''
This file contains key-value pairs for the general definition section in the Criminal Code.

Values are designed to hold the following information:

* Definition list
  * [-1] — operator (if applicable)
  * [:-1] — definition
* French key equivalent

This structure isn't as important here as it will be in other sections. With definitions, there usually isn't a big difference between different definitions linked conjuctively or disjunctively. But with legal tests, that difference is critical. Adopting the structure here will allow me to use the same code for both definitions and legal tests, and to test whether this structure is actually useful.
'''

general_definitions = {
    "Act": [["An Act of Parliament", "An Act of the legislature of the former Province of Canada", "An Act of the legislature of a province", "An Act or ordinance of the legislature of a province, territory or place in force at the time that province, territory or place became a province of Canada.", "and"], "Loi"],
    "appearance notice": [["A notice in Form 9 issued by a peace officer", "N/A"], "citation à comparaître"],
    "associated personell": [["Persons who are assigned by a government or an intergovernmental organization with the agreement of the competent organ of the United Nations to carry out activities in support of the fulfilment of the mandate of a United Nations operation", "Persons who are engaged by the Secretary-General of the United Nations, by a specialized agency of the United Nations or by the International Atomic Energy Agency to carry out activities in support of the fulfilment of the mandate of a United Nations operation", "Persons who are deployed by a humanitarian non-governmental organization or agency under an agreement with the Secretary-General of the United Nations, by a specialized agency of the United Nations or by the International Atomic Energy Agency to carry out activities in support of the fulfilment of the mandate of a United Nations operation", "or"], "personnel associé"],
    "attorney general": [[], "procureur général"],
    "audioconference": [["Any means of telecommunication that allows the judge or justice and any individual to communicate orally in a proceeding"], "audioconférence"],
    
}