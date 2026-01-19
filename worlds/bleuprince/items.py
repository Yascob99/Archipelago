from __future__ import annotations

from typing import TYPE_CHECKING

from .rooms import rooms

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BluePrinceWorld


ITEM_NAME_TO_ID = {
    # Special Items
    "Battery Pack": 1001,
    "Broken Lever": 1002,
    "Car Keys": 1003,
    "Coin Purse": 1004,
    "Compass": 1005,
    "Coupon Book": 1006,
    "Gear Wrench": 1007,
    "Hallpass": 1008,
    "Ivory Dice": 1009,
    "Keycard": 1010,
    "Lockpick": 1011,
    "Lucky Rabbit": 1012,
    "Magnifying Glass": 1013,
    "Metal Detector": 1014,
    "Repellent": 1015,
    "Running Shoes": 1016,
    "Salt Shaker": 1017,
    "Shovel": 1018,
    "Sledgehammer": 1019,
    "Stop Watch": 1020,
    "Telescope": 1021,
    "Treasure Map": 1022,
    "Watering Can": 1023,
    "Wind-up Key": 1024,
    #  Showroom Items
    "Chronograph": 2001,
    "Emerald Bracelet": 2002,
    "Master Key": 2003,
    "Moon Pendant": 2004,
    "Ornate Compass": 2005,
    "Silver Spoon": 2006,
    #  Workshop Items
    "Burning Glass": 3001,
    "Detector Shovel": 3002,
    "Dowsing Rod": 3003,
    "Electromagnet": 3004,
    "Jack Hammer": 3005,
    "Lucky Purse": 3006,
    "Pick Sound Amplifier": 3007,
    "Power Hammer": 3008,
    # Armory Items
    "Knight's Shield": 4001,
    "Morning Star": 4002,
    "Self Igniting Torch": 4003,
    "The Axe": 4004,
    # Special Keys
    "Basement Key": 5001,
    "Key 8": 5002,
    "Key of Aries": 5003,
    "Prism Key": 5004,
    "Secret Garden Key": 5005,
    "Silver Key": 5006,
    # Vault Keys
    "Vault Key 149": 6001,
    "Vault Key 233": 6002,
    "Vault Key 304": 6003,
    "Vault Key 370": 6004,
    # Progression Items
    "Allowance Token": 7001,
    "Cursed Effigy": 7002,
    "Sanctum Key 1": 7003,
    "Sanctum Key 2": 7004,
    "Sanctum Key 3": 7005,
    "Sanctum Key 4": 7006,
    "Sanctum Key 5": 7007,
    "Sanctum Key 6": 7008,
    "Sanctum Key 7": 7009,
    "Sanctum Key 8": 7010,
    "Upgrade Disk": 7011,
    # Unique Items
    "Crown of the Blueprints": 8001,
    "Diary Key": 8002,
    "File Cabinet Key": 8003,
    "Lunch Box": 8004,
    "Microchip A": 8005,
    "Microchip B": 8006,
    "Microchip C": 8007,
    "Paper Crown": 8008,
    "Royal Scepter": 8009,
    #
    # Extra "Stuff" Items
    #
    "Extra Coin 1": 10101,
    "Extra Coin 2": 10102,
    "Extra Coin 5": 10103,
    #
    "Extra Gems 1": 10201,
    "Extra Gems 2": 10202,
    #
    "Extra Keys 1": 10301,
    "Extra Keys 2": 10302,
    "Extra Keys 3": 10303,
    #
    "Extra Dice 1": 10401,
    "Extra Dice 2": 10402,
    "Extra Dice 4": 10404,
    #
    "Extra Steps 1": 10501,
    "Extra Steps 2": 10502,
    "Extra Steps 5": 10503,
    #
    "Extra Stars 1": 10601,
    "Extra Stars 2": 10602,
    "Extra Stars 5": 10605,
    #
    "Extra Allowance 1": 10701,
    "Extra Allowance 2": 10702,
    #
    "Extra Fruits Apple": 10801,
    "Extra Fruits Banana": 10802,
    "Extra Fruits Orange": 10803,
    #
    # Traps
    #
    "Trap Freeze Items": 40101,
    "Trap Take Step 1": 40201,
    "Trap Take Step 2": 40202,
    "Trap Take Step 5": 40203,
    "Trap Lose Item": 40301,
    "Trap Lose Star 1": 40401,
    "Trap Lose Star 2": 40402,
    "Trap Lose Star 5": 40405,
    "Trap End Day": 40501,
    #
    # Trash Item from digging. Client may interpret this freely as any of the "trash" items
    #
    "Dug Up Nothing": 50000,
} | {k: v["item_id"] for k, v in rooms.items()}


