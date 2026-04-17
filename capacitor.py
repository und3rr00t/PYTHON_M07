from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def demonstrate_healing_factory() -> None:
    factory = HealingCreatureFactory()
    print("Testing Creature with healing capability")
    pairs = (
        ("base", factory.create_base),
        ("evolved", factory.create_evolved),
    )
    for label, maker in pairs:
        print(f" {label}:")
        creature = maker()
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())

    print()


def demonstrate_transform_factory() -> None:
    factory = TransformCreatureFactory()
    print("Testing Creature with transform capability")
    pairs = (
        ("base", factory.create_base),
        ("evolved", factory.create_evolved),
    )
    for label, maker in pairs:
        print(f" {label}:")
        creature = maker()
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
    print()


def main() -> None:
    try:
        demonstrate_healing_factory()
        demonstrate_transform_factory()
    except Exception as exc:
        print(f"Capacitor script error: {exc}")


if __name__ == "__main__":
    main()
