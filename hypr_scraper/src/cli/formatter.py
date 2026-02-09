from typing import List

# Importações com fallback para evitar problemas de path
try:
    from src.models.anime import Anime
except ImportError:
    from hypr_scraper.src.models.anime import Anime


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
            # Tratar tanto objetos Anime quanto dicionários
            if hasattr(anime, 'title'):
                title = anime.title
                year = anime.year if hasattr(anime, 'year') else None
                rating = anime.rating if hasattr(anime, 'rating') else None
                anime_type = anime.type if hasattr(anime, 'type') else None
                description = anime.description if hasattr(anime, 'description') else None
            else:
                title = anime.get('title', 'Sem título')
                year = anime.get('year')
                rating = anime.get('rating')
                anime_type = anime.get('type')
                description = anime.get('description')
            
            output.append(f"{i}. {title}")
            
            if year:
                output.append(f"   📅 Year: {year}")
            
            if rating:
                output.append(f"   ⭐ Rating: {rating}")
            
            if anime_type:
                output.append(f"   🎬 Type: {anime_type}")
            
            if description:
                output.append(f"   📝 {description}")
            
            output.append(f"   🔗 {anime.url if hasattr(anime, 'url') else anime.get('url', '')}")
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
        
        titles = []
        for i, anime in enumerate(animes):
            if hasattr(anime, 'title'):
                title = anime.title
            else:
                title = anime.get('title', 'Sem título')
            titles.append(f"{i + 1}. {title}")
        return "\n".join(titles)