DEFAULT_ITEM_CLASSIFICATIONS = {
    # Special Items
    "Battery Pack": ItemClassification.progression,
    "Broken Lever": ItemClassification.progression,
    "Car Keys": ItemClassification.useful,
    "Coin Purse": ItemClassification.useful,
    "Compass": ItemClassification.useful,
    "Coupon Book": ItemClassification.useful,
    "Gear Wrench": ItemClassification.useful,
    "Hallpass": ItemClassification.useful,
    "Ivory Dice": ItemClassification.useful,
    "Keycard": ItemClassification.progression,
    "Lockpick": ItemClassification.useful,
    "Lucky Rabbit": ItemClassification.useful,
    "Magnifying Glass": ItemClassification.progression,
    "Metal Detector": ItemClassification.useful,
    "Repellent": ItemClassification.useful,
    "Running Shoes": ItemClassification.useful,
    "Salt Shaker": ItemClassification.useful,
    "Shovel": ItemClassification.progression,
    "Sledgehammer": ItemClassification.progression,
    "Stop Watch": ItemClassification.useful,
    "Telescope": ItemClassification.progression,
    "Treasure Map": ItemClassification.progression,
    "Watering Can": ItemClassification.progression,
    "Wind-up Key": ItemClassification.progression,
    #  Showroom Items
    "Chronograph": ItemClassification.useful,
    "Emerald Bracelet": ItemClassification.useful,
    "Master Key": ItemClassification.progression,
    "Moon Pendant": ItemClassification.useful,
    "Ornate Compass": ItemClassification.useful,
    "Silver Spoon": ItemClassification.useful,
    #  Workshop Items
    "Burning Glass": ItemClassification.progression,
    "Detector Shovel": ItemClassification.progression,
    "Dowsing Rod": ItemClassification.useful,
    "Electromagnet": ItemClassification.useful,
    "Jack Hammer": ItemClassification.progression,
    "Lucky Purse": ItemClassification.useful,
    "Pick Sound Amplifier": ItemClassification.useful,
    "Power Hammer": ItemClassification.progression,
    # Armory Items
    "Knight's Shield": ItemClassification.useful,
    "Morning Star": ItemClassification.useful,
    "Self Igniting Torch": ItemClassification.progression,
    "The Axe": ItemClassification.useful,
    # Special Keys
    "Basement Key": ItemClassification.progression,
    "Key 8": ItemClassification.progression,
    "Key of Aries": ItemClassification.progression,
    "Prism Key": ItemClassification.useful,
    "Secret Garden Key": ItemClassification.progression,
    "Silver Key": ItemClassification.useful,
    # Vault Keys
    "Vault Key 149": ItemClassification.progression,
    "Vault Key 233": ItemClassification.progression,
    "Vault Key 304": ItemClassification.progression,
    "Vault Key 370": ItemClassification.progression,
    # Progression Items
    "Allowance Token": ItemClassification.useful,
    "Cursed Effigy": ItemClassification.progression,
    "Sanctum Key 1": ItemClassification.progression,
    "Sanctum Key 2": ItemClassification.progression,
    "Sanctum Key 3": ItemClassification.progression,
    "Sanctum Key 4": ItemClassification.progression,
    "Sanctum Key 5": ItemClassification.progression,
    "Sanctum Key 6": ItemClassification.progression,
    "Sanctum Key 7": ItemClassification.progression,
    "Sanctum Key 8": ItemClassification.progression,
    "Upgrade Disk": ItemClassification.useful,
    # Unique Items
    "Crown of the Blueprints": ItemClassification.progression,
    "Diary Key": ItemClassification.progression,
    "File Cabinet Key": ItemClassification.progression,
    "Lunch Box": ItemClassification.useful,
    "Microchip A": ItemClassification.progression,
    "Microchip B": ItemClassification.progression,
    "Microchip C": ItemClassification.progression,
    "Paper Crown": ItemClassification.progression,
    "Royal Scepter": ItemClassification.progression,
    #
    # Extra "Stuff" Items
    #
    "Extra Coin 1": ItemClassification.filler,
    "Extra Coin 2": ItemClassification.filler,
    "Extra Coin 5": ItemClassification.filler,
    #
    "Extra Gems 1": ItemClassification.filler,
    "Extra Gems 2": ItemClassification.filler,
    #
    "Extra Keys 1": ItemClassification.filler,
    "Extra Keys 2": ItemClassification.filler,
    "Extra Keys 3": ItemClassification.filler,
    #
    "Extra Dice 1": ItemClassification.filler,
    "Extra Dice 2": ItemClassification.filler,
    "Extra Dice 4": ItemClassification.filler,
    #
    "Extra Steps 1": ItemClassification.filler,
    "Extra Steps 2": ItemClassification.filler,
    "Extra Steps 5": ItemClassification.filler,
    #
    "Extra Stars 1": ItemClassification.filler,
    "Extra Stars 2": ItemClassification.filler,
    "Extra Stars 5": ItemClassification.filler,
    #
    "Extra Allowance 1": ItemClassification.filler,
    "Extra Allowance 2": ItemClassification.filler,
    #
    "Extra Fruits Apple": ItemClassification.filler,
    "Extra Fruits Banana": ItemClassification.filler,
    "Extra Fruits Orange": ItemClassification.filler,
    #
    # Traps
    #
    "Trap Freeze Items": ItemClassification.trap,
    "Trap Take Step 1": ItemClassification.trap,
    "Trap Take Step 2": ItemClassification.trap,
    "Trap Take Step 5": ItemClassification.trap,
    "Trap Lose Item": ItemClassification.trap,
    "Trap Lose Star 1": ItemClassification.trap,
    "Trap Lose Star 2": ItemClassification.trap,
    "Trap Lose Star 5": ItemClassification.trap,
    "Trap End Day": ItemClassification.trap,
    #
    # Trash Item from digging. Client may interpret this freely as any of the "trash" items
    #
    "Dug Up Nothing": ItemClassification.filler,
} | {k: v["item_classification"] for k, v in rooms.items()}


