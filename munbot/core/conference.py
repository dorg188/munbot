import discord

from munbot.core.exceptions import InvalidCommittee


class Conference(object):
    def __init__(self, name: str, guild: discord.Guild):
        self._name = name
        self.guild = guild
        self._committees = dict()
    
    @property
    def name(self):
        return self._name
    
    @property
    def committees(self):
        return self._committees.values()
    
    async def register_committee(self, committee):
        if not committee.name in self._committees:
            self._committees[committee.name] = committee
            await committee.initialize_committee()
        else:
            raise InvalidCommittee(f'A {committee.name} committee is already registered to the {self.name} conference!')
    
    async def remove_committee(self, committee_name):
        if committee_name in self._committees:
            committee = self._committees.pop(committee_name)
            await committee.finalize_committee()
        else:
            raise InvalidCommittee(f'A {committee_name} committee was never registered to the {self.name} conference!')
    
    def get_committee_by_name(self, committee_name):
        if committee_name in self._committees:
            return self._committees[committee_name]
        else:
            raise InvalidCommittee(f'A {committee_name} committee was never registered to the {self.name} conference!')
    
    async def register_delegation(self, committee_name, delegation):
        await self.get_committee_by_name(committee_name).add_delegation(delegation)
        
    async def remove_delegation(self, committee_name, delegation_country):
        await self.get_committee_by_name(committee_name).remove_delegation(delegation_country)
