

class Histogram():

    def __init__(self):
        self.servers = {}

    def add(self, server, times):
        if server in self.servers:
            self.servers[server] += times
        else:
            self.servers[server] = times

    def count(self, server):
        if server in self.servers:
            return self.servers[server]

    def get_data(self):
        return self.servers

    def get_data_keys(self):
        return self.servers.keys()

    def get_data_values(self):
        return self.servers.values()
