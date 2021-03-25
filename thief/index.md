_[Home](../)_

# Thief

## Table of Contents
* [Alchemy](./alchemy.md)
* [Dexterity](./dexterity.md)
* [Light Armor](./lightarmor.md)
* [Sneak](./sneak.md)
* [Speechcraft](./speechcraft.md)
* [Wayfarer](./wayfarer.md)

## Overview

The following changes, additions and tweaks have been made to both make thief gameplay more interesting
and less of a gamebreaker.


* "Prodigy" perks: Mutually exclusive - only one may be chosen per character. Instantly
	gives access to two mid to high level perks. Not selectable if any of the perks it
	grants have already been selected.

* Shouting grants speechcraft experience
	
* Spell sneak with initial damage multiplier 0 (but sneak skill scaling applies)

* Gold weight : 0.01
* Lockpick weight: 0.5

* Sneak damage scaling
  * `+ 0.5% * SNEAK_SKILL` (heavy weaponry, ranged weaponry)
  * `+ 0.75% * SNEAK_SKILL` (light weaponry without dagger,tanto)
  * `+ 1% * SNEAK_SKILL` (dagger,tanto, spell)

* Shout scaling with speechcaft skill
  * `+ 0.5% magnitude * SPEECHCRAFT_SKILL`
  * `+ 0.5% duration * SPEECHCRAFT_SKILL`

* Sneak multiplier modified on target with specific armor pieces equipped:
   |       | Helmet  | Cuirass |
   |:------|:--------|:--------|
   | Light | `-0.15` | `-0.15` |
   | Heavy | `-0.3`  | `-0.3`  |

* Sneak attacks on undead 40% less effective than on living targets

-----

Replaced enchantments and alchemy effects, to accomodate for the addition of Wayfarer:


* Fortify Lockpicking -> Defender (Light Weaponry damage/ Block efficiency)
* Fortify Pickpocket -> Fortify Dexterity (picking locks/pockets is easier)

* Edits (renames) all armor pieces that carry those enchantments
* Edits (renames) all potions that carry those effects

* Ravage Health: Deals hefty damage after a short warm-up time
* Damage Magicka Regen: Removes all Magicka for a set duration, then gives it back once poison wears off.
* Damage Stamina Regen: Removes all Stamina for a set duration, then gives it back once poison wears off.
* Ravage Magicka -> Flare Undead: Against undead: Sun damage + consecutive hits lower confidence + counts as "Chastise" (to be used by Mage module spells)
* Ravage Stamina -> Corrode Armor: Deals damage and reduces armor depending on the target's armor value.

* Replaced crafting fortification effects on ingredients and potions:

* Fortify Smithing -> Weaponmaster (Heavy Weaponry damage/ Ranged Weaponry damage)
* Fortify Enchanting -> Brawler (Unarmed/ Fist weapon damage)

* Edits (renames) all potions that carry those effects

* Edited vanilla perks:
  * Bribery
  * Light Foot
