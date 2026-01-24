from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .rooms import rooms
from .constants import *

if TYPE_CHECKING:
    from .world import BluePrinceWorld


# TODO add atelier
# TODO check lambdas for items/events that I need to add/create.
def create_and_connect_regions(world: BluePrinceWorld) -> None:

    ##################
    # CREATE REGIONS #
    ##################

    # Creating a region is as simple as calling the constructor of the Region class.

    abandoned_mine = Region(
        "Abandoned Mine", world.player, world.multiworld
    )  # (area off the 9'oclock on the underground map.)
    excavation_tunnel = Region(
        "Excavation Tunnel", world.player, world.multiworld
    )  # Area to the left of the res not past minecart on map.
    basement = Region("Basement", world.player, world.multiworld)
    catacombs = Region("Catacombs", world.player, world.multiworld)
    inner_sanctum = Region("Inner Sanctum", world.player, world.multiworld)
    the_precipice = Region("The Precipice", world.player, world.multiworld)
    reservoir_gear_side = Region("Reservoir Gear Side", world.player, world.multiworld)
    reservoir_fountain_side = Region(
        "Reservoir Fountain Side", world.player, world.multiworld
    )
    reservoir_bottom = Region("Reservoir Bottom", world.player, world.multiworld)
    rotating_gear = Region("Rotating Gear", world.player, world.multiworld)
    safehouse = Region("Safehouse", world.player, world.multiworld)
    torch_chamber = Region("Torch Chamber", world.player, world.multiworld)
    the_underpass = Region("The Underpass", world.player, world.multiworld)
    aries_court = Region("Aries Court", world.player, world.multiworld)
    the_well = Region("The Well", world.player, world.multiworld)
    campsite = Region("Campsite", world.player, world.multiworld)
    grounds = Region("Grounds", world.player, world.multiworld)
    private_drive = Region("Private Drive", world.player, world.multiworld)
    apple_orchard = Region("Apple Orchard", world.player, world.multiworld)
    gemstone_cavern = Region("Gemstone Cavern", world.player, world.multiworld)
    sealed_entrance = Region("Sealed Entrance", world.player, world.multiworld)
    blakbridge_grotto = Region("Blackbridge Grotto", world.player, world.multiworld)
    orindian_ruins = Region("Orindian Ruins", world.player, world.multiworld)
    tunnel_area_entrance = Region(
        "Tunnel Area Entrance", world.player, world.multiworld
    )
    west_path = Region("West Path", world.player, world.multiworld)
    outer_room = Region("Outer Room", world.player, world.multiworld)
    gemstone_cavern = Region("Gemstone Cavern", world.player, world.multiworld)
    foundation_elevator = Region("Foundation Elevator", world.player, world.multiworld)
    tunnel_area_post_crates = Region(
        "Tunnel Area Past Crates", world.player, world.multiworld
    )
    tunnel_area_post_normal_locked_door = Region(
        "Tunnel Area Past Normal Locked Door", world.player, world.multiworld
    )
    tunnel_area_post_basement_key_door = Region(
        "Tunnel Area Past Basement key Door", world.player, world.multiworld
    )
    tunnel_area_post_security_door = Region(
        "Tunnel Area Past Security Door", world.player, world.multiworld
    )
    tunnel_area_post_weak_wall = Region(
        "Tunnel Area Past Weak Wall", world.player, world.multiworld
    )
    tunnel_area_post_red_door = Region(
        "Tunnel Area Past Red Door", world.player, world.multiworld
    )
    tunnel_area_post_candle_door = Region(
        "Tunnel Area Past Candle Door", world.player, world.multiworld
    )
    tunnel_area_post_sealed_door = Region(
        "Tunnel Area Past Sealed Door", world.player, world.multiworld
    )
    tunnel_area_post_blue_door = Region(
        "Tunnel Area Past Blue Door", world.player, world.multiworld
    )

    regions = [
        abandoned_mine,
        excavation_tunnel,
        basement,
        catacombs,
        inner_sanctum,
        the_precipice,
        reservoir_gear_side,
        reservoir_fountain_side,
        reservoir_bottom,
        rotating_gear,
        safehouse,
        torch_chamber,
        the_underpass,
        aries_court,
        the_well,
        campsite,
        grounds,
        private_drive,
        apple_orchard,
        gemstone_cavern,
        sealed_entrance,
        blakbridge_grotto,
        orindian_ruins,
        tunnel_area_entrance,
        west_path,
        outer_room,
        gemstone_cavern,
        tunnel_area_post_crates,
        tunnel_area_post_normal_locked_door,
        tunnel_area_post_basement_key_door,
        tunnel_area_post_security_door,
        tunnel_area_post_weak_wall,
        tunnel_area_post_red_door,
        tunnel_area_post_candle_door,
        tunnel_area_post_sealed_door,
        tunnel_area_post_blue_door,
    ]

    for k, v in rooms.items():
        regions.append(Region(k, world.player, world.multiworld))

    world.multiworld.regions += regions

    # For external Connections later

    ###################
    # CONNECT REGIONS #
    ###################

    # Get regions I am going to need later.
    tomb = world.get_region("Tomb")
    garage = world.get_region("Garage")
    foundation = world.get_region("Foundation")

    # Go through the rooms and connect them to the outer room/campsite (starting area)
    for k, v in rooms.items():
        if v[OUTER_ROOM_KEY]:
            room = world.get_region(k)

            # Connect room to outer room if you have that room
            outer_room.connect(
                room, f"Outer Room To {k}", lambda state: state.has(k, world.player)
            )
        else:
            # Connect all other rooms to outer room if you have that room unlocked and the shrine to monk.
            # TODO this doesent take into acount that you must first reach the room in the normal manner first, which has its own logic.
            # outer_room.connect(
            #     room,
            #     f"Outer Room To {k}",
            #     lambda state: state.has(k, world.player) and state.has("Shrine"),
            # )

            # TODO: This does not take into account that you need to have some level of placement restriction
            # Connect all other rooms to campsite (entrance hall?) if you have that room unlocked
            grounds.connect(
                room, f"Campsite To {k}", lambda state: state.has(k, world.player)
            )

    foundation.connect(foundation_elevator, "Foundation To Foundation Elevator")

    campsite.connect(private_drive, "Campsite To Private Drive")
    campsite.connect(apple_orchard, "Campsite To Apple Orchard")
    campsite.connect(
        gemstone_cavern,
        "Campsite To Gemstone Cavern",
        lambda state: state.has("Utility Closet", world.player),
    )  # Rules of are found in office emails. Solution is in office emails. May be able to adjust pattern?
    private_drive.connect(
        blakbridge_grotto,
        "Private Drive To Blackbridge Grotto",
        lambda state: state.has("Boiler Room", world.player),
    )
    private_drive.connect(grounds, "Private Drive To Frounds")
    blakbridge_grotto.connect(
        orindian_ruins,
        "Blackbridge Grotto To Orindian Ruins",
        lambda state: state.has_all(
            {"Microchip 1", "Microchip 2", "Microchip 3"}, world.player
        ),
    )
    grounds.connect(
        the_precipice, "Grounds To Precipice"
    )  # TODO Having blue flame elevator access. Requires (1: apple orchard, 2: outer room (school house, hovel), 3: Gemstone Cavern)
    grounds.connect(
        sealed_entrance,
        "Grounds To Sealed Entrance",
        lambda state: state.has("Powerhammer Access", world.player),
    )
    sealed_entrance.connect(
        grounds,
        "Sealed Entrance To Grounds",
        lambda state: state.has("Powerhammer Access", world.player),
    )
    the_precipice.connect(
        aries_court, "Precipice to Aries Court"
    )  # TODO (requires solving Castle puzzle, which requires specific room sets.)
    sealed_entrance.connect(
        basement,
        "Sealed Entrance To Basement",
        lambda state: state.has("Powerhammer Access", world.player),
    )
    basement.connect(
        sealed_entrance,
        "Basement To Sealed Entrance",
        lambda state: state.has("Powerhammer Access", world.player),
    )
    basement.connect(reservoir_gear_side, "Basement To Reservoir Gear Side")
    reservoir_gear_side.connect(basement, "Reservoir Gear Side To Basement")
    reservoir_gear_side.connect(rotating_gear, "Reservoir Gear Side To Rotating Gear")
    rotating_gear.connect(reservoir_gear_side, "Rotating Gear To Reservoir Gear Side")
    the_underpass.connect(inner_sanctum, "The Underpass To Inner Sanctum")
    abandoned_mine.connect(excavation_tunnel, "Abandoned Mine To Excavation Tunnel")
    excavation_tunnel.connect(abandoned_mine, "Excavation Tunnel To Abandoned Mine")
    excavation_tunnel.connect(torch_chamber, "Excavation Tunnel To Torch Chamber")
    excavation_tunnel.connect(
        reservoir_fountain_side, "Reservoir Fountain Side To Excavation Tunnel"
    )
    reservoir_fountain_side.connect(
        excavation_tunnel, "Reservoir Fountain Side To Excavation Tunnel"
    )
    the_well.connect(
        reservoir_fountain_side,
        "Well To Reservoir Fountain Side",
        lambda state: state.has("Pump Room", world.player)
        and state.has("Basement Key", world.player),
    )

    west_path.connect(
        grounds,
        "West Path To Grounds",
        lambda state: state.has("Garage", world.player)
        and (
            state.has("Utility Closet", world.player)
            or state.has("Boiler Room", world.player)
        ),
    )
    tomb.connect(catacombs, "Tomb to Catacombs")
    catacombs.connect(excavation_tunnel, "Catacombs to Excavation Tunnel")
    west_path.connect(outer_room, "West Path To Outer Room")
    garage.connect(west_path, "Garage To West Path")
    foundation_elevator.connect(
        basement,
        "Foundation Elevator To Basement",
        lambda state: state.has("The Foundation", world.player)
        and state.has("Basement Key", world.player),
    )
    torch_chamber.connect(
        the_precipice,
        "Torch Chamber To Precipice",
        lambda state: state.has("Burning Glass Access", world.player)
        and state.has("Torch Access", world.player),
    )

    grounds.connect(tunnel_area_entrance, "Grounds To Tunnel Area Entrance")
    tunnel_area_entrance.connect(
        tunnel_area_post_crates,
        "Tunnel Area Entrance To Tunnel Area Post Crates",
        lambda state: state.has("Satellite Raised", world.player)
        and (
            state.has("Laboratory", world.player)
            or state.has("Blackbridge Grotto Access", world.player)
        ),
    )
    tunnel_area_post_crates.connect(
        tunnel_area_post_normal_locked_door,
        "Tunnel Area Post Crates to Tunnel Area Post Normal Locked Door",
        lambda state: state.has("Normal Keys", world.player),
    )
    tunnel_area_post_normal_locked_door.connect(
        tunnel_area_post_basement_key_door,
        "Tunnel Area Post Normal Locked Door to Tunnel Area Post Basement Key",
        lambda state: state.has("Basement Key", world.player),
    )
    tunnel_area_post_basement_key_door.connect(
        tunnel_area_post_security_door,
        "Tunnel Area Post Basement Key to Tunnel Area Post Security Door",
        lambda state: state.has("Security Key", world.player),
    )
    tunnel_area_post_security_door.connect(
        tunnel_area_post_weak_wall,
        "Tunnel Area Post Security Door to Tunnel Area Post Weak Wall",
        lambda state: state.has("Powerhammer Access", world.player),
    )
    tunnel_area_post_weak_wall.connect(
        tunnel_area_post_red_door,
        "Tunnel Area Post Weak Wall to Tunnel Area Post Red Door",
        lambda state: state.has("Boiler Room", world.player),
    )
    tunnel_area_post_red_door.connect(
        tunnel_area_post_candle_door,
        "Tunnel Area Post Red Door to Tunnel Area Post Candle Door",
        lambda state: state.has("Torch Access", world.player)
        or state.has("Burning Glass Access", world.player),
    )
    tunnel_area_post_candle_door.connect(
        tunnel_area_post_sealed_door,
        "Tunnel Area Post Candle Door to Tunnel Area Post Sealed Door",
        lambda state: state.has_all(
            {"Microchip 1", "Microchip 2", "Microchip 3"}, world.player
        ),
    )
    tunnel_area_post_sealed_door.connect(
        tunnel_area_post_blue_door,
        "Tunnel Area Post Sealed Door to Tunnel Area Post Blue Door",
        lambda state: state.has("Blue Door Access", world.player),
    )

    ###################################
    # COMPLEX REGION CONNECTION LOGIC #
    ###################################
    # TODO (These connections have quite complex logic relating to the )
    reservoir_gear_side.connect(
        safehouse, "Reservoir Gear Side To Safehouse"
    )  # Pump Room & Fountain Side Access. (take fountain side to gear side, lower again, and make it back down on gear side.)
    reservoir_gear_side.connect(
        reservoir_bottom, "Reservoir Gear Side To Reservoir Bottom"
    )  # Pump Room and boiler room (both this and safehouse require ability to get to gear side NOT through well side.)
    rotating_gear.connect(
        the_underpass, "Rotating Gear To Underpass"
    )  # Require Dual side access
    rotating_gear.connect(abandoned_mine, "Rotating Gear To Abandoned Mine")
    reservoir_fountain_side.connect(
        reservoir_gear_side, "Reservoir Fountain Side To Reservoir Gear Side"
    )  # Pump Room
