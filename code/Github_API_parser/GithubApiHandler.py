# coding: utf-8

import requests

class UsersHandler():
    base_url = "https://api.github.com/users/"

    def __init__(self, token):
        self.auth = {
            "Authorization":"token {}".format(token)}

    def get_user_profile(self, user):
        user_url = self.base_url + user
        res = requests.get(user_url, headers=self.auth)
        return res.json()

    def get_user_followers(self, user):
        followers = []
        followers_url = self.base_url + user + '/followers'
        res = requests.get(followers_url, headers=self.auth)
        for item in res.json():
            followers.append(item['login'])
        return followers

    def get_user_following(self, user):
        following = []
        following_url = self.base_url + user + '/following'
        res = requests.get(following_url, headers=self.auth)
        for item in res.json():
            following.append(item['login'])
        return following