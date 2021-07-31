
from data.entrances import *

# TODO: Maybe make a separate list of entrances and exits that have no requirements when you start with a sword. (e.g. Cliff Plateau Isles Floating Plants Cave.) Probably not necessary though.

def randomize_entrances(self):
  if self.options.get("randomize_entrances") == "Dungeons":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_caves=False)
  elif self.options.get("randomize_entrances") == "Secret Caves":
    randomize_one_set_of_entrances(self, include_dungeons=False, include_caves=True)
  elif self.options.get("randomize_entrances") == "Dungeons & Secret Caves (Separately)":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_caves=False)
    randomize_one_set_of_entrances(self, include_dungeons=False, include_caves=True)
  elif self.options.get("randomize_entrances") == "Dungeons & Secret Caves (Together)":
    randomize_one_set_of_entrances(self, include_dungeons=True, include_caves=True)
  else:
    raise Exception("Invalid entrance randomizer option: %s" % self.options.get("randomize_entrances"))

def randomize_one_set_of_entrances(self, include_dungeons=False, include_caves=False):
  relevant_entrances = []
  remaining_exits = []
  if include_dungeons:
    relevant_entrances += DUNGEON_ENTRANCES
    remaining_exits += DUNGEON_EXITS
  if include_caves:
    relevant_entrances += SECRET_CAVE_ENTRANCES
    remaining_exits += SECRET_CAVE_EXITS

  doing_progress_entrances_for_dungeons_and_caves_only_start = False
  if self.dungeons_and_caves_only_start:
    if include_dungeons and self.options.get("progression_dungeons"):
      doing_progress_entrances_for_dungeons_and_caves_only_start = True
    if include_caves and (self.options.get("progression_puzzle_secret_caves") \
        or self.options.get("progression_combat_secret_caves") \
        or self.options.get("progression_mixed_secret_caves")):
      doing_progress_entrances_for_dungeons_and_caves_only_start = True

  if self.options.get("race_mode"):
    # Move entrances that are on islands with multiple entrances to the start of the list.
    # This is because we need to prevent these islands from having multiple dungeons on them in Race Mode, and this can fail if they're not at the start of the list because it's possible for the only possibility left to be to put multiple dungeons on one island.
    entrances_not_on_unique_islands = []
    for zone_entrance in relevant_entrances:
      for other_zone_entrance in relevant_entrances:
        if other_zone_entrance.island_name == zone_entrance.island_name and other_zone_entrance != zone_entrance:
          entrances_not_on_unique_islands.append(zone_entrance)
          break
    for zone_entrance in entrances_not_on_unique_islands:
      relevant_entrances.remove(zone_entrance)
    relevant_entrances = entrances_not_on_unique_islands + relevant_entrances

  if doing_progress_entrances_for_dungeons_and_caves_only_start:
    # If the player can't access any locations at the start besides dungeon/cave entrances, we choose an entrance with no requirements that will be the first place the player goes.
    # We will make this entrance lead to a dungeon/cave with no requirements so the player can actually get an item at the start.

    entrance_names_with_no_requirements = []
    if self.options.get("progression_dungeons"):
      entrance_names_with_no_requirements += DUNGEON_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_puzzle_secret_caves") \
        or self.options.get("progression_combat_secret_caves") \
        or self.options.get("progression_mixed_secret_caves"):
      entrance_names_with_no_requirements += SECRET_CAVE_ENTRANCE_NAMES_WITH_NO_REQUIREMENTS

    exit_names_with_no_requirements = []
    if self.options.get("progression_dungeons"):
      exit_names_with_no_requirements += DUNGEON_EXIT_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_puzzle_secret_caves"):
      exit_names_with_no_requirements += PUZZLE_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_mixed_secret_caves"):
      exit_names_with_no_requirements += MIXED_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS
    if self.options.get("progression_combat_secret_caves"):
      exit_names_with_no_requirements += COMBAT_SECRET_CAVE_EXIT_NAMES_WITH_NO_REQUIREMENTS
    # No need to check progression_savage_labyrinth, since neither of the items inside Savage have no requirements.

    possible_safety_entrances = [
      e for e in relevant_entrances
      if e.entrance_name in entrance_names_with_no_requirements
    ]
    safety_entrance = self.rng.choice(possible_safety_entrances)

    # In order to avoid using up all dungeons/caves with no requirements, we have to do this entrance first, so move it to the start of the array.
    relevant_entrances.remove(safety_entrance)
    relevant_entrances.insert(0, safety_entrance)

  done_entrances_to_exits = {}
  for zone_entrance in relevant_entrances:
    if doing_progress_entrances_for_dungeons_and_caves_only_start and zone_entrance == safety_entrance:
      possible_remaining_exits = [e for e in remaining_exits if e.unique_name in exit_names_with_no_requirements]
    else:
      possible_remaining_exits = remaining_exits

    # The below is debugging code for testing the caves with timers.
    #if zone_entrance.entrance_name == "Crater on Fire Mountain":
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name == "Ice Ring Isle Secret Cave"
    #  ]
    #elif zone_entrance.entrance_name == "Palsa on Ice Ring Isle":
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name == "Fire Mountain Secret Cave"
    #  ]
    #else:
    #  possible_remaining_exits = [
    #    x for x in remaining_exits
    #    if x.unique_name not in ["Fire Mountain Secret Cave", "Ice Ring Isle Secret Cave"]
    #  ]

    if self.options.get("race_mode") != "Default" and self.race_mode_quest_marker_mode == "With Entrances":
      # Prevent two entrances on the same island both leading into dungeons (DRC and Pawprint each have two entrances).
      # This is because Race Mode's dungeon markers only tell you what island required dungeons are on, not which of the two entrances it's in. So if a required dungeon and a non-required dungeon were on the same island there would be no way to tell which is required.
      done_entrances_on_same_island_leading_to_a_dungeon = [
        entr for entr in done_entrances_to_exits
        if entr.island_name == zone_entrance.island_name
        and done_entrances_to_exits[entr] in DUNGEON_EXITS
      ]
      if done_entrances_on_same_island_leading_to_a_dungeon:
        possible_remaining_exits = [x for x in possible_remaining_exits if x not in DUNGEON_EXITS]

    zone_exit = self.rng.choice(possible_remaining_exits)
    remaining_exits.remove(zone_exit)

    self.entrance_connections[zone_entrance.entrance_name] = zone_exit.unique_name
    self.dungeon_and_cave_island_locations[zone_exit.zone_name] = zone_entrance.island_name
    done_entrances_to_exits[zone_entrance] = zone_exit

    if not self.dry_run:
      # Update the stage this entrance takes you into.
      if not zone_exit.unique_name.endswith("Submarine"):
        entrance_dzr_path = "files/res/Stage/%s/Room%d.arc" % (zone_entrance.stage_name, zone_entrance.room_num)
        entrance_dzr = self.get_arc(entrance_dzr_path).get_file("room.dzr")
        print(entrance_dzr.entries_by_type("SCLS"),zone_entrance.stage_name,zone_entrance.room_num,zone_entrance.scls_exit_index)
        entrance_scls = entrance_dzr.entries_by_type("SCLS")[zone_entrance.scls_exit_index]
        entrance_scls.dest_stage_name = zone_exit.stage_name
        entrance_scls.room_index = zone_exit.room_num
        entrance_scls.spawn_id = zone_exit.spawn_id
        entrance_scls.save_changes()

      # Update the DRI spawn to not have spawn type 5.
      # If the DRI entrance was connected to the TotG dungeon, then exiting TotG while riding KoRL would crash the game.
      entrance_spawns = entrance_dzr.entries_by_type("PLYR")
      for spawn in entrance_spawns:
        if spawn.spawn_id == zone_entrance.spawn_id:
          entrance_spawn = spawn
          break
      if entrance_spawn.spawn_type == 5:
        entrance_spawn.spawn_type = 1
        entrance_spawn.save_changes()

      # Update the entrance you're put at when leaving the dungeon.
      if zone_exit.unique_name.endswith("Submarine"):
        exit_dzr_path = "files/res/Stage/%s/Stage.arc" % (zone_exit.stage_name)
        exit_dzr = self.get_arc(exit_dzr_path).get_file("stage.dzs")
      else:
        exit_dzr_path = "files/res/Stage/%s/Room%d.arc" % (zone_exit.stage_name, zone_exit.room_num)
        exit_dzr = self.get_arc(exit_dzr_path).get_file("room.dzr")
      exit_scls = exit_dzr.entries_by_type("SCLS")[zone_exit.scls_exit_index]
      exit_scls.dest_stage_name = zone_entrance.stage_name
      exit_scls.room_index = zone_entrance.room_num
      exit_scls.spawn_id = zone_entrance.spawn_id
      exit_scls.save_changes()

      # Also update the extra exits when leaving Savage Labyrinth to put you on the correct entrance when leaving.
      if zone_exit.unique_name == "Savage Labyrinth":
        for stage_and_room_name in ["Cave10/Room0", "Cave10/Room20", "Cave11/Room0"]:
          savage_dzr_path = "files/res/Stage/%s.arc" % stage_and_room_name
          savage_dzr = self.get_arc(savage_dzr_path).get_file("room.dzr")
          exit_sclses = [x for x in savage_dzr.entries_by_type("SCLS") if x.dest_stage_name == "sea"]
          for exit_scls in exit_sclses:
            exit_scls.dest_stage_name = zone_entrance.stage_name
            exit_scls.room_index = zone_entrance.room_num
            exit_scls.spawn_id = zone_entrance.spawn_id
            exit_scls.save_changes()

      if zone_exit in SECRET_CAVE_EXITS and not zone_exit.unique_name.endswith("Submarine"):
        # Update the sector coordinates in the 2DMA chunk so that save-and-quitting in a secret cave puts you on the correct island.
        exit_dzs_path = "files/res/Stage/%s/Stage.arc" % zone_exit.stage_name
        exit_dzs = self.get_arc(exit_dzs_path).get_file("stage.dzs")
        _2dma = exit_dzs.entries_by_type("2DMA")[0]
        island_number = self.island_name_to_number[zone_entrance.island_name]
        sector_x = (island_number-1) % 7
        sector_y = (island_number-1) // 7
        _2dma.sector_x = sector_x-3
        _2dma.sector_y = sector_y-3
        _2dma.save_changes()

      if zone_exit.unique_name == "Fire Mountain Secret Cave":
        actors = exit_dzr.entries_by_type("ACTR")
        for actor in actors:
          if actor.name == "VolTag":
            kill_trigger = actor
            break
        if zone_entrance.entrance_name == "Crater on Fire Mountain":
          # Unchanged from vanilla, do nothing.
          pass
        elif zone_entrance.entrance_name == "Palsa on Ice Ring Isle":
          # Ice Ring's entrance leads to Fire Mountain's exit.
          # Change the kill trigger on the inside of Fire Mountain to act like the one inside Ice Ring.
          kill_trigger.type = 2
          kill_trigger.save_changes()
        else:
          # An entrance without a timer leads into this cave.
          # Remove the kill trigger actor on the inside, because otherwise it would throw the player out the instant they enter.
          exit_dzr.remove_entity(kill_trigger, "ACTR")

      if zone_exit.unique_name == "Ice Ring Isle Secret Cave":
        actors = exit_dzr.entries_by_type("ACTR")
        for actor in actors:
          if actor.name == "VolTag":
            kill_trigger = actor
            break
        if zone_entrance.entrance_name == "Palsa on Ice Ring Isle":
          # Unchanged from vanilla, do nothing.
          pass
        elif zone_entrance.entrance_name == "Crater on Fire Mountain":
          # Fire Mountain's entrance leads to Ice Ring's exit.
          # Change the kill trigger on the inside of Ice Ring to act like the one inside Fire Mountain.
          kill_trigger.type = 1
          kill_trigger.save_changes()
        else:
          # An entrance without a timer leads into this cave.
          # Remove the kill trigger actor on the inside, because otherwise it would throw the player out the instant they enter.
          exit_dzr.remove_entity(kill_trigger, "ACTR")

      if zone_exit.unique_name == "Ice Ring Isle Secret Cave":
        # Also update the inner cave of Ice Ring Isle to take you out to the correct entrance as well.
        inner_cave_dzr_path = "files/res/Stage/ITest62/Room0.arc"
        inner_cave_dzr = self.get_arc(inner_cave_dzr_path).get_file("room.dzr")
        inner_cave_exit_scls = inner_cave_dzr.entries_by_type("SCLS")[0]
        inner_cave_exit_scls.dest_stage_name = zone_entrance.stage_name
        inner_cave_exit_scls.room_index = zone_entrance.room_num
        inner_cave_exit_scls.spawn_id = zone_entrance.spawn_id
        inner_cave_exit_scls.save_changes()

        # Also update the sector coordinates in the 2DMA chunk of the inner cave of Ice Ring Isle so save-and-quitting works properly there.
        inner_cave_dzs_path = "files/res/Stage/ITest62/Stage.arc"
        inner_cave_dzs = self.get_arc(inner_cave_dzs_path).get_file("stage.dzs")
        inner_cave_2dma = inner_cave_dzs.entries_by_type("2DMA")[0]
        inner_cave_2dma.sector_x = sector_x-3
        inner_cave_2dma.sector_y = sector_y-3
        inner_cave_2dma.save_changes()

      if zone_exit.boss_stage_name is not None:
        # Update the wind warp out event to take you to the correct island.
        boss_stage_arc_path = "files/res/Stage/%s/Stage.arc" % zone_exit.boss_stage_name
        event_list = self.get_arc(boss_stage_arc_path).get_file("event_list.dat")
        warp_out_event = event_list.events_by_name["WARP_WIND_AFTER"]
        for actor in warp_out_event.actors:
          if actor.name == "DIRECTOR":
            director = actor
            break
        for action in director.actions:
          if action.name == "NEXT":
            stage_change_action = action
            break
        stgNProp = False
        romNProp = False
        spnIProp = False
        for prop in stage_change_action.properties:
          if prop.name == "Stage" and not stgNProp:
            stage_name_prop = prop
            stgNProp = True
            continue
          elif prop.name == "RoomNo" and not romNProp:
            room_num_prop = prop
            romNProp = True
            continue
          elif prop.name == "StartCode" and not spnIProp:
            spawn_id_prop = prop
            spnIProp = True
            continue
        stage_name_prop.value = zone_entrance.warp_out_stage_name
        room_num_prop.value = zone_entrance.warp_out_room_num
        spawn_id_prop.value = zone_entrance.warp_out_spawn_id

  self.logic.update_entrance_connection_macros()
