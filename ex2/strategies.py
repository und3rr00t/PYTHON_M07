from abc import ABC, abstractmethod
from ex0.creature import Creature
from ex1.capabilities import HealCapability, TransformCapability
from ex2.errors import InvalidBattleStrategyError


class BattleStrategy(ABC):

    @property
    @abstractmethod
    def bracket_name(self) -> str:
        ...

    @property
    @abstractmethod
    def error_token(self) -> str:
        ...

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> list[str]:
        ...

    def _ensure_valid(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidBattleStrategyError(creature.name, self.error_token)


class NormalStrategy(BattleStrategy):

    @property
    def bracket_name(self) -> str:
        return "Normal"

    @property
    def error_token(self) -> str:
        return "normal"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> list[str]:
        self._ensure_valid(creature)
        return [creature.attack()]


class AggressiveStrategy(BattleStrategy):

    @property
    def bracket_name(self) -> str:
        return "Aggressive"

    @property
    def error_token(self) -> str:
        return "aggressive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> list[str]:
        self._ensure_valid(creature)
        if not isinstance(creature, TransformCapability):
            raise InvalidBattleStrategyError(creature.name, self.error_token)
        transformable = creature
        lines = [
            transformable.transform(),
            transformable.attack(),
            transformable.revert(),
        ]
        return lines


class DefensiveStrategy(BattleStrategy):

    @property
    def bracket_name(self) -> str:
        return "Defensive"

    @property
    def error_token(self) -> str:
        return "defensive"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> list[str]:
        self._ensure_valid(creature)
        if not isinstance(creature, HealCapability):
            raise InvalidBattleStrategyError(creature.name, self.error_token)
        return [creature.attack(), creature.heal()]
