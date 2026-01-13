# MEGA WEB SCRAPER 9000 - Interactive Edition! 🚀✨
# Enhanced with interactive menu, multi-URL support, and HTML reports!

from urllib.request import urlopen, Request, urlretrieve
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.parse import urljoin, urlparse
import json
import os
import time


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
    """Display an even cooler ASCII banner"""
    banner = f"""
{ColorText.HEADER}{ColorText.BOLD}
╔══════════════════════════════════════════════════════╗
║   🚀 MEGA WEB SCRAPER 9000 - INTERACTIVE! 🚀        ║
║        Now with 300% more awesome features!          ║
╚══════════════════════════════════════════════════════╝
{ColorText.END}"""
    print(banner)


def print_menu():
    """Display interactive menu"""
    print(f"\n{ColorText.CYAN}{ColorText.BOLD}📋 MENU:{ColorText.END}")
    print(f"{ColorText.GREEN}1.{ColorText.END} Scrape a single URL")
    print(f"{ColorText.GREEN}2.{ColorText.END} Scrape multiple URLs")
    print(f"{ColorText.GREEN}3.{ColorText.END} Extract all images from URL")
    print(f"{ColorText.GREEN}4.{ColorText.END} Generate HTML report")
    print(f"{ColorText.GREEN}5.{ColorText.END} Search for text in page")
    print(f"{ColorText.GREEN}6.{ColorText.END} View saved files")
    print(f"{ColorText.RED}0.{ColorText.END} Exit")
    print()


def fetch_page(url):
    """
    Fetch a web page with proper error handling.
    Returns the HTML content or None if an error occurs.
    """
    try:
        print(f"{ColorText.YELLOW}⏳ Fetching: {ColorText.CYAN}{url}{ColorText.END}")

        headers = {'User-Agent': 'Mozilla/5.0 (Mega Scraper 9000)'}
        req = Request(url, headers=headers)

        page = urlopen(req, timeout=10)
        html = page.read().decode("utf-8")

        print(f"{ColorText.GREEN}✅ Success! Fetched {len(html):,} bytes{ColorText.END}")
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
    """Parse HTML and extract comprehensive analytics"""
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Get text
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    # Gather comprehensive analytics
    analytics = {
        'title': soup.title.string if soup.title else 'No title',
        'links': len(soup.find_all('a')),
        'images': len(soup.find_all('img')),
        'headings': {
            'h1': len(soup.find_all('h1')),
            'h2': len(soup.find_all('h2')),
            'h3': len(soup.find_all('h3')),
            'h4': len(soup.find_all('h4')),
            'h5': len(soup.find_all('h5')),
            'h6': len(soup.find_all('h6'))
        },
        'paragraphs': len(soup.find_all('p')),
        'forms': len(soup.find_all('form')),
        'tables': len(soup.find_all('table')),
        'lists': len(soup.find_all(['ul', 'ol'])),
        'total_text_length': len(text),
        'word_count': len(text.split())
    }

    return soup, analytics


def display_analytics(analytics):
    """Display comprehensive page analytics"""
    print(f"\n{ColorText.BOLD}{ColorText.HEADER}📊 PAGE ANALYTICS{ColorText.END}")
    print("═" * 60)
    print(f"{ColorText.CYAN}📄 Title:{ColorText.END} {analytics['title']}")
    print(f"{ColorText.CYAN}🔗 Links:{ColorText.END} {analytics['links']}")
    print(f"{ColorText.CYAN}🖼️  Images:{ColorText.END} {analytics['images']}")
    print(f"{ColorText.CYAN}📰 Headings:{ColorText.END} H1: {analytics['headings']['h1']}, H2: {analytics['headings']['h2']}, H3: {analytics['headings']['h3']}")
    print(f"{ColorText.CYAN}📝 Paragraphs:{ColorText.END} {analytics['paragraphs']}")
    print(f"{ColorText.CYAN}📋 Forms:{ColorText.END} {analytics['forms']}")
    print(f"{ColorText.CYAN}📊 Tables:{ColorText.END} {analytics['tables']}")
    print(f"{ColorText.CYAN}📑 Lists:{ColorText.END} {analytics['lists']}")
    print(f"{ColorText.CYAN}📏 Text Length:{ColorText.END} {analytics['total_text_length']:,} characters")
    print(f"{ColorText.CYAN}💬 Word Count:{ColorText.END} {analytics['word_count']:,} words")
    print("═" * 60)


