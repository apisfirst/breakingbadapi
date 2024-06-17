import json
from models import Episode
from fastapi import APIRouter, HTTPException
from typing import Dict, List

router = APIRouter()

with open("./data/episodes.json", "r") as file:
    episodes_data = json.load(file)


@router.get("/", response_model=List[Episode])
async def get_all_episodes():
    """
    Get all Breaking Bad episodes.
    :return:
    """
    all_episodes = []
    seasons = episodes_data.get("seasons")

    for season in seasons:
        for episode in season.get("episodes"):
            all_episodes.append(episode)
    return all_episodes


@router.get("/{season_number}")
async def get_episode_by_season(season_number: int) -> Dict:
    """
    Get Breaking Bad episodes by season number
    :param season_number:
    :return:
    """
    season_episodes = next(
        (
            season
            for season in episodes_data["seasons"]
            if season["season_number"] == season_number
        ),
        None,
    )

    if season_episodes:
        return season_episodes
    else:
        raise HTTPException(status_code=404, detail=f"Season {season_number} not found")
