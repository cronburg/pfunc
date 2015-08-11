""" Data/Either.py - functional programming library for the Either monad
"""
import pfunc.Prelude

class Either(object):
  def __init__(self, typ, val):
    self.typ = typ
    self.val = val

def Left(val):  return Either(Left, val)
def Right(val): return Either(Right, val)

# either :: (a -> c) -> (b -> c) -> Either a b -> c
def either(f, g, e):
  if isinstance(e, Left): f(e.val)
  if isinstance(e, Right): g(e.val)
  raise Exception("Prelude.either: " + str(type(e)) + \
                  " is not either Left or Right")

isLeft  = lambda x: x.typ == Left
isRight = lambda x: x.typ == Right

# lefts :: [Either a b] -> [a]
lefts = lambda xs: [x.val for x in xs if isLeft(x)]

# rights :: [Either a b] -> [b]
rights = lambda xs: [x.val for x in xs if isRight(x)]

# partitionEithers :: [Either a b] -> ([a],[b])
def partitionEithers(xs):
  left  = lambda a,(l,r): (cons(a,l), r)
  right = lambda a,(l,r): (l, cons(a,r))
  return foldr(either(left,right), ([],[]))

