import re
import json


def valid_email(mail):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", mail) != None:
            return True
    return False


class Panda:

    def __init__(self, name, email, gender):
        self.name = name
        self.gender = gender
        is_valid = valid_email(email)
        if is_valid:
            self.email = email

    def isMale(self):
        if self.gender == 'male':
            return True
        return False

    def isFemale(self):
        if self.gender == 'female':
            return True
        return False

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        names = self.name == other.name
        emails = self.email == other.email
        genders = self.gender == other.gender
        if names and emails and genders:
            return True
        else:
            return False

    def __repr__(self):
        return "Panda('{}', '{}', '{}')".format(
            self.name, self.email, self.gender)

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender


class PandaSocialNetwork:

    def __init__(self):
        self.net = {}

    def add_panda(self, new):
        if new in self.net:
            raise PandaAlreadyThere
        else:
            self.net[new] = []

    def has_panda(self, panda):
        if panda in self.net:
            return True
        return False

    def make_friends(self, panda1, panda2):
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        if self.are_friends(panda1, panda2):
            raise AlreadyFriends
        else:
            self.net[panda1].append(panda2)
            self.net[panda2].append(panda1)

    def are_friends(self, panda1, panda2):
        return panda1 in self.net[panda2] and panda2 in self.net[panda1]

    def friends_of(self, friend):
        if not self.has_panda(friend):
            return False
        else:
            return self.net[friend]

    def connection_level(self, panda1, panda2):
        net = self.net
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False

        if self.are_friends(panda1, panda2):
            return 1

        visited = set()
        queue = []
        path_to = {}
        path_lenght = 0
        found = False
        queue.append(panda1)
        visited.add(panda1)
        path_to[panda1] = None
        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == panda2:
                found = True
                break
            for friend in net[current_node]:
                if friend not in visited:
                    path_to[friend] = current_node
                    visited.add(friend)
                    queue.append(friend)

        if found:
            while path_to[panda2] is not None:
                path_lenght += 1
                panda2 = path_to[panda2]
        return path_lenght

    def are_connected(self, panda1, panda2):
        if self.connection_level(panda1, panda2) != 0:
            return True
        return False

    def how_many_gender_in_network(self, level, panda, gender):
        count = 0
        friends = []
        while level > 0:
            for pand in self.net[panda]:
                if pand.gender == gender and pand not in friends:
                    count += 1
                    friends.append(pand)
            level -= 1

        return count

    def save(self, path):
        self.save = {}
        for pandas in self.net:
            if repr(pandas) not in self.save:
                self.save[repr(pandas)] = []
            for friends in self.net[pandas]:
                self.save[repr(pandas)].append(repr(friends))
        json_str = json.dumps(self.save, indent=4)

        with open(path, "w") as f:
            f.write(json_str)

    def load(self, path):
        self.data = {}
        with open(path, 'r') as f1:
            self.data = json.load(f1)
        for pandas in self.data:
            self.add_panda(eval(pandas))
            for friends in self.data[pandas]:
                self.net[eval(pandas)].append(eval(friends))


class PandaAlreadyThere(Exception):
    pass


class AlreadyFriends(Exception):
    pass

if __name__ == '__main__':
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    print(ivo.get_name() == "Ivo")
    print(ivo.get_email() == "ivo@pandamail.com")  # True
    print(ivo.get_gender() == "male")
    print(ivo.isMale() == True)
    print(ivo.isFemale() == False)
    network = PandaSocialNetwork()
    ivo = Panda("Ivo", "ivo@pandamail.com", "male")
    rado = Panda("Rado", "rado@pandamail.com", "male")
    tony = Panda("Tony", "tony@pandamail.com", "female")
    for panda in [ivo, rado, tony]:
        network.add_panda(panda)
    network.make_friends(ivo, rado)
    network.make_friends(rado, tony)
    print(network.connection_level(ivo, rado) == 1)
    print(network.connection_level(ivo, tony) == 2)
    print(network.how_many_gender_in_network(1, rado, "female") == 1)
    network.save("panda.json")
    print(network.load("panda.json"))
