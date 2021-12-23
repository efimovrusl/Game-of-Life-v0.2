class LCG:

    def __init__(self, 
    seed: int=0, 
    min: int=0, max: int=2147483647,
    a: int=1103515245, c: int=12345, m: int=2**31):
        self.seed = seed
        self.min, self.max = min, max
        self.a, self.c, self.m = a, c, m

    def set_seed(self, seed : int) -> None:
        self.seed = seed

    def next(self) -> int:
        self.seed = self.lcg(self.seed, self.a, self.c, self.m)
        return self.seed % (self.max - self.min) + self.min
    
    def lcg(seed, a, c, m):
        return (a * seed + c) % m
            


# test #
if __name__ == '__main__':
    seed = 0
    count = 16
    min, max = 0, 9
    amount = 10_000
    rand = LCG(seed, min, max)

    print(f"seed: {seed}\tinterval: [{min}, {max}]")
    
    list = []

    [list.append(rand.next()) for _ in range(amount)]
    for i in set(list):
        print(f"{i}: {list.count(i) / amount}")
