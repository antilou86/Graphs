import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        while self.last_id <= num_users:
        # Add users, user name will essentially be the user_id
            self.add_user(self.last_id)
        # Create friendships
        #for each user
        for user in self.users:
            #empty list to track potential friends
            possible_friends = []
            
            #loop through all users
            for person in self.users:
                #if its a duplicate, or the user we're evaluating, skip
                if person is not user:
                    if person not in possible_friends: 
                        possible_friends.append(person)
            #fisher-yates shuffle - to randomize the list
            for i in range(len(possible_friends)):
                random_index = random.randint(i, len(possible_friends) - 1)
                possible_friends[random_index], possible_friends[i] = possible_friends[i], possible_friends[random_index]

            #slice the first N (or "avg_friendships") bits off the list
            friends_to_add = possible_friends[:avg_friendships]
            #add random number of friends from the resulting array.
            for item in friends_to_add:
                #avoids double adding, since it is a bi-directional relationship.
                if user < item:
                    self.add_friendship(user, item)
                
    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        qu = Queue()
        qu.enqueue(user_id)
        visited[user_id] = set([user_id])

        while qu.size() > 0:
            current_user = qu.dequeue()
            visited[current_user].add(current_user)

            for i in self.friendships[current_user]:
                if not i in visited:
                    if i is not None:
                        visited[i]=visited.get(current_user).copy()#copy of the current_user array
                        visited[i].add(current_user)
                        visited[i].add(i)
                        qu.enqueue(i)
                        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
