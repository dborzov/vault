from itertools import chain, product
from re import match, findall

GRAMMAR = '''                                                                                                                                                                         
<sentence> ::= <noun phrase=""> <verb phrase="">                                                                                                                                            
<noun> ::= "boy " | "troll " | "moon " | "telescope "                                                                                                                                 
<transitive verb=""> ::= "hits " | "sees "                                                                                                                                               
<intransitive verb=""> ::= "runs " | "sleeps "                                                                                                                                           
<adjective> ::= "big " | "red "                                                                                                                                                       
<adverb> ::= "quickly " | "quietly "                                                                                                                                                  
<determiner> ::= "a " | "that " | "each " | "every "                                                                                                                                  
<pronoun> ::= "he " | "she " | "it "                                                                                                                                                  
<noun phrase=""> ::= <determiner> <noun> | <determiner> <adjective> <noun>                                                                                                               
<verb phrase=""> ::= <intransitive verb=""> | <transitive verb=""> <noun phrase="">                                                                                                               
'''

def parse(g):
    return dict([(w.strip(), [findall(r'(<.+?>|".+?")', s) for s in m.split('|')]) for w, m in [d.split('::=') for d in g.strip().splitlines()]])

def generate(term):
    return findall(r'"(.*?)"', term) if match('".*', term) else chain(*[map(''.join, product(*map(generate, p))) for p in syntax[term]])

syntax = parse(GRAMMAR)
print list(generate('<sentence>'))