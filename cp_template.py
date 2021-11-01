from __future__ import annotations
import os, sys
from io import BytesIO, IOBase


class FastIO(IOBase):
    newlines: ClassVar[int] = 0

    def __init__(self, file: File) -> None:
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = 'x' in file.mode or 'r' not in file.mode
        self.write = self.buffer.write if self.writable else None



    def read(self) -> Any:
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        
        self.newlines = 0
        return self.buffer.read()



    def readline(self) -> Any:
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        
        self.newlines -= 1
        return self.buffer.readline()



    def flush(self) -> Any:
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)



class IOWrapper(IOBase):
    def __init__(self, file: _file) -> None:
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")




def print(*args: tuple[Any, ...|Any], **kwargs: dict[Any, Any]) -> Any:
    sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
    at_start: bool = True
    
    for x in args:
        if not at_start:
            file.write(sep)
        file.write(str(x))
        at_start = False
    
    file.write(kwargs.pop("end", "\n"))
    if kwargs.pop("flush", False):
        file.flush()



#@: --- Globals ---
BUFSIZE: int = 8192
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout) 



def solve(*args: tuple[Any, ...|Any], **kwargs: dict[Any, Any]) -> Any:
    ...
    






#@: Driver code
if __name__.__contains__('__main__'):
    sys.stdin = open('C:\\Users\\RAHUL\\OneDrive\\Desktop\\Python_CP\\input.txt', 'r')
    sys.stdout = open('C:\\Users\\RAHUL\\OneDrive\\Desktop\\Python_CP\\output.txt', 'w')       

    test_cases: int = int(input())
    for _ in range(test_cases):
        # args: list[int] <- take inputs
        # print(args)
        ...

    