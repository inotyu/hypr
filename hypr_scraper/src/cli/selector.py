"""Interactive keyboard selector for anime."""

import sys
import curses
from typing import List, Optional
from src.models.anime import Anime
from src.models.episode import Episode


class KeyboardSelector:
    """Interactive keyboard selector using curses."""
    
    def __init__(self):
        self.screen = None
    
    def select_anime(self, animes: List[Anime]) -> Optional[Anime]:
        """Select anime using keyboard navigation."""
        try:
            self.screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.screen.keypad(True)
            curses.curs_set(0)
            
            current_selection = 0
            
            while True:
                self._display_animes(animes, current_selection)
                
                key = self.screen.getch()
                
                if key == curses.KEY_UP or key == ord('w') or key == ord('W'):
                    current_selection = max(0, current_selection - 1)
                elif key == curses.KEY_DOWN or key == ord('s') or key == ord('S'):
                    current_selection = min(len(animes) - 1, current_selection + 1)
                elif key == ord('\n') or key == ord('\r'):  # Enter
                    return animes[current_selection]
                elif key == ord('q') or key == ord('Q') or key == 27:  # q or ESC
                    return None
                    
        finally:
            if self.screen:
                curses.endwin()
    
    def _display_animes(self, animes: List[Anime], selection: int):
        """Display anime list with selection."""
        self.screen.clear()
        
        # Get screen dimensions
        height, width = self.screen.getmaxyx()
        
        # Title
        title = "🎬 Selecione um anime (W/S ou ↑/↓ para navegar, ENTER para escolher, Q para sair):"
        if len(title) < width:
            self.screen.addstr(0, 0, title)
        else:
            self.screen.addstr(0, 0, title[:width-1])
        
        # Separator
        separator = "=" * min(width, 70)
        self.screen.addstr(1, 0, separator)
        
        start_row = 3
        max_display = min(len(animes), height - 10)  # Leave space for UI
        
        # Calculate start index for scrolling
        start_index = max(0, min(selection - max_display // 2, len(animes) - max_display))
        
        for i in range(max_display):
            anime_idx = start_index + i
            if anime_idx >= len(animes):
                break
                
            anime = animes[anime_idx]
            year_str = f" ({anime.year})" if anime.year else ""
            
            if anime_idx == selection:
                prefix = "▶ "
                attr = curses.A_REVERSE
            else:
                prefix = "  "
                attr = curses.A_NORMAL
            
            line = f"{prefix}{anime_idx + 1:2d}. {anime.title}{year_str}"
            # Truncate to fit screen width
            if len(line) > width - 1:
                line = line[:width-2] + "..."
            
            try:
                self.screen.addstr(start_row + i, 0, line, attr)
            except curses.error:
                # Skip if position is invalid
                continue
        
        if len(animes) > max_display:
            more_text = f"Mostrando {start_index + 1}-{min(start_index + max_display, len(animes))} de {len(animes)} animes"
            if len(more_text) < width:
                self.screen.addstr(start_row + max_display, 0, more_text)
        
        # Selection info
        selected_text = f"Selecionado: {animes[selection].title}"
        if len(selected_text) < width:
            self.screen.addstr(start_row + max_display + 2, 0, selected_text)
        
        self.screen.refresh()
    
    def show_episodes(self, episodes: List[Episode], anime_title: str):
        """Display episodes list with video URL extraction."""
        try:
            self.screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.screen.keypad(True)
            curses.curs_set(0)
            
            current_row = 0
            video_url = None
            loading = False
            
            while True:
                self._display_episodes(episodes, anime_title, current_row, video_url, loading)
                
                key = self.screen.getch()
                
                if key == curses.KEY_UP or key == ord('w') or key == ord('W'):
                    current_row = max(0, current_row - 1)
                    video_url = None  # Reset when changing selection
                elif key == curses.KEY_DOWN or key == ord('s') or key == ord('S'):
                    current_row = min(len(episodes) - 1, current_row + 1)
                    video_url = None  # Reset when changing selection
                elif key == ord('\n') or key == ord('\r'):  # Enter - play video
                    if not loading:
                        loading = True
                        video_url = "🎬 Preparando vídeo, aguarde..."
                        self._display_episodes(episodes, anime_title, current_row, video_url, loading)
                        
                        # Sair do curses temporariamente para executar o player
                        curses.endwin()
                        self.screen = None
                        
                        try:
                            from src.scraper.hypr_scraper import HyprScraper
                            with HyprScraper() as scraper:
                                video_url = scraper.get_video_url(episodes[current_row].url)
                                
                                if video_url:
                                    print(f"🎬 Reproduzindo: {episodes[current_row].title}")
                                    
                                    # Detectar sistema operacional e abrir player
                                    system = platform.system().lower()
                                    
                                    # Windows: precisa ter mpv instalado (scoop install mpv ou winget install mpv)
                                    if system == "linux":
                                        # Linux: tentar mpv primeiro, depois browser
                                        players = [
                                            ["mpv", video_url],
                                            ["xdg-open", video_url]
                                        ]
                                    elif system == "windows":
                                        # Windows: tentar mpv primeiro, depois browser padrão
                                        players = [
                                            ["mpv.exe", video_url],
                                            ["cmd", "/c", "start", video_url]
                                        ]
                                    elif system == "darwin":  # macOS
                                        # macOS: tentar mpv primeiro, depois browser
                                        players = [
                                            ["mpv", video_url],
                                            ["open", video_url]
                                        ]
                                    else:
                                        # Fallback genérico
                                        players = [["xdg-open", video_url]]
                                    
                                    # Tentar cada player
                                    for player_cmd in players:
                                        try:
                                            subprocess.run(player_cmd, check=True, capture_output=True)
                                            break
                                            
                                        except (subprocess.CalledProcessError, FileNotFoundError):
                                            continue
                                    else:
                                        print(f"❌ Não foi possível abrir o vídeo")
                                else:
                                    print(f"❌ URL do vídeo não encontrada")
                        except Exception:
                            print(f"❌ Erro ao carregar vídeo")
                        
                        print("Pressione Enter para continuar...")
                        input()
                        
                        # Recriar a tela curses
                        self.screen = curses.initscr()
                        curses.noecho()
                        curses.cbreak()
                        self.screen.keypad(True)
                        curses.curs_set(0)
                        
                        loading = False
                        video_url = None  # Reset para não mostrar na tela
                elif key == ord('\n') or key == ord('\r'):  # Enter - select episode
                    print(f"\n🎬 Estamos na página do episódio: {episodes[current_row].title}")
                    print(f"🔗 URL: {episodes[current_row].url}")
                    # Continue with the loop
                elif key == ord('q') or key == ord('Q') or key == 27:  # q or ESC
                    break
                    
        finally:
            if self.screen:
                curses.endwin()
    
    def _display_episodes(self, episodes: List[Episode], anime_title: str, current_row: int, video_url: str = None, loading: bool = False):
        """Display episodes with navigation."""
        self.screen.clear()
        
        # Get screen dimensions
        height, width = self.screen.getmaxyx()
        
        # Title
        title = f"📺 {anime_title} - Episódios:"
        if len(title) < width:
            self.screen.addstr(0, 0, title)
        else:
            self.screen.addstr(0, 0, title[:width-1])
        
        # Separator
        separator = "=" * min(width, 70)
        self.screen.addstr(1, 0, separator)
        
        # Instructions
        instructions = "W/S ou ↑/↓ para navegar, Enter para assistir, Q para sair"
        if len(instructions) < width:
            self.screen.addstr(2, 0, instructions)
        
        # Second separator
        self.screen.addstr(3, 0, "-" * min(width, 70))
        
        start_row = 5
        max_display = min(len(episodes), height - 15)  # Leave more space for UI
        start_episode = max(0, min(current_row - max_display // 2, len(episodes) - max_display))
        
        for i in range(max_display):
            episode_idx = start_episode + i
            if episode_idx >= len(episodes):
                break
                
            episode = episodes[episode_idx]
            date_str = f" [{episode.date}]" if episode.date else ""
            
            if episode_idx == current_row:
                prefix = "▶ "
                attr = curses.A_REVERSE
            else:
                prefix = "  "
                attr = curses.A_NORMAL
            
            line = f"{prefix}{episode}{date_str}"
            if len(line) > width - 1:
                line = line[:width-2] + "..."
            
            try:
                self.screen.addstr(start_row + i, 0, line, attr)
            except curses.error:
                continue
        
        # Navigation info
        if len(episodes) > max_display:
            nav_text = f"Mostrando {start_episode + 1}-{min(start_episode + max_display, len(episodes))} de {len(episodes)} episódios"
            if len(nav_text) < width:
                nav_row = start_row + max_display
                if nav_row < height - 1:  # Check if within screen bounds
                    self.screen.addstr(nav_row, 0, nav_text)
        
        # Video URL or loading
        video_start = start_row + max_display + 2
        if video_start < height - 1:  # Check if within screen bounds
            if loading:
                loading_text = "🎬 Preparando vídeo, aguarde..."
                try:
                    self.screen.addstr(video_start, 0, loading_text, curses.A_BOLD)
                except curses.error:
                    pass
            elif video_url:
                if video_url.startswith("❌"):
                    try:
                        self.screen.addstr(video_start, 0, video_url, curses.A_BOLD)
                    except curses.error:
                        pass
                else:
                    video_label = "🎬 Stream: "
                    try:
                        self.screen.addstr(video_start, 0, video_label, curses.A_BOLD)
                        # Display video URL in parts if too long
                        video_display = video_url
                        if len(video_display) > width - len(video_label):
                            video_display = video_display[:width - len(video_label) - 3] + "..."
                        self.screen.addstr(video_start, len(video_label), video_display)
                    except curses.error:
                        pass
        else:
            hint_text = "Pressione V para assistir ao vídeo"
            try:
                self.screen.addstr(video_start, 0, hint_text)
            except curses.error:
                pass
        
        self.screen.refresh()
