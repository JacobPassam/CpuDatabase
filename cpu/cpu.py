class Cpu:

    def __init__(self, name: str, clock_speed: float, cores: int, cache_size: int, price: float, cpu_id: int = None):
        self.name = name
        self.clock_speed = clock_speed
        self.cores = cores
        self.cache_size = cache_size
        self.price = price
        self.cpu_id = cpu_id

    def get_as_string(self):
        if self.cpu_id is None:
            return f"Name: {self.name}, ClockSpeed: {self.clock_speed}, Cores: {self.cores}, CacheSize: {self.cache_size}, Price: {self.price} "
        else:
            return f"ID: {self.cpu_id}, Name: {self.name}, ClockSpeed: {self.clock_speed}, Cores: {self.cores}, CacheSize: {self.cache_size}, Price: {self.price}"
