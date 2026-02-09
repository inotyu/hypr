"""Interactive mode for anime selection and episode viewing."""

import sys
from typing import List, Optional

# Importações com fallback para evitar problemas de path
try:
    from src.scraper.hypr_scraper import HyprScraper
    from src.models.anime import Anime
    from src.models.episode import Episode
    from src.utils.exceptions import HyprScraperError
    from src.cli.selector import KeyboardSelector
except ImportError:
    from hypr_scraper.src.scraper.hypr_scraper import HyprScraper
    from hypr_scraper.src.models.anime import Anime
    from hypr_scraper.src.models.episode import Episode
    from hypr_scraper.src.utils.exceptions import HyprScraperError
    from hypr_scraper.src.cli.selector import KeyboardSelector


class InteractiveMode:
    """Interactive mode for anime selection."""
    
    def __init__(self):
        self.scraper = HyprScraper()
        self.selector = KeyboardSelector()
    
    def run(self, query: Optional[str] = None) -> int:
        """Run interactive mode."""
        try:
            with self.scraper:
                if query:
                    print("🔍 Procurando resultados, aguarde...")
                    anime_results = self.scraper.search_anime(query)
                else:
                    query = input("🔍 Buscar anime: ").strip()
                    print("🔍 Procurando resultados, aguarde...")
                    anime_results = self.scraper.search_anime(query)
                
                # Convert to Anime objects
                animes = []
                for result in anime_results:
                    anime = Anime(
                        title=result['title'],
                        url=result['url'],
                        description=""  # Not available from search
                    )
                    animes.append(anime)
                
                if not animes:
                    print(f"❌ Nenhum resultado encontrado para: {query}")
                    return 0
                
                # Show anime selection with keyboard
                selected_anime = self.selector.select_anime(animes)
                if not selected_anime:
                    print("👋 Cancelado.")
                    return 0
                
                print(f"📺 Iniciando {selected_anime.title}, aguarde...")
                
                # Get and show episodes
                episode_results = self.scraper.get_episodes(selected_anime.url)
                
                # Convert to Episode objects
                episodes = []
                for result in episode_results:
                    episode = Episode(
                        number=result['episode'],
                        title=result['title'],
                        url=result['url']
                    )
                    episodes.append(episode)
                
                if not episodes:
                    print(f"❌ Nenhum episódio encontrado para: {selected_anime.title}")
                    return 0
                
                # Show episodes with keyboard navigation
                self.selector.show_episodes(episodes, selected_anime.title)
                return 0
            
        except HyprScraperError as e:
            print(f"❌ Erro: {e}")
            return 1
        except KeyboardInterrupt:
            print("\n👋 Cancelado pelo usuário.")
            return 0
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return 1
