from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import BluePrinceWorld


def set_all_rules(world: BluePrinceWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


# TODO implement entrance rules.
def set_all_entrance_rules(world: BluePrinceWorld) -> None:
    {}


# TODO implement location rules.
def set_all_location_rules(world: BluePrinceWorld) -> None:
    {}


def set_completion_condition(world: BluePrinceWorld) -> None:

    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