class BluePrinceItem(Item):
    game = "Blue Prince"


def get_random_filler_item_name(world: BluePrinceWorld) -> str:

    if world.random.randint(0, 99) < world.options.trap_percentage:

        choice = world.random.choices(
            list(world.options.trap_type_distribution.valid_keys),
            list(world.options.trap_type_distribution.value.values()),
        )[0]

        count = world.random.randint(0, 99)

        match choice:
            case "step_traps_1":
                return "Trap Take Step 1"
            case "step_traps_2":
                return "Trap Take Step 2"
            case "step_traps_5":
                return "Trap Take Step 5"
            case "star_traps_1":
                return "Trap Lose Star 1"
            case "star_traps_2":
                return "Trap Lose Star 2"
            case "star_traps_5":
                return "Trap Lose Star 5"
            case "freeze_traps":
                return "Trap Freeze Items"
            case "eod_traps":
                return "Trap End Day"
            case "item_traps":
                if count < 20:
                    return "Trap Take Step 5"
                elif count < 60:
                    return "Trap Take Step 2"
                else:
                    return "Trap Take Step 1"
            case "star_traps":
                if count < 20:
                    return "Trap Take Star 5"
                elif count < 60:
                    return "Trap Take Star 2"
                else:
                    return "Trap Take Star 1"
    else:
        choice = world.random.choices(
            list(world.options.filler_item_distribution.valid_keys),
            list(world.options.filler_item_distribution.value.values()),
        )[0]

        count = world.random.randint(0, 99)

        match choice:
            case "extra_allowance_1":
                return "Extra Allowance 1"
            case "extra_allowance_2":
                return "Extra Allowance 2"
            case "extra_coins_1":
                return "Extra Coin 1"
            case "extra_coins_2":
                return "Extra Coin 2"
            case "extra_coins_5":
                return "Extra Coin 5"
            case "extra_keys_1":
                return "Extra Keys 1"
            case "extra_keys_2":
                return "Extra Keys 2"
            case "extra_keys_3":
                return "Extra Keys 3"
            case "extra_gems_1":
                return "Extra Gems 1"
            case "extra_gems_2":
                return "Extra Gems 2"
            case "extra_steps_1":
                return "Extra Steps 1"
            case "extra_steps_2":
                return "Extra Steps 2"
            case "extra_steps_5":
                return "Extra Steps 5"
            case "extra_dice_1":
                return "Extra Dice 1"
            case "extra_dice_2":
                return "Extra Dice 2"
            case "extra_dice_4":
                return "Extra Dice 4"
            case "extra_stars_1":
                return "Extra Stars 1"
            case "extra_stars_2":
                return "Extra Stars 2"
            case "extra_stars_5":
                return "Extra Stars 5"
            case "extra_fruit_apple":
                return "Extra Fruits Apple"
            case "extra_fruit_banana":
                return "Extra Fruits Banana"
            case "extra_fruit_orange":
                return "Extra Fruits Orange"
            case "nothing":
                return "Dug Up Nothing"

            case "extra_allowance":

                if count < 20:
                    return "Extra Allowance 2"
                else:
                    return "Extra Allowance 1"

            case "extra_coins":

                if count < 20:
                    return "Extra Coin 5"
                elif count < 60:
                    return "Extra Coin 2"
                else:
                    return "Extra Coin 1"

            case "extra_keys":

                if count < 10:
                    return "Extra Keys 3"
                elif count < 30:
                    return "Extra Keys 2"
                else:
                    return "Extra Keys 1"

            case "extra_gems":
                if count < 30:
                    return "Extra Gems 2"
                else:
                    return "Extra Gems 1"

            case "extra_steps":

                if count < 20:
                    return "Extra Steps 5"
                elif count < 60:
                    return "Extra Steps 2"
                else:
                    return "Extra Steps 1"

            case "extra_dice":

                if count < 10:
                    return "Extra Dice 4"
                elif count < 40:
                    return "Extra Dice 2"
                else:
                    return "Extra Dice 1"

            case "extra_stars":

                if count < 20:
                    return "Extra Stars 5"
                elif count < 60:
                    return "Extra Stars 2"
                else:
                    return "Extra Stars 1"

            case "extra_fruit":
                if count < 20:
                    return "Extra Fruit Orange"
                elif count < 50:
                    return "Extra Fruit Banana"
                else:
                    return "Extra Fruit Apple"

    return "Dug Up Nothing"


def create_item_with_correct_classification(
    world: BluePrinceWorld, name: str
) -> BluePrinceItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return BluePrinceItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# Create the items For the world
def create_all_items(world: BluePrinceWorld) -> None:

    # TODO Implement this list
    # Items that always exist.
    itempool: list[Item] = [
        world.create_item("Key"),
        world.create_item("Sword"),
        world.create_item("Shield"),
        world.create_item("Health Upgrade"),
        world.create_item("Health Upgrade"),
    ]

    # TODO Implement these items.
    # Create Items Based On Options
    # if world.options.hammer:
    #     itempool.append(world.create_item("Hammer"))

    #
    # Add Filler Stuff
    #

    # Get Number of Existing Items.
    number_of_items = len(itempool)

    # Get number of unfilled locations.
    number_of_unfilled_locations = len(
        world.multiworld.get_unfilled_locations(world.player)
    )

    # Determine Number Of Filler Items To Create
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Append Filler Items To Item Pool
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # Add Itempool to world itempool
    world.multiworld.itempool += itempool
