import typing
import discord
from munbot.core.conference import Conference


class Committee(object):
    def __init__(self, conference: Conference, name: str, topics: typing.List[str],
                 chairs: typing.List[typing.Union[discord.User, discord.Member]]):
        self._conference = conference
        self._name = name
        self._chairs = chairs
        self.topics = topics
        self._delegations = dict()
    
    @property
    def conference(self):
        return self._conference
    
    @property
    def name(self):
        return self._name
    
    @property
    def chairs(self):
        return tuple(self._chairs)
    
    @property
    def delegations(self):
        return self._delegations.values()
    
    def add_delegation(self, delegation):
        if not delegation.country in self.delegations:
            self._delegations[delegation.country] = delegation
        else:
            raise KeyError(f'A delegation from {delegation.country.name} is already registered!')
    
    def remove_delegation(self, country):
        if country in self.delegations:
            self._delegations.pop(country)
        else:
            raise KeyError(f'A delegation from {country.name} is not registered!')
