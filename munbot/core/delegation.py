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
    def committee(self) -> Committee:
        return self._committee
    
    @property
    def guild(self) -> discord.Guild:
        return self._committee.guild
    
    @property
    def country(self) -> Countries:
        return self._country
    
    def whisper(self, country: Countries, message: str):
        pass

    def message_chairs(self, message: str):
        pass

    def submit_clause(self, clause_file: discord.File, message: str = None):
        pass

    def submit_amendment(self, amendment: str, amendment_file: discord.File = None):
        pass

    def submit_directive(self, directive: str, private: bool = False, directive_file: discord.File = None):
        pass
