from dataclasses import dataclass
from typing import Optional


@dataclass
class Episode:
    """Model representing an anime episode."""
    
    number: int
    title: str
    url: str
    season: Optional[int] = None
    date: Optional[str] = None
    image_url: Optional[str] = None
    
    def __str__(self) -> str:
        if self.season:
            return f"Episódio {self.number} (S{self.season})"
        return f"Episódio {self.number}"
