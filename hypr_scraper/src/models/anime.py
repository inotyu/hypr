from dataclasses import dataclass
from typing import Optional


@dataclass
class Anime:
    """Model representing an anime result from scraping."""
    
    title: str
    url: str
    description: Optional[str] = None
    year: Optional[int] = None
    rating: Optional[float] = None
    type: Optional[str] = None
    
    def __str__(self) -> str:
        return f"{self.title} ({self.year}) - {self.rating}"
    
    def to_dict(self) -> dict:
        """Convert anime to dictionary representation."""
        return {
            'title': self.title,
            'url': self.url,
            'description': self.description,
            'year': self.year,
            'rating': self.rating,
            'type': self.type
        }
