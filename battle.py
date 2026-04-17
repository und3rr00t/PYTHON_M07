from ex0 import AquaFactory, CreatureFactory, FlameFactory


def verify_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()
    for creature in (base, evolved):
        print(creature.describe())
        print(creature.attack())
    print()


def battle_bases(
    factory_a: CreatureFactory,
    factory_b: CreatureFactory,
) -> None:
    print("Testing battle")
    a = factory_a.create_base()
    b = factory_b.create_base()
    print(a.describe())
    print(" vs.")
    print(b.describe())
    print(" fight!")
    print(a.attack())
    print(b.attack())


def main() -> None:
    try:
        flame = FlameFactory()
        aqua = AquaFactory()
        verify_factory(flame)
        verify_factory(aqua)
        battle_bases(flame, aqua)
    except Exception as exc:
        print(f"Battle script error: {exc}")


if __name__ == "__main__":
    main()