def extract_links(soup, limit=15):
    """Extract and display links"""
    links = soup.find_all('a')

    print(f"\n{ColorText.BOLD}{ColorText.BLUE}🔗 FOUND {len(links)} LINKS:{ColorText.END}")
    print("─" * 60)

    for i, link in enumerate(links[:limit], 1):
        href = link.get('href', 'No URL')
        text = link.get_text(strip=True) or 'No text'
        print(f"{ColorText.GREEN}{i:2d}.{ColorText.END} {text[:45]}")
        print(f"    {ColorText.CYAN}→ {href[:70]}{ColorText.END}")

    if len(links) > limit:
        print(f"{ColorText.YELLOW}... and {len(links) - limit} more links{ColorText.END}")


def extract_images(soup, base_url):
    """Extract all images from the page"""
    images = soup.find_all('img')

    print(f"\n{ColorText.BOLD}{ColorText.BLUE}🖼️  FOUND {len(images)} IMAGES:{ColorText.END}")
    print("─" * 60)

    image_data = []
    for i, img in enumerate(images, 1):
        src = img.get('src', '')
        alt = img.get('alt', 'No alt text')

        # Convert relative URLs to absolute
        if src:
            full_url = urljoin(base_url, src)
            image_data.append({'url': full_url, 'alt': alt})
            print(f"{ColorText.GREEN}{i:2d}.{ColorText.END} {alt[:40]}")
            print(f"    {ColorText.CYAN}→ {full_url[:70]}{ColorText.END}")

    return image_data


