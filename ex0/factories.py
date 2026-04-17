from abc import ABC, abstractmethod
from ex0.creature import Aquabub, Creature, Flameling, Pyrodon, Torragon


class CreatureFactory(ABC):

    @property
    @abstractmethod
    def family_key(self) -> str:
        ...

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):

    @property
    def family_key(self) -> str:
        return "Flameling"

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):

    @property
    def family_key(self) -> str:
        return "Aquabub"

    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
