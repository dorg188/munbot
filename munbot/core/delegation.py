import typing
import discord
from munbot.core.committee import Committee
from munbot.core.countries import Countries


class Delegation(object):
    def __init__(self, committee: Committee, country: Countries,
                 *delegates: typing.List[typing.Union[discord.User, discord.Member]]):
        self._committee = committee
        self._country = country
        self.delegates = delegates
    
    @property
    def committee(self):
        return self._committee
    
    @property
    def country(self):
        return self._country
