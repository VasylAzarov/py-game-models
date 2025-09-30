import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild

def main() -> None:

    with open("players.json", "r", encoding="utf-8") as file:
        data_from_file = json.load(file)

    for player_name, values in data_from_file.items():
        email = values["email"]
        bio = values["bio"]

        race_info = values["race"]
        race, _ = Race.objects.get_or_create(
            name=race_info["name"],
            defaults={"description": race_info["description"]}
        )

        for skill_info in race_info["skills"]:
            Skill.objects.get_or_create(
                name=skill_info["name"],
                race=race,
                defaults={"bonus": skill_info["bonus"]}
            )

        guild_info = values.get("guild")
        guild_obj = None
        if guild_info:
            guild_obj, _ = Guild.objects.get_or_create(
                name=guild_info["name"],
                defaults={"description": guild_info.get("description")}
            )

        Player.objects.create(
            nickname=player_name,
            email=email,
            bio=bio,
            race=race,
            guild=guild_obj
        )


if __name__ == "__main__":
    main()
