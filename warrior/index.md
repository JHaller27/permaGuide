_[Home](../)_

# Warrior

## Table of Contents
* [Block](./block.md)
* [Heavy Armor](./heavyarmor.md)
* [Heavy Weaponry](./heavyweaponry.md)
* [Light Weaponry](./lightweaponry.md)
* [Ranged Weaponry](./rangedweaponry.md)
* [Smithing](./smithing.md)

## Overview
General changes and new curiosities:

* "Mastery" perks. Activated abilities. Mutually exclusive - exactly one can be chosen per character.

* Smithing exp from smelter/tanning rack

* Changed arcane blacksmith fail message (since that can't happen in PerMa)

-----

Skyrim combat is very simplistic, even though the whole game seems to revolve around it. The following tweaks have been made to add some depth and tactic. All changes apply to both the player and all NPCs.

* Bash reach reduced (141 -> 100)

* Activate a bear trap to be given the option to collect it. Collecting and simple placing (-> dropping from inventory) do not require any perk investment, but dropping a trap might instantly trigger it.

* Critical hit damage scales with potions and enchantments
* Critical hit damage scales with skill; +0.5% per skill level in the related skill

* Swinging weapons consumes stamina; the amount dpeends on the weapon type
* Not attacking or blocking makes stamina regenerate 75% faster
* Standing still makes stamina regenerate an additional 200% faster

* Base critical hit chance:
    | Type | % Chance |
    |:-----|:---------|
    | Light Weaponry (minus dagger/tanto) | `7%` |
    | Dagger/tanto | `14%` |
    | Heavy Weaponry | `3.5%` |
    | Ranged Weaponry | `5%` |

* Fist weapon damage scales with anything that boosts unarmed damage

* Regular, unblocked attacks start to stagger after 2-4 hits (random)
* In between each stagger on a single enemy, there exists a cooldown depending on the weapon's stagger rank. If stagger is not on cooldown and the initial 2-4 hit protection is gone, weapon hits will always stagger if the cooldown is not running.

* Regular, unblocked attacks apply bleeding damage. The bleeding damage depends on the weapon's bleed rank.

* Regular, unblocked attacks apply a debuff to armor and resistance. The magnitude of the debuff depends on the weapon's debuff rank.

* Moving with worn armor (2 pieces or more) levels armor skill slightly every four seconds; magnitude can be adjusted in the console with set xMAWARArmorPassiveSkillBase to X where x is a floating point number. Default: 0.1

* Dual wielding has 30% damage malus without perk "Dual Wield". Since this perk is player-only, the malus does not apply to enemies.

* Added spell blocking. If you block a hostile spell, your health gets restored by 50% of its first effect's magnitude afterwards, and you take 20% of its base cost as stamina damage. Sanctuary rank 1 and 2 reduce the stamina cost to 15%/10% of the spell's base cost.

> The following effects are only active if both PerMa_Warrior and
> PerMa-Thief are used

* **Movement slowdown** with worn armor
  |       | Head | Body | Arms | Legs | Shield |
  |:------|:-----|:-----|:-----|:-----|:-------|
  | Heavy | `2%` | `6%` | `2%` | `4%` | `2%` |
  | Light | `1%` | `3%` | `1%` | `2%` | `1%` |

* **Attack speed slowdown** with worn armor
  |       | Head | Body | Arms | Legs | Shield |
  |:------|:-----|:-----|:-----|:-----|:-------|
  | Heavy | `1%` | `3%` | `4%` | `0%` | `4%` |
  | Light | `0%` | `2%` | `3%` | `0%` | `3$` |

* **Spell casting cost increase** with worn armor
  |       | Head | Body | Arms | Legs | Shield |
  |:------|:-----|:-----|:-----|:-----|:-------|
  | Heavy | `6%` | `6%` | `2%` | `2%` | `4%` |
  | Light | `3%` | `3%` | `1%` | `1%` | `2$` |


### Edited Vanilla Perks

Two-handed
* Savage Strike
* Critical Charge
* Devastating Blow
* Great Critical Charge

Blocking
* Power Bash
* Shield Charge

Archery
* Eagle Eye

Smithing
* Smithing (hidden perk DLC2Smithing)
* Elven Smithing
* Advanced Armor
* Glass Smithing
* Dragon Armor
* Steel Smithing
* Dwarven Smithing
* Orcish Smithing
* Ebony Smithing
* Daedric Smithing
