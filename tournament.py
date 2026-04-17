from ex0 import AquaFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    DefensiveStrategy,
    NormalStrategy,
    run_tournament,
)


def main() -> None:
    try:
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        healing_factory = HealingCreatureFactory()
        transform_factory = TransformCreatureFactory()

        normal = NormalStrategy()
        aggressive = AggressiveStrategy()
        defensive = DefensiveStrategy()

        run_tournament(
            "Tournament 0 (basic)",
            [(flame_factory, normal), (healing_factory, defensive)],
        )
        run_tournament(
            "Tournament 1 (error)",
            [(flame_factory, aggressive), (healing_factory, defensive)],
        )
        run_tournament(
            "Tournament 2 (multiple)",
            [
                (aqua_factory, normal),
                (healing_factory, defensive),
                (transform_factory, aggressive),
            ],
        )
    except Exception as exc:
        print(f"Tournament script error: {exc}")


if __name__ == "__main__":
    main()
