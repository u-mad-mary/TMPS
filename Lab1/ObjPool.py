class Tool:
            
    def tool(self, nr):
        return nr
        
class PoolManager:
    def __init__(self,pool):
        self.pool = pool
        
    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj
    
    def __exit__(self, type, value, trace):
        self.pool.release(self.obj)
        
        
class ToolPool:
    
    def __init__(self, number):
        self.number = number
        self.free = []
        self.in_use = []
        
        for _ in range(number):
            self.free.append(Tool())
            
    def acquire(self) -> Tool:
        if len(self.free) <= 0:
            raise Exception("No more available tools.")
        c = self.free[0]
        self.free.remove(c)
        self.in_use.append(c)
        return c
    
    def release(self, c: Tool):
        self.in_use.remove(c)
        self.free.append(c)
        return c
        
