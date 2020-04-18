import discord


class Conference(object):
    def __init__(self, name: str):
        self._name = name
        self._committees = dict()
    
    @property
    def name(self):
        return self._name
    
    @property
    def committees(self):
        return self._committees.values()
    
    def register_committee(self, committee):
        if not committee.name in self._committees:
            self._committees[committee.name] = committee
        else:
            raise KeyError(f'A {committee.name} committee is already registered!')
