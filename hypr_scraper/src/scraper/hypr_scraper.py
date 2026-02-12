"""Scraper for hypr anime website."""

import re
from typing import List, Optional, Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
try:
    from src.utils.exceptions import HyprScraperError, NetworkError
except ImportError:
    # Fallback for direct execution
    class HyprScraperError(Exception):
        pass
    class NetworkError(HyprScraperError):
        pass


class HyprScraper:
    """Scraper for hypr anime website."""
    
    def __init__(self):
        self.driver = None
        self.setup_driver()
    
    def setup_driver(self):
        """Setup Chrome driver with minimal options and clean output."""
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        # Enable performance and network logging for video extraction
        options.set_capability('goog:loggingPrefs', {
            'performance': 'ALL',  # Essential for video URL capture
            'network': 'ALL'       # Also needed for some video URLs
        })
        
        try:
            self.driver = webdriver.Chrome(options=options)
        except Exception as e:
            raise HyprScraperError(f"Failed to setup driver: {e}")
    
    def search_anime(self, query: str) -> List[Dict[str, Any]]:
        """
        Search for anime on animesdigital.org - ultra fast version.
        """
        try:
            # Format search URL
            search_url = f"https://animesdigital.org/search/{query.replace(' ', '+')}"
            
            self.driver.get(search_url)
            
            # Ultra fast wait
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Find all anime items
            anime_items = []
            
            try:
                # Look for div.itemA elements
                items = self.driver.find_elements(By.CSS_SELECTOR, "div.itemA")
                
                for item in items:
                    try:
                        # Get link and title
                        link_element = item.find_element(By.TAG_NAME, "a")
                        url = link_element.get_attribute("href")
                        
                        # Get title from span.title_anime
                        title_element = item.find_element(By.CSS_SELECTOR, "span.title_anime")
                        title = title_element.text.strip()
                        
                        if url and title:
                            anime_items.append({
                                "title": title,
                                "url": url
                            })
                            
                    except Exception:
                        continue
                        
            except Exception:
                return []
            
            return anime_items
            
        except Exception:
            return []
    
    def get_episodes(self, anime_url: str) -> List[Dict[str, Any]]:
        """
        Get episode list from anime page - ultra fast version.
        """
        try:
            self.driver.get(anime_url)
            
            # Ultra fast wait
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Find all episode items
            episodes = []
            
            try:
                # Look for div.item_ep elements
                episode_items = self.driver.find_elements(By.CSS_SELECTOR, "div.item_ep")
                
                for item in episode_items:
                    try:
                        # Get link and title
                        link_element = item.find_element(By.TAG_NAME, "a")
                        url = link_element.get_attribute("href")
                        
                        # Get title from div.title_anime
                        title_element = item.find_element(By.CSS_SELECTOR, "div.title_anime")
                        title = title_element.text.strip()
                        
                        # Extract episode number from title
                        episode_num = self._extract_episode_number(title)
                        
                        if url and title:
                            episodes.append({
                                "title": title,
                                "url": url,
                                "episode": episode_num
                            })
                            
                    except Exception:
                        continue
                        
            except Exception:
                return []
            
            # Sort by episode number (descending - newest first)
            episodes.sort(key=lambda x: x["episode"], reverse=True)
            
            return episodes
            
        except Exception:
            return []
    
    def _extract_episode_number(self, title: str) -> int:
        """Extract episode number from title."""
        # Look for patterns like "Episódio 13", "Ep 13", etc.
        patterns = [
            r'episódio\s*(\d+)',
            r'ep\s*(\d+)',
            r'episode\s*(\d+)',
            r'(\d+)\s*$'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, title.lower())
            if match:
                return int(match.group(1))
        
        # Default to 0 if no episode number found
        return 0
    
    def _resolve_redirect_url(self, url: str) -> str:
        """Resolve redirect URLs to get the final URL."""
        try:
            import requests
            # Follow redirects and get final URL
            response = requests.head(url, allow_redirects=True, timeout=10)
            return response.url
        except Exception:
            return url
    
    def _parse_m3u8_segments(self, url: str) -> str:
        """Parse M3U8 playlist or HTML redirect and return video URL."""
        try:
            import requests
            import re
            
            # Download content
            headers = {'Referer': 'https://animesdigital.org'}
            response = requests.get(url, headers=headers, timeout=10)
            content = response.text
            
            # Check if it's HTML (redirect page) or M3U8
            if content.strip().startswith('#EXTM3U'):
                # It's a real M3U8 file
                lines = content.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('#') and (line.endswith('.ts') or line.endswith('.mp4')):
                        # If relative URL, make it absolute
                        if line.startswith('http'):
                            return line
                        else:
                            # Extract base URL from M3U8 URL
                            base_url = url.rsplit('/', 1)[0]
                            return f"{base_url}/{line}"
            else:
                # It's HTML, extract M3U8 URL from JavaScript
                file_match = re.search(r"file\s*:\s*['\"]([^'\"]*\.m3u8[^'\"]*)['\"]", content)
                if file_match:
                    m3u8_url = file_match.group(1)
                    if m3u8_url.startswith('http'):
                        # Now download the real M3U8
                        m3u8_response = requests.get(m3u8_url, headers=headers, timeout=10)
                        m3u8_content = m3u8_response.text
                        
                        if m3u8_content.strip().startswith('#EXTM3U'):
                            lines = m3u8_content.split('\n')
                            for line in lines:
                                line = line.strip()
                                if line and not line.startswith('#') and (line.endswith('.ts') or line.endswith('.mp4')):
                                    # If relative URL, make it absolute
                                    if line.startswith('http'):
                                        return line
                                    else:
                                        # Extract base URL from M3U8 URL
                                        base_url = m3u8_url.rsplit('/', 1)[0]
                                        return f"{base_url}/{line}"
            
            # If no segments found, return original URL
            return url
            
        except Exception as e:
            print(f"Erro ao fazer parse M3U8: {e}")
            return url
    
    def _capture_google_video_url(self) -> Optional[str]:
        """Capture video URL from network logs - ultra fast version."""
        try:
            import time
            import json
            
            # Wait minimal time for video requests
            time.sleep(3)
            
            # Get performance logs only (faster)
            try:
                logs = self.driver.get_log('performance')
            except:
                return None
            
            # Procura por URLs de vídeo - retorna imediatamente ao encontrar
            for entry in logs:
                try:
                    message = json.loads(entry['message'])
                    message_data = message.get('message', {})
                    
                    if message_data.get('method') in ['Network.responseReceived', 'Network.requestWillBeSent']:
                        if message_data.get('method') == 'Network.responseReceived':
                            url = message_data.get('params', {}).get('response', {}).get('url', '')
                        else:
                            url = message_data.get('params', {}).get('request', {}).get('url', '')
                        
                        # Procura URLs de vídeo - retorna imediatamente
                        if any(pattern in url.lower() for pattern in ['videoplayback', 'video/mp4', '.mp4', 'm3u8']):
                            return url
                            
                except (json.JSONDecodeError, KeyError, TypeError):
                    continue
                    
        except Exception:
            return None
    
    def get_video_url(self, episode_url: str) -> Optional[str]:
        """
        Get video URL from episode page.
        
        Args:
            episode_url: URL of the episode page
            
        Returns:
            Video URL or None if not found
        """
        try:
            self.driver.get(episode_url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # Try to find and click play button to trigger video loading
            try:
                player = self.driver.find_element(By.ID, "player")
                self.driver.execute_script("arguments[0].click();", player)
            except:
                pass
            
            # Try to enter iframe and trigger video
            try:
                iframes = self.driver.find_elements(By.TAG_NAME, "iframe")
                if iframes:
                    self.driver.switch_to.frame(iframes[0])
                    
                    # Try to find and play video
                    try:
                        video = self.driver.find_element(By.TAG_NAME, "video")
                        self.driver.execute_script("arguments[0].play();", video)
                    except:
                        pass
                    
                    self.driver.switch_to.default_content()
            except:
                pass
            
            # Wait for video requests (faster)
            import time
            time.sleep(3)
            
            # Capture video URL from network logs
            found_video_url = self._capture_google_video_url()
            if found_video_url:
                resolved_url = self._resolve_redirect_url(found_video_url)
                # If it's an M3U8 URL, try to parse it for direct segments
                if '.m3u8' in resolved_url.lower():
                    segment_url = self._parse_m3u8_segments(resolved_url)
                    if segment_url != resolved_url:
                        return segment_url
                return resolved_url
            
            # Try to find video element
            try:
                video = WebDriverWait(self.driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "video"))
                )
                
                # Wait for src to be populated
                time.sleep(3)
                
                video_src = video.get_attribute("src")
                if video_src:
                    return video_src
                else:
                    # Try currentSrc
                    current_src = self.driver.execute_script("return arguments[0].currentSrc;", video)
                    if current_src:
                        return current_src
                        
            except TimeoutException:
                pass
            
            # Look for JWPlayer
            try:
                jwplayer_url = self.driver.execute_script("""
                    var player = jwplayer();
                    if(player && player.getPlaylistItem){
                        var item = player.getPlaylistItem();
                        if(item && item.sources){
                            for(var i=0;i<item.sources.length;i++){
                                if(item.sources[i].file && item.sources[i].file.endsWith('.m3u8')){
                                    return item.sources[i].file;
                                }
                            }
                        }
                    }
                    return null;
                """)
                
                if jwplayer_url:
                    return jwplayer_url
                    
            except Exception:
                pass
            
            # Look for scripts with video URLs
            try:
                scripts = self.driver.find_elements(By.TAG_NAME, "script")
                for script in scripts:
                    script_content = script.get_attribute("innerHTML") or ""
                    if script_content and ("m3u8" in script_content or "mp4" in script_content):
                        # Extract URLs from script
                        import re
                        patterns = [
                            r'https://[^\s"\']*\.m3u8[^"\']*',
                            r'https://[^\s"\']*\.mp4[^"\']*',
                            r'file["\']?\s*:\s*["\']([^"\']*\.(?:m3u8|mp4)[^"\']*)["\']',
                            r'src["\']?\s*:\s*["\']([^"\']*\.(?:m3u8|mp4)[^"\']*)["\']'
                        ]
                        
                        for pattern in patterns:
                            matches = re.findall(pattern, script_content)
                            if matches:
                                for match in matches:
                                    if isinstance(match, tuple):
                                        match = match[0]
                                    return match
                                    
            except Exception:
                pass
            
            return None
            
        except Exception:
            return None
    
    def close(self):
        """Close the driver."""
        if self.driver:
            self.driver.quit()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
