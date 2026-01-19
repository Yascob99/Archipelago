from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BluePrinceWorld


def create_and_connect_regions(world: BluePrinceWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


# TODO implement sub-regions
# TODO implement regions for each of the rooms


def create_all_regions(world: BluePrinceWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.

    # Above Ground Grounds
    campsite = Region("The Campsite", world.player, world.multiworld)
    campsite = Region("The Grounds", world.player, world.multiworld)
    campsite = Region("Private Drive", world.player, world.multiworld)
    campsite = Region("Apple Orchard", world.player, world.multiworld)
    campsite = Region("Gemstone Cavern", world.player, world.multiworld)
    campsite = Region("Sealed Entrance", world.player, world.multiworld)
    campsite = Region("Blackbridge Grotto", world.player, world.multiworld)
    campsite = Region("Orindian Ruins", world.player, world.multiworld)
    campsite = Region("Tunnel Area", world.player, world.multiworld)
    campsite = Region("West Path", world.player, world.multiworld)
    campsite = Region("Outer Room", world.player, world.multiworld)
    campsite = Region("Gemstone Cavern", world.player, world.multiworld)

    # Underground area

    # Note: These are NOT the final list of areas. The regions are all able to be broken up more.
    # TODO Need to work with Gelly to determine the full list for all regions.
    campsite = Region("Abandoned Mine", world.player, world.multiworld)
    campsite = Region("Basement", world.player, world.multiworld)
    campsite = Region("Catacombs", world.player, world.multiworld)
    campsite = Region("Inner Sanctum", world.player, world.multiworld)
    campsite = Region("The Precipice", world.player, world.multiworld)
    campsite = Region("Reservoir", world.player, world.multiworld)
    campsite = Region("Rotating Gear", world.player, world.multiworld)
    campsite = Region("Safehouse", world.player, world.multiworld)
    campsite = Region("Torch Chamber", world.player, world.multiworld)
    campsite = Region("The Underpass", world.player, world.multiworld)
    campsite = Region("Aries Court", world.player, world.multiworld)
    campsite = Region("The Well", world.player, world.multiworld)

    # Hard-coded rooms?
    campsite = Region("The Antechamber", world.player, world.multiworld)
    campsite = Region("Room 46", world.player, world.multiworld)
    campsite = Region("Entrance Hall", world.player, world.multiworld)
    # ...
    # TODO each room individually is a region under room-sanity.
    campsite = Region("Room X", world.player, world.multiworld)

    # TODO question: Do any rooms require region parts?
    # Pool trunks for example? I think requires region access to pump room AND pool room?

    # Let's put all these regions in a list.
    regions = [campsite]

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: BluePrinceWorld) -> None:
    campsite = world.get_region("The Campsite")
