from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = dict()

    def fibonacci(num: int) -> int:
        if num <= 0:
            return 0
        
        if num == 1:
            return 1

        if num in cache:
            return cache[num]
        
        #caching
        cache[num] = fibonacci(num-1) + fibonacci(num-2)

        return cache[num]
    
    return fibonacci


f = caching_fibonacci()
print(f(15))