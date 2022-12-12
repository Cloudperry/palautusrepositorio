from matchers import * # Voidaan pitää huonona tyylinä Pythonissa, mutta tässä pitäisi olla ok
from enum import Enum
from collections import namedtuple

class QueryType(Enum):
    PlaysIn = 1
    HasAtLeast = 2
    HasFewerThan = 3
    Or = 4

Query = namedtuple("Query", ["type", "args"])

class QueryBuilder:
    def __init__(self, pino = []):
        self.pino = pino

    def playsIn(self, team):
        uusi_pino = self.pino + [Query(QueryType.PlaysIn, (team,))]
        return QueryBuilder(uusi_pino)

    def hasAtLeast(self, value, attr):
        uusi_pino = self.pino + [Query(QueryType.HasAtLeast, (value, attr))]
        return QueryBuilder(uusi_pino)

    def hasFewerThan(self, value, attr):
        uusi_pino = self.pino + [Query(QueryType.HasFewerThan, (value, attr))]
        return QueryBuilder(uusi_pino)

    def oneOf(self, *queries):
        uusi_pino = [Query(QueryType.Or, queries)]
        return QueryBuilder(uusi_pino)

    def _query_to_queryobj(self, query):
        args = query.args
        if query.type == QueryType.PlaysIn: # Enumin voisi jopa korvata suoraan luokalla
            # Argumenttien purkaminen näin on ehkä vähän kyseenalaista
            return PlaysIn(*args) 
        elif query.type == QueryType.HasAtLeast:
            return HasAtLeast(*args)
        elif query.type == QueryType.HasFewerThan:
            return HasFewerThan(*args)
        elif query.type == QueryType.Or:
            return Or(*args)

    def build(self):
        queries = map(self._query_to_queryobj, self.pino)
        return And(*queries)
