import typing
import discord
from munbot.core.roles import Roles
from munbot.core.conference import Conference


class Committee(object):
    def __init__(self, conference: Conference, name: str, topics: typing.Iterable[str],
                 chairs: typing.Iterable[typing.Union[discord.User, discord.Member]],
                 admins: typing.Iterable[typing.Union[discord.User, discord.Member]] = (),
                 observers: typing.Iterable[typing.Union[discord.User, discord.Member]] = ()):
        self._conference = conference
        self._name = name
        self._chairs = list(chairs)
        self._admins = list(admins)
        self._observers = list(observers)
        self.topics = list(topics)
        self._delegations = dict()
        self._role: discord.Role
        self._category: discord.CategoryChannel
        self._permissions: dict = self._get_default_permissions()
        self._initialized = False
    
    def _get_default_permissions(self) -> dict:
        return {
            self.guild.default_role: discord.PermissionOverwrite.from_pair(discord.Permissions.none(),
                                                                           discord.Permissions.all()),
            discord.utils.get(self.guild.roles, name=Roles.Advisor): discord.PermissionOverwrite(),
            discord.utils.get(self.guild.roles, name=Roles.SecretaryGeneral): discord.PermissionOverwrite()
        }
    
    async def _create_committee_role(self):
        self._role = await self.guild.create_role(name=self.name)
    
    async def _create_committee_category(self):
        category_permissions = self._permissions.copy()
        if self._role:
            category_permissions.update({self._role: discord.PermissionOverwrite()})
        self._category = await self.guild.create_category(name=self.name, overwrites=category_permissions)
    
    async def _create_committee_channels(self):
        if self._category:
            await self._category.create_text_channel(f'{self.name}-floor')
            await self._category.create_voice_channel(f'{self.name}: Floor')
    
    async def _give_member_committee_role(self, member: typing.Union[discord.User, discord.Member]):
        if self._role and self._role not in member.roles():
            await member.add_roles(self._role)
    
    async def _remove_committee_role_from_member(self, member: typing.Union[discord.User, discord.Member]):
        if self._role and self._role in member.roles():
            await member.remove_roles(self._role)
    
    async def _give_members_committee_role(self):
        for chair in self._chairs:
            self._give_member_committee_role(chair)
        for admin in self._admins:
            self._give_member_committee_role(admin)
        for observer in self._observers:
            self._give_member_committee_role(observer)
        for delegation in self._delegations:
            for delegate in delegation.delegates:
                self._give_member_committee_role(delegate)
    
    async def initialize_committee(self):
        await self._create_committee_role()
        await self._create_committee_category()
        self._initialized = True
        await self._create_committee_channels()
        await self.create_group('Chairs', [])
        await self._give_members_committee_role()
    
    async def create_group(self, group_id: str, group_members: typing.List[typing.Union[discord.User, discord.Member]]):
        if not self._initialized:
            raise Exception('Committee not initialized!')
        channel_permissions = self._permissions.copy()
        channel_permissions.update({member: discord.PermissionOverwrite() for member in group_members})
        channel_permissions.update({member: discord.PermissionOverwrite() for member in self._chairs})
        await self._category.create_text_channel(f'{self.name}-{group_id}', overwrites=channel_permissions)
        await self._category.create_voice_channel(f'{self.name}: {group_id}', overwrites=channel_permissions)
    
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
    def admins(self):
        return tuple(self._admins)
    
    @property
    def observers(self):
        return tuple(self._observers)
    
    @property
    def delegations(self):
        return self._delegations.values()
    
    @property
    def guild(self) -> discord.Guild:
        return self._conference.guild
    
    async def add_delegation(self, delegation):
        if not delegation.country in self.delegations:
            self._delegations[delegation.country] = delegation
            for delegate in delegation.delegates:
                await self._give_member_committee_role(delegate)
        else:
            raise KeyError(f'A delegation from {delegation.country.name} is already registered!')
    
    async def add_delegations(self, delegations):
        for delegation in delegations:
            await self.add_delegation(delegation)
    
    async def remove_delegation(self, country):
        if country in self.delegations:
            delegation = self._delegations.pop(country)
            for delegate in delegation.delegates:
                await self._remove_committee_role_from_member(delegate)
        else:
            raise KeyError(f'A delegation from {country.name} is not registered!')
    
    async def add_member(self, member: typing.Union[discord.User, discord.Member], role: Roles):
        if role == Roles.Admin:
            if member not in self._admins:
                self._admins.append(member)
        elif role == Roles.Observer:
            if member not in self._observers:
                self._observers.append(member)
        await self._give_member_committee_role(member)
    
    async def remove_member(self, member: typing.Union[discord.User, discord.Member]):
        if member in self._admins:
            self._admins.remove(member)
        elif member in self._observers:
            self._observers.remove(member)
        await self._remove_committee_role_from_member(member)
