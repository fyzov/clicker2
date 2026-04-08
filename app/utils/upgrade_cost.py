from functools import lru_cache

from app.config import Config


@lru_cache(maxsize=None)
def calculate_upgrade_cost(level):
    if level <= 1:
        return 0

    cost = Config.BASE_COST * (Config.MULTIPLIER ** (level - 2))
    return round(cost)


def clear_upgrade_cache():
    calculate_upgrade_cost.cache_clear()
