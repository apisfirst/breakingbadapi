#!/usr/bin/env python

from typing import List
from pydantic import BaseModel


class Episode(BaseModel):
    title: str
    episode_number: int
