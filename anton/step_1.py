# Enhanced Web Scraper with Beautiful Output and Cool Features! 🚀
# This program fetches web pages and extracts useful information in style.

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
import json


class ColorText:
    """Add cool colors to terminal output"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def print_banner():
    """Display a cool ASCII banner"""
    banner = f"""
{ColorText.CYAN}{ColorText.BOLD}
╔══════════════════════════════════════════════╗
║       🌐 SUPER WEB SCRAPER 3000 🌐          ║
║          Made Cooler & Better!               ║
╚══════════════════════════════════════════════╝
{ColorText.END}"""
    print(banner)


def fetch_page(url):
    """
    Fetch a web page with proper error handling.
    Returns the HTML content or None if an error occurs.
    """
    try:
        print(f"{ColorText.YELLOW}⏳ Fetching: {ColorText.CYAN}{url}{ColorText.END}")

        # Add a user agent to avoid being blocked
        headers = {'User-Agent': 'Mozilla/5.0 (Web Scraper 3000)'}
        req = Request(url, headers=headers)

        page = urlopen(req, timeout=10)
        html = page.read().decode("utf-8")

        print(f"{ColorText.GREEN}✅ Success! Fetched {len(html)} bytes{ColorText.END}\n")
        return html

    except HTTPError as e:
        print(f"{ColorText.RED}❌ HTTP Error {e.code}: {e.reason}{ColorText.END}")
        return None
    except URLError as e:
        print(f"{ColorText.RED}❌ URL Error: {e.reason}{ColorText.END}")
        return None
    except Exception as e:
        print(f"{ColorText.RED}❌ Unexpected error: {e}{ColorText.END}")
        return None


def analyze_page(html):
    """
    Parse HTML and extract interesting information.
    Returns a BeautifulSoup object and analytics.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Gather analytics
    analytics = {
        'title': soup.title.string if soup.title else 'No title',
        'links': len(soup.find_all('a')),
        'images': len(soup.find_all('img')),
        'headings': len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])),
        'paragraphs': len(soup.find_all('p')),
        'total_text_length': len(soup.get_text())
    }

    return soup, analytics


def display_analytics(analytics):
    """Display page analytics in a cool formatted way"""
    print(f"{ColorText.BOLD}{ColorText.HEADER}📊 PAGE ANALYTICS{ColorText.END}")
    print("─" * 50)
    print(f"{ColorText.CYAN}📄 Title:{ColorText.END} {analytics['title']}")
    print(f"{ColorText.CYAN}🔗 Links:{ColorText.END} {analytics['links']}")
    print(f"{ColorText.CYAN}🖼️  Images:{ColorText.END} {analytics['images']}")
    print(f"{ColorText.CYAN}📰 Headings:{ColorText.END} {analytics['headings']}")
    print(f"{ColorText.CYAN}📝 Paragraphs:{ColorText.END} {analytics['paragraphs']}")
    print(f"{ColorText.CYAN}📏 Total Text:{ColorText.END} {analytics['total_text_length']} characters")
    print("─" * 50 + "\n")


def extract_links(soup):
    """Extract and display all links from the page"""
    links = soup.find_all('a')

    print(f"{ColorText.BOLD}{ColorText.BLUE}🔗 FOUND {len(links)} LINKS:{ColorText.END}")
    print("─" * 50)

    for i, link in enumerate(links[:10], 1):  # Show first 10 links
        href = link.get('href', 'No URL')
        text = link.get_text(strip=True) or 'No text'
        print(f"{ColorText.GREEN}{i}.{ColorText.END} {text[:50]}")
        print(f"   {ColorText.CYAN}→ {href}{ColorText.END}")

    if len(links) > 10:
        print(f"{ColorText.YELLOW}... and {len(links) - 10} more links{ColorText.END}")
    print()


def extract_headings(soup):
    """Extract and display all headings"""
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    print(f"{ColorText.BOLD}{ColorText.BLUE}📰 HEADINGS STRUCTURE:{ColorText.END}")
    print("─" * 50)

    for heading in headings:
        level = heading.name
        text = heading.get_text(strip=True)
        indent = "  " * (int(level[1]) - 1)
        print(f"{indent}{ColorText.YELLOW}{level.upper()}:{ColorText.END} {text}")
    print()


def save_to_file(html, url):
    """Save HTML and analytics to files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save HTML
    html_filename = f"scraped_page_{timestamp}.html"
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html)

    # Save analytics as JSON
    soup, analytics = analyze_page(html)
    analytics['url'] = url
    analytics['timestamp'] = timestamp

    json_filename = f"analytics_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(analytics, f, indent=2)

    print(f"{ColorText.GREEN}💾 Saved:{ColorText.END}")
    print(f"   HTML: {html_filename}")
    print(f"   Analytics: {json_filename}\n")


def main():
    """Main program function"""
    print_banner()

    # The URL to scrape
    url = "https://github.com/14148-MSs-DH/webscraping#"

    # Fetch the page
    html = fetch_page(url)

    if html:
        # Parse and analyze
        soup, analytics = analyze_page(html)

        # Display cool information
        display_analytics(analytics)
        extract_headings(soup)
        extract_links(soup)

        # Save to files
        save_to_file(html, url)

        print(f"{ColorText.BOLD}{ColorText.GREEN}✨ Scraping complete! ✨{ColorText.END}\n")
    else:
        print(f"{ColorText.RED}😞 Failed to fetch the page{ColorText.END}")


# Run the program!
if __name__ == "__main__":
    main()

