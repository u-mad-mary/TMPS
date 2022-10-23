# The Object Pool design pattern uses a pool of initialized objects that are ready to be used rather than creating a new object all the time. 
# The main idea of an Object Pool is that instead of creating instances of the class you can reuse them by getting them from the pool.
# It manages a fixed number of instances.


class Tool:
            
    def tool(self, nr):
        return nr
        
class PoolManager: #automaticlly acquires and releases objects
    
    def __init__(self, pool):
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
        
        t = self.free[0]
        self.free.remove(t)
        self.in_use.append(t)
        return t
    
    def release(self, t: Tool):
        self.in_use.remove(t)
        self.free.append(t)
        return t
        
