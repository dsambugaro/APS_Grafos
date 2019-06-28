#! /usr/bin/env python3
# coding: utf-8

from os import path
from sys import argv

from GithubApiHandler import UsersHandler


class User():
    def __init__(self, username, name, avatar):
        self.followers = []
        self.following = []
        self.username = username
        self.name = name
        self.avatar = avatar

    def get_username(self):
        return self.username

    def get_name(self):
        return self.name

    def get_avatar(self):
        return self.avatar

    def get_followers(self):
        return self.followers

    def get_following(self):
        return self.following

    def is_follower(self, user):
        for follower in self.followers:
            if isinstance(user, User):
                if follower == user.get_username():
                    return True
            elif follower == user:
                return True
        return False

    def is_being_followed(self, user):
        for user_following in self.following:
            if isinstance(user, User):
                if user_following == user.get_username():
                    return True
            elif user_following == user:
                return True
        return False

    def add_follower(self, user):
        if not self.is_follower(user):
            if isinstance(user, User):
                self.followers.append(user.get_username())
            else:
                self.followers.append(user)

    def start_follow(self, user):
        if not self.is_being_followed(user):
            if isinstance(user, User):
                self.following.append(user.get_username())
            else:
                self.following.append(user)


class GithubUsersList():
    users = []

    def __init__(self, token):
        self.usersAPI = UsersHandler(token)

    def get_users_list(self, fileName):
        users = []
        with open(fileName, 'r') as fp:
            for user in fp:
                users.append(user.replace('\n', ''))
        return users

    def has_user(self, userName):
        for user in self.users:
            if user.get_username() == userName:
                return True
        return False

    def get_user(self, userName):
        for user in self.users:
            if user.get_username() == userName:
                return user
        return None

    def get_users(self):
        return self.users

    def create_users(self, users, relations_depth=0):
        created_users = []
        for user in users:
            if not self.has_user(user):
                print('Creating user {}...'.format(user))
                profile = self.usersAPI.get_user_profile(user)
                new_user = User(profile['login'],
                                profile['name'], profile['avatar_url'])
                self.users.append(new_user)
                created_users.append(new_user)
            else:
                new_user = self.get_user(user)
                if new_user:
                    created_users.append(new_user)
            if relations_depth > 0:
                index = self.users.index(new_user)
                if index >= 0:
                    followers = self.create_users(
                        self.usersAPI.get_user_followers(user), relations_depth-1)
                    following = self.create_users(
                        self.usersAPI.get_user_following(user), relations_depth-1)
                    for user_following in following:
                        print('User {} follows user {}...'.format(
                            user, user_following.get_username()))
                        self.users[index].start_follow(user_following)
                    for follower in followers:
                        print('User {} is followed by user {}...'.format(
                            user, follower.get_username()))
                        self.users[index].add_follower(follower)
        return created_users

    def set_last_relations(self):
        for user in self.users:
            if user.get_followers():
                for follower in user.get_followers():
                    usersList.get_user(follower).start_follow(user)
            if user.get_following():
                for following in user.get_following():
                    usersList.get_user(following).add_follower(user)

    def export_to_file(self, fileName):
        with open(fileName, 'w+') as fp:
            for user in self.users:
                fp.write("{}\n".format(user.get_username()))
                fp.write("{}\n".format(user.get_name()))
                fp.write("{}\n".format(user.get_avatar()))
                # fp.write("followers")
                followers = user.get_followers()
                if followers:
                    for i in range(len(followers)):
                        fp.write("{}".format(followers[i]))
                        if i < len(followers)-1:
                            fp.write(",")
                    fp.write('\n')
                else:
                    fp.write("None\n")
                following = user.get_following()
                if following:
                    for i in range(len(following)):
                        fp.write("{}".format(following[i]))
                        if i < len(following)-1:
                            fp.write(",")
                    fp.write('\n')
                else:
                    fp.write("None\n")


# token = "b6901330af2a0e6d1f03ad11d2cd8ce10d6c3501"
def main():

    try:
        if not path.isfile(argv[1]):
            raise IOError("File not found")
        fileName = argv[1]
        token = "b6901330af2a0e6d1f03ad11d2cd8ce10d6c3501"
    except IndexError as e:
        print('\n')
        print("Error: Please check given params\n")
        print("Usage:")
        print("\t{} <path_to_file_with_usernames> <token>".format(argv[0]))
        print('\n')
        exit(1)
    except IOError as e:
        print('\n')
        print("Error: {}".format(str(e)))
        print("Please give a valid input file")
        print('\n')
        exit(1)

    usersList = GithubUsersList(token)
    usersList.create_users(usersList.get_users_list(fileName), 1)
    usersList.set_last_relations()
    usersList.export_to_file('teste')
    users = usersList.get_users()

    print('Total: {}'.format(len(users)))

if __name__ == '__main__':
    main()