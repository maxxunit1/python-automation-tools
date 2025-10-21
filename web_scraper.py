#!/usr/bin/env python3
"""
Web Scraper - Extract data from websites
"""

import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional
import time
import json


class WebScraper:
    """Scrape data from websites"""

    def __init__(self, base_url: str, delay: float = 1.0):
        """
        Initialize WebScraper

        Args:
            base_url: Base URL for scraping
            delay: Delay between requests in seconds
        """
        self.base_url = base_url
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def fetch_page(self, url: str) -> Optional[BeautifulSoup]:
        """
        Fetch and parse a web page

        Args:
            url: URL to fetch

        Returns:
            BeautifulSoup object or None if failed
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            time.sleep(self.delay)
            return BeautifulSoup(response.content, 'html.parser')

        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_links(self, soup: BeautifulSoup) -> List[str]:
        """Extract all links from page"""
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                links.append(href)
            elif href.startswith('/'):
                links.append(self.base_url + href)
        return links

    def extract_text(self, soup: BeautifulSoup, selector: str) -> List[str]:
        """Extract text from elements matching selector"""
        elements = soup.select(selector)
        return [elem.get_text(strip=True) for elem in elements]

    def extract_data(
            self,
            url: str,
            selectors: Dict[str, str]
    ) -> Dict[str, List[str]]:
        """
        Extract data using CSS selectors

        Args:
            url: URL to scrape
            selectors: Dictionary of {field_name: css_selector}

        Returns:
            Dictionary of extracted data
        """
        soup = self.fetch_page(url)
        if not soup:
            return {}

        data = {}
        for field, selector in selectors.items():
            data[field] = self.extract_text(soup, selector)

        return data

    def save_to_json(self, data: dict, filename: str) -> None:
        """Save extracted data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Data saved to {filename}")


def main():
    """Main entry point"""
    # Example usage
    scraper = WebScraper('https://example.com')

    # Scrape a page
    soup = scraper.fetch_page('https://example.com')

    if soup:
        # Extract links
        links = scraper.extract_links(soup)
        print(f"Found {len(links)} links")

        # Extract specific data
        data = scraper.extract_data(
            'https://example.com',
            {
                'titles': 'h1, h2',
                'paragraphs': 'p'
            }
        )

        # Save to file
        scraper.save_to_json(data, 'scraped_data.json')


if __name__ == "__main__":
    main()

# Streamline email template in file handler to meet requirements - 2025-10-14 11:44:13
# Modified: 2025-10-14 11:44:13
CONFIG_VALUE = 'new_value'

# Address test coverage in utility functions - 2025-10-19 13:32:02
class NewFeature:
    def __init__(self):
        self.enabled = True
    
    def execute(self):
        return 'Feature executed'

# Integrate dependency in core system for code clarity - 2025-10-21 16:03:02
# Modified: 2025-10-21 16:03:02
CONFIG_VALUE = 'new_value'