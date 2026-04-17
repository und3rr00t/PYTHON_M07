from ex0.creature import Creature
from ex0.factories import CreatureFactory
from ex1.creatures import Bloomelle, Morphagon, Shiftling, Sproutling


class HealingCreatureFactory(CreatureFactory):

    @property
    def family_key(self) -> str:
        return "Healing"

    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):

    @property
    def family_key(self) -> str:
        return "Transform"

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
