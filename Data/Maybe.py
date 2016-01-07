""" Data/Maybe.py - functional programming library for the Maybe monad
"""
import pfunc.Prelude
from pfunc.Prelude import *

# maybe :: b -> (a -> b) -> Maybe a -> b
def maybe(n, f, m):
  if m is None: return n
  return f(m.val)

# isJust :: Maybe a -> Bool
isJust = lambda x: x.typ == Just

# isNothing :: Maybe a -> Bool
isNothing = lambda x: x.typ == Nothing

# fromJust :: Maybe a -> a
def fromJust(m):
  if isNothing(m): raise Exception("Maybe.fromJust: Nothing")
  return m.val

# fromMaybe :: a -> Maybe a -> a
def fromMaybe(d, x):
  if isNothing(x): return d
  return x.val

# maybeToList :: Maybe a -> [a]
def maybeToList(m):
  if isNothing(m): return []
  return [m.val]

# listToMaybe :: [a] -> Maybe a
def listToMaybe(xs):
  if len(xs) == 0: return Nothing()
  return Just(xs[0])

# catMaybes :: [Maybe a] -> [a]
def catMaybes(ms):
  return [m.val for m in ms if isJust(m)]

# mapMaybe :: (a -> Maybe b) -> [a] -> [b]
def mapMaybe(f, xs):
  if len(xs) == 0: return []
  rs = mapMaybe(f, tail(xs))
  v  = f(head(xs))
  if isNothing(v): return rs
  return cons(r, rs)

# mapMaybeFB :: (b -> r -> r) -> (a -> Maybe b) -> a -> r -> r
def mapMaybeFB(cns, f, x, nxt):
  if isNothing(f(x)): return nxt
  return cns(r, nxt)

