import math

class Enumerator(object):
    
    def __init__(self, total):
        self.total = total

    def combination(self, n, r):
        return int(math.factorial(n) / (math.factorial(r) * (math.factorial(n-r))))

    def enumerate(self, *args):
        heroes_count = len(args)
        if heroes_count < 1 or heroes_count > 5:
            raise Exception("Hero count is invalid ({})".format(heroes_count))

        hero_ids = [0, 0, 0, 0, 0, 0 ]
        hero_minimum_id = [1, 1, 1, 1, 1, 1]
        result = 0

        for i in range(0, heroes_count):
            if not isinstance(args[i], int):
                raise Exception("Hero id is not in integer format ({})".format(args[i]))
            if args[i] < 1 or args[i] > self.total:
                raise Exception("Hero has invalid id ({})".format(args[i]))
            hero_ids[6 - heroes_count + i] = args[i]

        for i in range(1, 5):
            hero_minimum_id[i+1] = hero_ids[i] + 1

        for i in range(1, 5):
            for j in range(1, hero_ids[i] - hero_minimum_id[i] + 1):
                result += self.combination(self.total - j - hero_ids[i-1], 5 - i)
        result += hero_ids[5] - hero_minimum_id[5]

        return result
