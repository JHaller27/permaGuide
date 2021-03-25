_[Go to Restoration Perks](../restoration.md)_

Spells [Restoration]
============--------

Notes on archetypes
--------------------

- Aura: 		Toggleable area-of-effect buffs. While active, Health and Stamina are reduced by 10/20/30/40/50 for Novice/Apprentice/Adept/Expert/Master level auras. Only one aura may be active at any time.
- Curse:		Potent long-range debuffs. When the target dies while affected by a curse, the curse will randomly select a new target within its spread radius (default: 200 units). If the target fulfills a few conditions (not the player, has base actor, not NONE), the curse jumps over and affects the new target. If this check fails, the curse will either try again or stop of the maximum number of attempts (default: 1) is reached. Curses last 60 seconds.
- Plague: 		Medium-range debuffs. Plagues spread from the initial target to adjacent targets, initially affecting one new target every 2.5 seconds. They do not spread from secondary targets. Plagues will not reinfect the initial target. Plagues last 12 seconds.
- Healing:		Spells that restore health to living or undead targets.
- Ward:			Spells that block incoming physical or magical hits.
- Anti-Undead:	Spells that have potent effects on undead targets, but do not initially work on living targets.

Novice
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Chastise		| 30		| Aura. - 200% Health, Stamina and Magicka regeneration for all undead actors within 30 feet range. 
Spell Ward		| 25/s		| Absorbs up to 200 points of spell or shout damage and effects, but instantly breaks and staggers the user when hit with a shout.
Recovery		| 12/s		| Restores 10 points of Health per second.


Apprentice
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Armored Ascension		| 40	| Aura. 10% More melee weapon damage and 50 armor for all friendly actors within 30 feet range.
Curse of Infestation	| 40	| Curse. The target takes 1 poison damage per second for 60 seconds. If it dies while this spell is active, three small spiders spawn from its corpse. Each spider is at 40% of the caster's level.
Cure Poison				| 60	| Terminates any poison effect the caster is affected by, and restores 10 points of Health.
Fast Healing			| 64	| Restores 40 points of Health.	
Healing Hands			| 33/s	| Restores 20 points of Health to the target per second.
Kingsbane				| 45	| Plague. All affected targets have their Stamina regeneration reduced by 400% and lose 10% of their current Stamina every second.
Brainmelt Syndrome		| 45	| Plague. All affected targets consume 75 additional Magicka when casting a spell.
Outbreak				| 26	| Touch-range spell. Only affects targets affected by a plague-type spell. Drains 6 points of health per second for 5 second. If the target spreads a plague (that means it was the original target), it also makes the plague spread 10 times faster. Cannot be dual cast.
Necromantic Healing		| 15	| Restore 15 points of Health per second to target undead creature.
Cleansing				| 40	| Staggers the target. If the target as less than 40% Health left, it dies. If not, it loses 20% of its current Health. Only works on targets affected by "Chastise".
Sun Fire				| 30	| Target undead takes 10 points of sun damage per second for 5 seconds. Counts as "Chastise".


Adept
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Cryomancer's Sight		| 50	| Aura. 4 Frost damage to Health and Stamina per second, -10% frost resistance and -10% movement speed to all hostile actors within 30 feet.
Grand Blaze				| 50	| Aura. 4 Fire damage to Health per second and -10% fire resistance to all hostile actors within 30 feet.
Upcoming Tempest		| 50	| Aura. 4 Shock damage to Health and Magicka per second and -10% shock resistance to all hostile actors within 30 feet.
Curse of Blood Magic	| 60	| Curse. Whenever the target casts a spell, it loses 15% of its current Health.
Cure Disease			| 80	| Curse any disease the caste is affected by, and restores 10 points of Health.
Stream of Life			| 44/s	| Restores 30 points of Health per second.
Heal Other				| 90	| Restores 60 points of Health to the target.
Heal Undead				| 90	| Restores 60 points of Health to target undead creature.
Poison Rune				| 52	| Rune. Deals 3 points of poison damge per second for 30 seconds to all targets. 
Vampire's Bane			| 70	| Deals 10 points of sun damage per second for 6 seconds to all undead creatures within a 15 feet radius of the impact destination. Counts as "Chastise". 
Sun Cloak				| 59	| For 60 seconds, undead within a 10 feet radius take 6 points of sun damage per second. Counts as "Chastise".


Expert
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Soul Consumer	| 60		| Aura. Whenever a hostile actor within 30 feet range dies, its killer recovers 20% of his maximum Health and Magicka.
Thorn's Embrace	| 60		| Aura. All non-hostile actors within 30 feet range gain 50% damage reflection.
Curse of Greed	| 80		| Curse. Once per second, a random actor within 500 units range of the target loses 10% of its current Health, and th target's Health increases by the damage dealt. If the total damage dealt this way exceeds 60% of the target's maximum Health, it instantly dies and detonates. The detonation ragdolls everyone within 30 feet range, but deals no damage.
Repulsive Ward	| 60/s		| Increases armor rating by 150 and absorbs up to 150 points of spell or shout damage and effects. When hit by a melee attack, the attacker is struck to the ground.
Purgatory		| 60		| Staggers the target. If the target is below 40% health, it dies and detonates for 80 non-elemental damage in a 200 unit radius. If not, it loses 25% of its current Health. Only works on targets affected by "Cleansing".
Thornswreath	| 80		| Plague. Every 1.6 seconds, every affected target has a 50% chance to get staggered.


Master
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Curse of Roots	| 90		| Curse. Whenever the target takes a hit, there is a 20% chance it instantly dies and turns into a tree. The body and inventory are destroyed in the process.
Mirror Ward		| 83/s		| Negates up to 5000 points of spell or shout damage and effects. Reflects any spell it is hit with back at the caster.
Resurrection	| 120		| Revives the target and destroys its inventory.
Legionfall		| 129		| Plague. Every affected target takes x damage to Health, Stamina and Magicka per second, where x is the number of affected targets * 5. 


Focus
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Curse of Binding		| 150	| Curse. While the target is alive, this spell's caster does not take damage from weapons or Destruction spells, and the caster's spell casting cost is increased by 50%. Only works on targets that are affected by a Plague-type spell.
Aspect of Brilliance	| 0 	| Aura. +15% Weapon and Destruction spell damage for all friendly actors within 30 feet range. -15% Weapon and Destruction spell damage for all non-friendly actors within 30 feet range.


Special (Quest etc)
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Lesser Ward		| 34		| Increases armor rating by 40 and absorbs up to 40 points of spell damage.


Planned
============--------
Spell name 		|	Cost	|	Decription
------------------------------------------
Great Curse of Infestation (expert?): Drains health while active, spawns single large spider when target dies, spider gets larger when much health was drained.