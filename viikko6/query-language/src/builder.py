from matchers import * # Voidaan pitää huonona tyylinä Pythonissa, mutta tässä pitäisi olla ok
from enum import Enum
from collections import namedtuple

class QueryType(Enum):
    PlaysIn = 1
    HasAtLeast = 2
    HasFewerThan = 3

Query = namedtuple("Query", ["type", "args"])

class QueryBuilder:
    def __init__(self, pino = []):
        self.pino = pino

    def playsIn(self, team):
        # Tämä toteutus ei noudata immutabilityä eli muokaamattomuutta, mutta
        # tämä on niin yksinkertainen että sille ei ole tarvetta. Olisin käyttänyt
        # jonkinlaista value tyyppinä toimivaa luokkaa/structia, jos Python tarjoaisi sellaisia.
        self.pino.append(Query(QueryType.PlaysIn, (team,)))
        return self

    def hasAtLeast(self, value, attr):
        self.pino.append(Query(QueryType.HasAtLeast, (value, attr)))
        return self

    def hasFewerThan(self, value, attr):
        self.pino.append(Query(QueryType.HasFewerThan, (value, attr)))
        return self

    def _querytuple_to_query(self, qt):
        args = qt.args
        if qt.type == QueryType.PlaysIn: # Enumin voisi jopa korvata suoraan luokalla
            # Argumenttien purkaminen näin on ehkä vähän kyseenalaista
            return PlaysIn(*args) 
        elif qt.type == QueryType.HasAtLeast:
            return HasAtLeast(*args)
        elif qt.type == QueryType.HasFewerThan:
            return HasFewerThan(*args)

    def build(self):
        queries = map(self._querytuple_to_query, self.pino)
        return And(*queries)
