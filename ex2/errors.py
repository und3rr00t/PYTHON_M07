class InvalidBattleStrategyError(Exception):

    def __init__(self, creature_name: str, strategy_error_token: str) -> None:
        self.creature_name = creature_name
        self.strategy_error_token = strategy_error_token
        message = (
            f"Invalid Creature '{creature_name}' for this "
            f"{strategy_error_token} strategy"
        )
        super().__init__(message)
