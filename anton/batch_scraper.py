# 🚀 Batch Web Scraper - Scrape Multiple URLs from File!
# Reads URLs from urls.txt and scrapes them all automatically

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
from datetime import datetime
import json
import time
import sys


class ColorText:
    """Terminal colors"""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_banner():
    """Display banner"""
    print(f"""
{ColorText.CYAN}{ColorText.BOLD}
╔══════════════════════════════════════════════════════╗
║         🚀 BATCH WEB SCRAPER 🚀                     ║
║      Scrape multiple URLs automatically!             ║
╚══════════════════════════════════════════════════════╝
{ColorText.END}""")


def read_urls_from_file(filename='urls.txt'):
    """Read URLs from a text file, ignoring comments and empty lines"""
    try:
        with open(filename, 'r') as f:
            urls = []
            for line in f:
                line = line.strip()
                # Skip comments and empty lines
                if line and not line.startswith('#'):
                    if not line.startswith('http'):
                        line = 'https://' + line
                    urls.append(line)
            return urls
    except FileNotFoundError:
        print(f"{ColorText.RED}❌ File '{filename}' not found!{ColorText.END}")
        print(f"{ColorText.YELLOW}💡 Create a urls.txt file with one URL per line{ColorText.END}")
        return []
    except Exception as e:
        print(f"{ColorText.RED}❌ Error reading file: {e}{ColorText.END}")
        return []


def fetch_page(url):
    """Fetch a web page with error handling"""
    try:
        print(f"{ColorText.YELLOW}⏳ Fetching: {ColorText.CYAN}{url}{ColorText.END}")

        headers = {'User-Agent': 'Mozilla/5.0 (Batch Scraper)'}
        req = Request(url, headers=headers)

        page = urlopen(req, timeout=10)
        html = page.read().decode("utf-8")

        print(f"{ColorText.GREEN}✅ Success! {len(html):,} bytes{ColorText.END}")
        return html

    except HTTPError as e:
        print(f"{ColorText.RED}❌ HTTP Error {e.code}: {e.reason}{ColorText.END}")
        return None
    except URLError as e:
        print(f"{ColorText.RED}❌ URL Error: {e.reason}{ColorText.END}")
        return None
    except Exception as e:
        print(f"{ColorText.RED}❌ Error: {e}{ColorText.END}")
        return None


def analyze_page(html):
    """Parse and analyze HTML"""
    soup = BeautifulSoup(html, 'html.parser')

    # Remove scripts and styles
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    analytics = {
        'title': soup.title.string if soup.title else 'No title',
        'links': len(soup.find_all('a')),
        'images': len(soup.find_all('img')),
        'headings': {
            'h1': len(soup.find_all('h1')),
            'h2': len(soup.find_all('h2')),
            'h3': len(soup.find_all('h3')),
        },
        'paragraphs': len(soup.find_all('p')),
        'forms': len(soup.find_all('form')),
        'tables': len(soup.find_all('table')),
        'total_text_length': len(text),
        'word_count': len(text.split())
    }

    return soup, analytics


def display_progress_bar(current, total, bar_length=40):
    """Display a cool progress bar"""
    progress = current / total
    filled = int(bar_length * progress)
    bar = '█' * filled + '░' * (bar_length - filled)
    percent = progress * 100

    print(f"\r{ColorText.CYAN}Progress: [{bar}] {percent:.1f}% ({current}/{total}){ColorText.END}", end='')
    if current == total:
        print()  # New line when complete


def scrape_urls(urls, delay=1):
    """Scrape multiple URLs with progress tracking"""
    total = len(urls)
    results = []
    successful = 0
    failed = 0

    print(f"\n{ColorText.BOLD}Starting batch scrape of {total} URLs...{ColorText.END}\n")

    for i, url in enumerate(urls, 1):
        print(f"\n{ColorText.BOLD}[{i}/{total}]{ColorText.END}")
        print("─" * 60)

        html = fetch_page(url)

        if html:
            soup, analytics = analyze_page(html)
            analytics['url'] = url
            analytics['scraped_at'] = datetime.now().isoformat()

            results.append({
                'url': url,
                'status': 'success',
                'analytics': analytics
            })

            # Display quick stats
            print(f"{ColorText.GREEN}📊 Quick Stats:{ColorText.END}")
            print(f"   Title: {analytics['title'][:50]}")
            print(f"   Links: {analytics['links']}, Images: {analytics['images']}, Words: {analytics['word_count']:,}")

            successful += 1
        else:
            results.append({
                'url': url,
                'status': 'failed'
            })
            failed += 1

        # Progress bar
        display_progress_bar(i, total)

        # Delay between requests (be nice to servers!)
        if i < total:
            time.sleep(delay)

    return results, successful, failed


