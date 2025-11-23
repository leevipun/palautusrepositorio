class QueryBuilder:
    def __init__(self, stack=None):
        self._stack = stack or []

    def _with(self, matcher):
        # Luo uusi QueryBuilder kopioidulla stackilla
        return QueryBuilder(self._stack + [matcher])

    def build(self):
        if len(self._stack) == 0:
            return All()
        if len(self._stack) == 1:
            return self._stack[0]
        return And(*self._stack)
    
    def plays_in(self, team):
        return self._with(PlaysIn(team))
    
    def has_at_least(self, value, attr):
        return self._with(HasAtLeast(value, attr))
    
    def has_fewer_than(self, value, attr):
        return self._with(HasFewerThan(value, attr))
    
    def one_of(self, *queries):
        matchers = []
        for query in queries:
            if isinstance(query, QueryBuilder):
                matchers.append(query.build())
            else:
                matchers.append(query)
        return self._with(Or(*matchers))

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def test(self, player):
        status = False
        for matcher in self._matchers:
            if matcher.test(player):
                status = True     

        return status
            

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class All:
    def test(self):
        return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def test(self, player):
        return not self._matcher.test(player)


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

