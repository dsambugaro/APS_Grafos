#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from grafo import Graph


def main():
    G = Graph(is_directional=True)

    print("\n\n")
    print("Loading graph...")

    with open('following_followers', 'r') as fp:
        count_line = 0
        user = []
        for line in fp:
            user.append(line)
            count_line += 1
            if count_line == 5:
                count_line = 0
                username = user[0].strip('\n')
                name = user[1].strip('\n')
                avatar = user[1].strip('\n')

                followers = list(user[3].strip('\n').split(','))
                for follower in followers:
                    if follower == 'None':
                        break
                    G.add_vertex([(follower, username)])

                following = list(user[4].strip('\n').split(','))
                for user_following in following:
                    if user_following == 'None':
                        break
                    G.add_vertex([(username, user_following)])
                user = []

    print("Graph loaded!")
    print("\n==========================================\n")
    print("Edges count: ", G.edges_count)
    print("Order: ", G.get_order())
    print("\n==========================================\n")
    print("\n\n")
    print("Ctrl + C to quit")
    while True:
        try:
            user_1 = input('User 1: ')
            user_2 = input('User 2: ')
            print("\n\n")

            if G.get_vertex(user_1):
                if G.get_vertex(user_2):
                    print("Separation degree: ", G.breadth_first_search(user_1, user_2))
                else:
                    print("User 2 '{}' is'n in this graph :<".format(user_2))
            else:
                print("User 1 '{}' is'n in this graph :<".format(user_1))
                if not G.get_vertex(user_2):
                    print("User 2 '{}' is'n in this graph :<".format(user_2))

            print("\n==========================================\n\n")
        except KeyboardInterrupt as e:
            print("\n\n")
            out = input('Do you really want to quit? [Y/n]: ')
            if out != 'n' and out != 'no' and out != 'N' and out != 'NO' and out != 'No' and out != 'nO':
                exit(0)

if __name__ == '__main__':
    main()
