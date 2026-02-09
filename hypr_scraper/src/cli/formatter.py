from typing import List
from src.models.anime import Anime


class OutputFormatter:
    """Formatter for displaying anime search results."""
    
    @staticmethod
    def format_console(animes: List[Anime], query: str) -> str:
        """
        Format anime results for console output.
        
        Args:
            animes: List of anime objects
            query: Original search query
            
        Returns:
            Formatted string for console display
        """
        if not animes:
            return f"No results found for: {query}"
        
        output = [f"\n🔍 Search results for: {query}"]
        output.append(f"📊 Found {len(animes)} results\n")
        
        for i, anime in enumerate(animes, 1):
            output.append(f"{i}. {anime.title}")
            
            if anime.year:
                output.append(f"   📅 Year: {anime.year}")
            
            if anime.rating:
                output.append(f"   ⭐ Rating: {anime.rating}")
            
            if anime.type:
                output.append(f"   🎬 Type: {anime.type}")
            
            if anime.description:
                output.append(f"   📝 {anime.description}")
            
            output.append(f"   🔗 {anime.url}")
            output.append("")
        
        return "\n".join(output)
    
    @staticmethod
    def format_simple(animes: List[Anime]) -> str:
        """
        Format anime results in simple list format.
        
        Args:
            animes: List of anime objects
            
        Returns:
            Simple formatted string with just titles
        """
        if not animes:
            return "No results found"
        
        titles = [f"{i + 1}. {anime.title}" for i, anime in enumerate(animes)]
        return "\n".join(titles)
