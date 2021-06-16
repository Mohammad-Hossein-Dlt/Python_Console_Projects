text = input("Enter Your Text: \n").title()
for i in ['.' , '?' , '/' , '!' , '<' , '>' , ','] : text = text.replace(i," ")
words_list , counter = list(filter(lambda x : x !="", text.split(" ") )) , dict()
for i in set(words_list) : counter[i] = words_list.count(i)
for i in counter : print(f" {i} : {counter[i]} ")
print("\n Most Repeeted Words : ",list(filter(lambda x : max(counter.values()) in x , counter.items())))

# uehfbiwef hello .hello JKHBKU ef.heLLo.by iejfneirfj By woenfwef.hello erfjeb.bY.hello

# Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[31] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a garbage collection system using reference counting and was discontinued with version 2.7.18 in 2020.[32] Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible and much Python 2 code does not run unmodified on Python 3.
