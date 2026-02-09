"""Custom exceptions for the hypr scraper."""


class HyprScraperError(Exception):
    """Base exception for hypr scraper."""
    pass


class NetworkError(HyprScraperError):
    """Raised when network operations fail."""
    pass


class ParsingError(HyprScraperError):
    """Raised when HTML parsing fails."""
    pass


class NoResultsError(HyprScraperError):
    """Raised when no search results are found."""
    pass
