import difflib

a = 'excellent'
b = 'goods'

seq = difflib.SequenceMatcher(None,a,b)
d = seq.ratio()*100
print(d)
