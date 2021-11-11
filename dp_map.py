
class DpMap:
    def __init__(self, function: Callable[[Any], Any]) -> None:
        self.function = function
        self.memo_map: dict[Any, Any] = {}


    def __call__(self, *args: tuple[Any, ...]) -> Any:
        if args not in self.memo_map:
            self.memo_map[args] = self.function(*args)        
        return self.memo_map[args]



    def __repr__(self) -> str(dict[str, str]):
        return str({
            x: y for x, y in zip(['Module', 'Name', 'ObjectID'], [self.__module__, type(self).__name__, hex(id(self))])
        })



    def __str__(self) -> str(dict[str, Union[Callable[[Any], Any], dict[Any, Any]]]):
        return str({
            x: y for x, y in zip(['Function', 'Memo_Map'], [self.function, self.memo_map])    
        })

    
    

@DpMap
def lcs(x: str, y: str, m: int, n: int) -> int:
    if m == 0 or n == 0:
        return 0
    
    elif x[m - 1] == y[n - 1]:
        return 1 + lcs(x, y, m - 1, n - 1)
    
    return max(lcs(x, y, m, n - 1), lcs(x, y, m - 1, n))



#@: convert any recursive function and cache the value 
#...




if __name__.__contains__('__main__'):
    X: str = "AGGTAB"
    Y: str = "GXTXAYB"
    print(lcs(X, Y, len(X), len(Y)))
