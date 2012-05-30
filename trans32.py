"""
Any *three*-symbol language is isomorphic to a *two*-symbol language trivially obtained 
using binary prefix-codes: denoting the three symbols by x,y,z, obtain a binary language
using the two symbols u,v by the substitutions x -> u, y -> vu, z -> vv.  

Example: 
[Whitespace](http://compsoc.dur.ac.uk/whitespace/) has alphabet S,T,L (Space,Tab,Linefeed).
A Binary Whitespace language with alphabet S,T uses TS instead of T, and TT instead of L; 
e.g., the BWS instruction to push -5 onto the stack is SSTSTSSTSTT instead of SSTTSTL, etc.

Translator (below):
To translate a WS program into a BWS program: bws = translate(wsprog, ' \t\n', ' \t')
To translate a BWS program into a WS program: ws = translate(bwsprog, ' \t', ' \t\n')
"""

def translate(s,a,b):
    #translate program s **from** the a-alphabet language **to** the b-alphabet language;
    #ignores all other characters (treated as comments);
    #one alphabet must have two chars, the other alphabet must have three chars;
    #the 2-char language will be a binary prefix-code version of the 3-char language.
    la = len(a); lb = len(b)
    if min(la,lb)!=2 or max(la,lb)!=3:
        raise Exception("strings a and b must be 2- and 3-letter alphabets")
    out = ''
    if la == 3:     #if a is the 3-char alphabet
        for c in s:
            if c == a[0]: out += b[0]
            elif c == a[1]: out += b[1]+b[0]
            elif c == a[2]: out += b[1]+b[1]
    else:           #else a is the 2-char alphabet
        i = 0
        while i < len(s):
            if s[i] == a[0]: out += b[0]
            elif s[i] == a[1]:
                i += 1
                if i >= len(s): raise Exception("unexpected end of string")
                elif s[i] == a[0]: out += b[1]
                elif s[i] == a[1]: out += b[2]
            i += 1
    return out