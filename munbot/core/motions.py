import abc
import discord

from munbot.core.countries import Countries
from munbot.core.delegation import Delegation


class Motion(object, metaclass=abc.ABCMeta):
    def __init__(self, delegation: Delegation):
        self._delegation = delegation

    @property
    def delegation(self) -> Delegation:
        return self._delegation
    
    @property
    def committee(self):
        return self._delegation.committee

    @abc.abstractmethod
    def get_motion_description(self) -> str:
        pass

    async def publish_motion(self):
        await self.committee.main_text_channel.send()

    async def vote_motion(self):
        pass

    def __str__(self):
        return f'{self._delegation.country.get_country_name()}: {self.get_motion_description()}'


class OpenGeneralSpeakersList(Motion):
    def get_motion_description(self):
        return 'Motion to Open General Speakers\' List'


class RollCallVote(Motion):
    def get_motion_description(self):
        return 'Motion for a Roll Call Vote'


class DivideTheHouse(Motion):
    def get_motion_description(self):
        return 'Motion to Divide the House'


class VotingProcedure(Motion):
    def get_motion_description(self):
        return 'Motion to move to Voting Procedure'


class OverruleChairsDecision(Motion):
    def get_motion_description(self):
        return 'Motion to Overrule Chairs Desicion'


class AdjornSession(Motion):
    def get_motion_description(self):
        return 'Motion to Adjorn Session'


class AdjornClause(Motion):
    def get_motion_description(self):
        return 'Motion to Adjorn Clause'


class ExtendPOIs(Motion):
    def get_motion_description(self):
        return 'Motion to Extend Time for POIs'


class ExtendCaucusTime(Motion):
    def __init__(self, delegation: Delegation, extension_time_mins: int):
        super().__init__(delegation)
        self.extension_time_mins = extension_time_mins

    def get_motion_description(self):
        return f'Motion to Extend Caucus Time by {self.extension_time_mins} mins'


class ModeratedCaucus(Motion):
    def __init__(self, delegation: Delegation, subject: str, total_speaking_mins: int, speaker_time_secs: int):
        super().__init__(delegation)
        self.subject = subject
        self.total_speaking_mins = total_speaking_mins
        self.speaker_time_secs = speaker_time_secs

    def get_motion_description(self):
        return f'Motion for a Moderated Caucus on the subject of {self.subject} ' \
               f'({self.total_speaking_mins} mins, {self.speaker_time_secs} secs speaker time)'


class UnmoderatedCaucus(Motion):
    def __init__(self, delegation: Delegation, total_time_mins: int):
        super().__init__(delegation)
        self.total_time_mins = total_time_mins
    
    def get_motion_description(self):
        return f'Motion for an Unmoderated Caucus for {self.total_time_mins} mins'
