from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

from .data_rooms import rooms

if TYPE_CHECKING:
    from .world import BluePrinceWorld


LOCATION_NAME_TO_ID = {
    "Entrance Hall East Vase": 0,
    "Entrance Hall West Vase": 1,
    # TODO-0 add location map
    # LOCAITONS
    # First time entering a room
    # first time picking up a unique item
    # Nth time opening a trunk.
    # Vanilla room unlocks.
}


class BluePrinceLocation(Location):
    game = "Blue Prince"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BluePrinceWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BluePrinceWorld) -> None:

    # TODO-0 create locations
    bottom_right_room = world.get_region("Entrance Hall")
    bottom_right_room_locations = get_location_names_with_ids(["Entrance Hall East Vase", "Entrance Hall West Vase"])
    bottom_right_room.add_locations(bottom_right_room_locations, BluePrinceLocation)


def create_events(world: BluePrinceWorld) -> None:
    campsite = world.get_region("The Campsite")  # For Sanctum Solves Victory.
    antechamber = world.get_region("The Antechamber")
    room_46 = world.get_region("Room 46")
    throneroom = world.get_region("Throne Room")
    atelier = world.get_region("The Atelier")

    # Set Victory as entering antechamber
    if world.options.goal_type.value == BluePrinceWorld.options.goal_type.option_antechamber:
        antechamber.add_event(
            "Entered The Antechamber",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as reaching room 46
    if world.options.goal_type.value == BluePrinceWorld.options.goal_type.option_room46:
        room_46.add_event(
            "Room 46 Victory",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as opening X Sanctums.
    if world.options.goal_type.value == BluePrinceWorld.options.goal_type.option_sanctum:
        # Generate the necessary events for the solve count.
        for region in [
            "Sanctum 1",
            "Sanctum 2",
            "Sanctum 3",
            "Sanctum 4",
            "Sanctum 5",
            "Sanctum 6",
            "Sanctum 7",
            "Sanctum 8",
        ]:
            world.get_region(region).add_event(
                f"Solved {region}",
                "Sanctum Solve",
                location_type=BluePrinceLocation,
                item_type=items.BluePrinceItem,
            )

        # Add solve count victory condition.
        campsite.add_event(
            "Solved Sanctums",
            "Victory",
            rule=lambda state: state.has("Sanctum Solve", world.player, world.options.goal_sanctum_solves.value),
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as ascending to the throne
    if world.options.goal_type.value == BluePrinceWorld.options.goal_type.option_ascend:
        throneroom.add_event(
            "Ascended The Throne",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )

    # Set Victory as entering the atelier and reading the blue prints.
    if world.options.goal_type.value == BluePrinceWorld.options.goal_type.option_blueprints:

        atelier.add_event(
            "Read The Blue Prints",
            "Victory",
            location_type=BluePrinceLocation,
            item_type=items.BluePrinceItem,
        )
