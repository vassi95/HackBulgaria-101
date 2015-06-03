class DirectedGraph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node_a, node_b):
        self.node_a = node_a
        self.node_b = node_b
        if node_a in self.nodes.keys():
            self.nodes[node_a].append(node_b)
            self.nodes[node_b] = []
        else:
            self.nodes[node_a] = [node_b]
            self.nodes[node_b] = []

    def get_neighbors_for(self, node):
        if node in self.nodes:
            return self.nodes[node]

    def path_between(self, node_a, node_b):
        visited_nodes = set()
        queue = []
        queue.append(node_a)
        visited_nodes.add(node_a)
        while len(queue) != 0:
            node = queue.pop(0)
            if node == node_b:
                return True
            for neighbour in self.nodes[node]:
                if neighbour not in visited_nodes:
                    visited_nodes.add(neighbour)
                    queue.append(neighbour)
        return False


class Who_follows_you:
    def __init__(self):
        self.graph = DirectedGraph()
        self.name = name

    def do_you_follow(self, user):
        return self.graph.edge_between(self.user, user)

    def do_you_follow_indirectly(self, user):
        return self.graph.path_between(self.user, user)

    def does_he_she_follows(self, user):
        return self.graph.edge_between(user, self.user)

    def does_he_she_follows_indirectly(self, user):
        return self.graph.path_between(user, self.user)

    def build_network(self, name, level):
        if level < 4:
            self.name = name
            self.followers_network(name, level)
            self.following_network(name, level)

    def followers_network(self, name, level):
        level = 0
        visited = set()
        queue = []
        visited.add(name)
        queue.append((level, name))
        while len(queue) != 0:
            level, user = queue.pop(0)
            if level == level:
                break
            if len(user.get_followers()) == 0:
                user.followers()
            followers = user.get_followers()
            for f in followers:
                if f not in visited:
                    visited.add(follower)
                    queue.append((level + 1, f))
                    self.graph.add_edge(f, user)

    def following_network(self, name, level):
        level = 0
        visited = set()
        queue = []
        queue.append((level, name))
        visited.add(name)
        while len(queue) != 0:
            level, user = queue.pop(0)
            if level == level:
                break
            if len(user.get_following()) == 0:
                user.following()
            followings = user.get_following()
            for following in followings:
                if following not in visited:
                    queue.append((level + 1, following))
                    visited.add(following)
                    self.graph.add_edge(user, following)

    def who_follows_you_back(self):
        followers = self.name.get_followers()
        following = self.name.get_following()
        qho_follows_you_back = []
        for f in followers:
            if f in following:
                who_follows_you_back.append(f)
        return who_follows_you_back

