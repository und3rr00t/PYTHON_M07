from typing import Sequence
from ex0.creature import Creature
from ex0.factories import CreatureFactory
from ex2.errors import InvalidBattleStrategyError
from ex2.strategies import BattleStrategy


def format_opponent_banner(
    opponents: Sequence[tuple[CreatureFactory, BattleStrategy]],
) -> str:
    inner = ", ".join(
        f"({factory.family_key}+{strategy.bracket_name})"
        for factory, strategy in opponents
    )
    return f"[ {inner} ]"


def run_battle(
    factory_a: CreatureFactory,
    strategy_a: BattleStrategy,
    factory_b: CreatureFactory,
    strategy_b: BattleStrategy,
) -> None:
    creature_a: Creature = factory_a.create_base()
    creature_b: Creature = factory_b.create_base()
    print()
    print("* Battle *")
    print(creature_a.describe())
    print(" vs.")
    print(creature_b.describe())
    print("now fight!")
    for line in strategy_a.act(creature_a):
        print(line)
    for line in strategy_b.act(creature_b):
        print(line)


def run_tournament(
    title: str,
    opponents: list[tuple[CreatureFactory, BattleStrategy]],
) -> None:
    print()
    print(title)
    print(format_opponent_banner(opponents))
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                fa, sa = opponents[i]
                fb, sb = opponents[j]
                run_battle(fa, sa, fb, sb)
    except InvalidBattleStrategyError as exc:
        print(f"Battle error, aborting tournament: {exc}")
    except Exception as exc:
        print(f"Unexpected tournament error, aborting tournament: {exc}")