def save_batch_results(results):
    """Save batch scraping results"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save complete results
    results_file = f"batch_results_{timestamp}.json"
    with open(results_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    # Create summary report
    summary_file = f"batch_summary_{timestamp}.txt"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("BATCH SCRAPING SUMMARY\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 70 + "\n\n")

        for result in results:
            url = result['url']
            status = result['status']

            f.write(f"URL: {url}\n")
            f.write(f"Status: {status.upper()}\n")

            if status == 'success':
                analytics = result['analytics']
                f.write(f"Title: {analytics['title']}\n")
                f.write(f"Links: {analytics['links']}, Images: {analytics['images']}\n")
                f.write(f"Words: {analytics['word_count']:,}\n")

            f.write("-" * 70 + "\n\n")

    print(f"\n{ColorText.GREEN}💾 Results saved:{ColorText.END}")
    print(f"   Complete data: {results_file}")
    print(f"   Summary: {summary_file}")


def display_final_summary(results, successful, failed):
    """Display final summary"""
    print(f"\n{ColorText.BOLD}{ColorText.HEADER}📊 FINAL SUMMARY{ColorText.END}")
    print("═" * 60)
    print(f"{ColorText.GREEN}✅ Successful:{ColorText.END} {successful}")
    print(f"{ColorText.RED}❌ Failed:{ColorText.END} {failed}")
    print(f"{ColorText.CYAN}📄 Total:{ColorText.END} {len(results)}")

    if successful > 0:
        # Calculate aggregate stats
        total_links = sum(r['analytics']['links'] for r in results if r['status'] == 'success')
        total_images = sum(r['analytics']['images'] for r in results if r['status'] == 'success')
        total_words = sum(r['analytics']['word_count'] for r in results if r['status'] == 'success')

        print(f"\n{ColorText.YELLOW}Aggregate Statistics:{ColorText.END}")
        print(f"  🔗 Total Links: {total_links:,}")
        print(f"  🖼️  Total Images: {total_images:,}")
        print(f"  💬 Total Words: {total_words:,}")

    print("═" * 60)


def main():
    """Main function"""
    print_banner()

    # Allow custom file via command line argument
    filename = 'urls.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    print(f"\n{ColorText.CYAN}📋 Reading URLs from: {filename}{ColorText.END}")

    urls = read_urls_from_file(filename)

    if not urls:
        print(f"\n{ColorText.YELLOW}No URLs to scrape!{ColorText.END}")
        print(f"\n{ColorText.CYAN}Example urls.txt format:{ColorText.END}")
        print("  https://example.com")
        print("  https://github.com")
        print("  # This is a comment (ignored)")
        return

    print(f"{ColorText.GREEN}✓ Found {len(urls)} URL(s) to scrape{ColorText.END}")
    print(f"\n{ColorText.YELLOW}URLs to scrape:{ColorText.END}")
    for i, url in enumerate(urls, 1):
        print(f"  {i}. {url}")

    # Confirm before starting
    confirm = input(f"\n{ColorText.BOLD}Start scraping? (y/n): {ColorText.END}").strip().lower()

    if confirm != 'y':
        print(f"{ColorText.YELLOW}Cancelled!{ColorText.END}")
        return

    # Scrape all URLs
    results, successful, failed = scrape_urls(urls, delay=1)

    # Save results
    if results:
        save_batch_results(results)
        display_final_summary(results, successful, failed)

    print(f"\n{ColorText.BOLD}{ColorText.GREEN}✨ Batch scraping complete! ✨{ColorText.END}\n")


if __name__ == "__main__":
    main()

