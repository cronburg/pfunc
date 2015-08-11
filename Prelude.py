""" Prelude.py - a functional programming library for python
"""

##############################################################################
# Maybe:
class Maybe(object):
  def __init__(self, typ, val=None):
    self.typ = typ
    self.val = val

def Nothing(): return Maybe(Nothing)
def Just(a):   return Maybe(Just, a)

##############################################################################
# Ordering:
class Ordering(object):
  def __init__(self, order):
    self.order = order

def LT(): return Ordering(LT)
def EQ(): return Ordering(EQ)
def GT(): return Ordering(GT)

##############################################################################
# cons :: a -> [a] -> [a]
def cons(b,bs): return [b] + bs

# head :: [a] -> a
def head(lst):
  try: return lst[0]
  except IndexError as e: raise Exception("Prelude.head: empty list")

# tail :: [a] -> [a]
def tail(lst):
  try: return lst[1:]
  except IndexError as e: raise Exception("Prelude.tail: empty list")

# map :: (a -> b) -> [a] -> [b]
def map(fncn, lst):
  if len(lst) == 0: return lst
  return cons( fncn( head( lst ) ), map(fncn, tail( lst ) ) ) 

