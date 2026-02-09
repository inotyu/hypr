"""Utility modules for hypr scraper."""

from .exceptions import (
    HyprScraperError,
    NetworkError,
    ParsingError,
    NoResultsError
)

__all__ = [
    'HyprScraperError',
    'NetworkError',
    'ParsingError',
    'NoResultsError'
]
