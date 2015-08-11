""" Data/Tuple.py - functional programming functions for tuples
"""

# fst :: (a,b) -> a
fst = lambda x: x[0]

# snd :: (a,b) -> b
snd = lambda x: x[1]

# curry :: ((a,b) -> c) -> a -> b -> c
curry = lambda f,x,y: f(x,y)

# uncurry :: (a -> b -> c) -> ((a, b) -> c)
uncurry = lambda f: lambda (a,b): f(a,b)

# swap :: (a,b) -> (b,a)
swap = lambda (a,b): (b,a)