def download_images(image_data, output_dir="downloaded_images"):
    """Download all images to a directory"""
    if not image_data:
        print(f"{ColorText.YELLOW}No images to download{ColorText.END}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"\n{ColorText.YELLOW}📥 Downloading {len(image_data)} images...{ColorText.END}")

    for i, img in enumerate(image_data, 1):
        try:
            filename = os.path.join(output_dir, f"image_{i:03d}.{img['url'].split('.')[-1][:4]}")
            urlretrieve(img['url'], filename)
            print(f"{ColorText.GREEN}✓{ColorText.END} Downloaded: {filename}")
        except Exception as e:
            print(f"{ColorText.RED}✗{ColorText.END} Failed to download image {i}: {e}")

    print(f"{ColorText.GREEN}✅ Download complete!{ColorText.END}")


def search_text(soup, query):
    """Search for specific text in the page"""
    text = soup.get_text()
    count = text.lower().count(query.lower())

    print(f"\n{ColorText.BOLD}{ColorText.BLUE}🔍 SEARCH RESULTS for '{query}':{ColorText.END}")
    print("─" * 60)
    print(f"{ColorText.GREEN}Found {count} occurrence(s){ColorText.END}")

    if count > 0:
        # Find elements containing the text
        elements = soup.find_all(string=lambda text: text and query.lower() in text.lower())
        print(f"\n{ColorText.CYAN}First 5 matches:{ColorText.END}")
        for i, elem in enumerate(elements[:5], 1):
            print(f"{ColorText.YELLOW}{i}.{ColorText.END} {elem.strip()[:80]}...")


def generate_html_report(url, soup, analytics, timestamp):
    """Generate a beautiful HTML report"""
    filename = f"report_{timestamp}.html"

    links = soup.find_all('a')[:20]
    images = soup.find_all('img')[:10]
    headings = soup.find_all(['h1', 'h2', 'h3'])

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Web Scraping Report - {analytics['title']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
        }}
        .container {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }}
        h1 {{
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #764ba2;
            margin-top: 30px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
        }}
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.9;
        }}
        .link-list {{
            list-style: none;
            padding: 0;
        }}
        .link-list li {{
            background: #f8f9fa;
            margin: 10px 0;
            padding: 15px;
            border-radius: 5px;
            border-left: 4px solid #667eea;
        }}
        .link-list a {{
            color: #667eea;
            text-decoration: none;
            font-weight: bold;
        }}
        .link-list a:hover {{
            text-decoration: underline;
        }}
        .metadata {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin: 20px 0;
        }}
        .emoji {{
            font-size: 1.2em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🌐 Web Scraping Report</h1>
        
        <div class="metadata">
            <p><strong>URL:</strong> <a href="{url}" target="_blank">{url}</a></p>
            <p><strong>Scraped on:</strong> {datetime.now().strftime("%B %d, %Y at %I:%M %p")}</p>
            <p><strong>Page Title:</strong> {analytics['title']}</p>
        </div>
        
        <h2>📊 Quick Statistics</h2>
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number">🔗 {analytics['links']}</div>
                <div class="stat-label">Links</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">🖼️ {analytics['images']}</div>
                <div class="stat-label">Images</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">📝 {analytics['paragraphs']}</div>
                <div class="stat-label">Paragraphs</div>
            </div>
            <div class="stat-card">
                <div class="stat-number">💬 {analytics['word_count']:,}</div>
                <div class="stat-label">Words</div>
            </div>
        </div>
        
        <h2>📰 Headings Found</h2>
        <ul>
"""

    for heading in headings:
        html_content += f"            <li><strong>{heading.name.upper()}:</strong> {heading.get_text(strip=True)}</li>\n"

    html_content += """
        </ul>
        
        <h2>🔗 Top Links</h2>
        <ul class="link-list">
"""

    for link in links:
        href = link.get('href', '#')
        text = link.get_text(strip=True) or 'No text'
        html_content += f'            <li><a href="{href}" target="_blank">{text[:100]}</a></li>\n'

    html_content += """
        </ul>
        
        <footer style="margin-top: 50px; text-align: center; color: #666; padding-top: 20px; border-top: 1px solid #ddd;">
            <p>Generated by <strong>Mega Web Scraper 9000</strong> 🚀</p>
        </footer>
    </div>
</body>
</html>
"""

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n{ColorText.GREEN}📄 HTML Report saved: {filename}{ColorText.END}")
    return filename


def save_data(html, url, analytics, timestamp):
    """Save scraped data to files"""
    # Save HTML
    html_filename = f"scraped_{timestamp}.html"
    with open(html_filename, 'w', encoding='utf-8') as f:
        f.write(html)

    # Save analytics as JSON
    analytics['url'] = url
    analytics['timestamp'] = timestamp

    json_filename = f"analytics_{timestamp}.json"
    with open(json_filename, 'w', encoding='utf-8') as f:
        json.dump(analytics, f, indent=2)

    print(f"\n{ColorText.GREEN}💾 Data saved:{ColorText.END}")
    print(f"   HTML: {html_filename}")
    print(f"   Analytics: {json_filename}")


def scrape_single_url():
    """Scrape a single URL - interactive"""
    url = input(f"{ColorText.CYAN}Enter URL to scrape: {ColorText.END}").strip()

    if not url.startswith('http'):
        url = 'https://' + url

    html = fetch_page(url)
    if not html:
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    soup, analytics = analyze_page(html)

    display_analytics(analytics)
    extract_links(soup)

    save_choice = input(f"\n{ColorText.YELLOW}Save data? (y/n): {ColorText.END}").strip().lower()
    if save_choice == 'y':
        save_data(html, url, analytics, timestamp)

        report_choice = input(f"{ColorText.YELLOW}Generate HTML report? (y/n): {ColorText.END}").strip().lower()
        if report_choice == 'y':
            generate_html_report(url, soup, analytics, timestamp)


def scrape_multiple_urls():
    """Scrape multiple URLs"""
    print(f"{ColorText.CYAN}Enter URLs (one per line, empty line to finish):{ColorText.END}")
    urls = []

    while True:
        url = input(f"{ColorText.GREEN}> {ColorText.END}").strip()
        if not url:
            break
        if not url.startswith('http'):
            url = 'https://' + url
        urls.append(url)

    if not urls:
        print(f"{ColorText.RED}No URLs entered!{ColorText.END}")
        return

    print(f"\n{ColorText.YELLOW}🚀 Scraping {len(urls)} URLs...{ColorText.END}\n")

    results = []
    for i, url in enumerate(urls, 1):
        print(f"\n{ColorText.BOLD}[{i}/{len(urls)}]{ColorText.END}")
        html = fetch_page(url)
        if html:
            soup, analytics = analyze_page(html)
            results.append({'url': url, 'analytics': analytics})
            display_analytics(analytics)
            time.sleep(1)  # Be nice to servers

    # Save summary
    if results:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        summary_file = f"multi_scrape_summary_{timestamp}.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"\n{ColorText.GREEN}📄 Summary saved: {summary_file}{ColorText.END}")


def extract_images_mode():
    """Extract and optionally download images from a URL"""
    url = input(f"{ColorText.CYAN}Enter URL to extract images from: {ColorText.END}").strip()

    if not url.startswith('http'):
        url = 'https://' + url

    html = fetch_page(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')
    image_data = extract_images(soup, url)

    if image_data:
        download_choice = input(f"\n{ColorText.YELLOW}Download all images? (y/n): {ColorText.END}").strip().lower()
        if download_choice == 'y':
            download_images(image_data)


def search_mode():
    """Search for text in a webpage"""
    url = input(f"{ColorText.CYAN}Enter URL to search: {ColorText.END}").strip()

    if not url.startswith('http'):
        url = 'https://' + url

    html = fetch_page(url)
    if not html:
        return

    soup = BeautifulSoup(html, 'html.parser')

    query = input(f"{ColorText.CYAN}Enter search term: {ColorText.END}").strip()
    search_text(soup, query)


def view_saved_files():
    """View all saved files"""
    print(f"\n{ColorText.BOLD}{ColorText.BLUE}📁 SAVED FILES:{ColorText.END}")
    print("─" * 60)

    files = [f for f in os.listdir('.') if f.startswith(('scraped_', 'analytics_', 'report_'))]

    if files:
        for i, file in enumerate(sorted(files), 1):
            size = os.path.getsize(file)
            print(f"{ColorText.GREEN}{i:2d}.{ColorText.END} {file} ({size:,} bytes)")
    else:
        print(f"{ColorText.YELLOW}No saved files found{ColorText.END}")


def main():
    """Main program with interactive menu"""
    print_banner()

    while True:
        print_menu()
        choice = input(f"{ColorText.BOLD}Choose an option: {ColorText.END}").strip()

        if choice == '1':
            scrape_single_url()
        elif choice == '2':
            scrape_multiple_urls()
        elif choice == '3':
            extract_images_mode()
        elif choice == '4':
            url = input(f"{ColorText.CYAN}Enter URL for HTML report: {ColorText.END}").strip()
            if not url.startswith('http'):
                url = 'https://' + url
            html = fetch_page(url)
            if html:
                soup, analytics = analyze_page(html)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                generate_html_report(url, soup, analytics, timestamp)
        elif choice == '5':
            search_mode()
        elif choice == '6':
            view_saved_files()
        elif choice == '0':
            print(f"\n{ColorText.CYAN}Thanks for using Mega Web Scraper 9000! 🚀{ColorText.END}\n")
            break
        else:
            print(f"{ColorText.RED}Invalid choice! Please try again.{ColorText.END}")


if __name__ == "__main__":
    main()

