from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .rooms import rooms
from .constants import *

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
    grounds = Region("The Grounds", world.player, world.multiworld)
    private_drive = Region("Private Drive", world.player, world.multiworld)
    apple_orchard = Region("Apple Orchard", world.player, world.multiworld)
    gemstone_cavern = Region("Gemstone Cavern", world.player, world.multiworld)
    sealed_entrance = Region("Sealed Entrance", world.player, world.multiworld)
    blakbridge_grotto = Region("Blackbridge Grotto", world.player, world.multiworld)
    orindian_ruins = Region("Orindian Ruins", world.player, world.multiworld)
    tunnel_area = Region("Tunnel Area", world.player, world.multiworld)
    west_path = Region("West Path", world.player, world.multiworld)
    outer_room = Region("Outer Room", world.player, world.multiworld)
    gemstone_cavern = Region("Gemstone Cavern", world.player, world.multiworld)

    # Underground area

    # Note: These are NOT the final list of areas. The regions are all able to be broken up more.
    # TODO Need to work with Gelly to determine the full list for all regions.
    abandoned_mine = Region("Abandoned Mine", world.player, world.multiworld)
    basement = Region("Basement", world.player, world.multiworld)
    catacombs = Region("Catacombs", world.player, world.multiworld)
    inner_sanctum = Region("Inner Sanctum", world.player, world.multiworld)
    the_precipice = Region("The Precipice", world.player, world.multiworld)
    reservoir = Region("Reservoir", world.player, world.multiworld)
    rotating_gear = Region("Rotating Gear", world.player, world.multiworld)
    safehouse = Region("Safehouse", world.player, world.multiworld)
    torch_chamber = Region("Torch Chamber", world.player, world.multiworld)
    the_underpass = Region("The Underpass", world.player, world.multiworld)
    aries_court = Region("Aries Court", world.player, world.multiworld)
    the_well = Region("The Well", world.player, world.multiworld)

    regions = [
        campsite,
        grounds,
        private_drive,
        apple_orchard,
        gemstone_cavern,
        sealed_entrance,
        blakbridge_grotto,
        orindian_ruins,
        tunnel_area,
        west_path,
        outer_room,
        gemstone_cavern,
        abandoned_mine,
        basement,
        catacombs,
        inner_sanctum,
        the_precipice,
        reservoir,
        rotating_gear,
        safehouse,
        torch_chamber,
        the_underpass,
        aries_court,
        the_well,
    ]

    for k, v in rooms.items():
        regions.append(Region(k, world.player, world.multiworld))

    # TODO question: Do any rooms require region parts?
    # Pool trunks for example? I think requires region access to pump room AND pool room?

    # Let's put all these regions in a list.

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: BluePrinceWorld) -> None:
    campsite = world.get_region("The Campsite")

    outer_room = world.get_region("Outer Room")
    # TODO make connections

    # Go through the rooms and connect them to the outer room/campsite (starting area)
    for k, v in rooms.items():
        if v[OUTER_ROOM_KEY]:
            room = world.get_region(k)

            # Connect room to outer room if you have that room
            outer_room.connect(
                room, f"Outer Room To {k}", lambda state: state.has(k, world.player)
            )
        else:
            # Connect all other rooms to outer room if you have that room unlocked.
            outer_room.connect(
                room, f"Outer Room To {k}", lambda state: state.has(k, world.player)
            )
            # Connect all other rooms to campsite (entrance hall?) if you have that room unlocked
            campsite.connect(
                room, f"Campsite To {k}", lambda state: state.has(k, world.player)
            )
