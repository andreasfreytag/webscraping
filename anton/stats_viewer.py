# 📊 Stats Viewer & Comparison Tool
# View and compare analytics from previously scraped pages

import json
import os
from datetime import datetime


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
{ColorText.HEADER}{ColorText.BOLD}
╔══════════════════════════════════════════════════════╗
║       📊 SCRAPER STATS VIEWER & COMPARATOR 📊       ║
║          Analyze your scraped data!                  ║
╚══════════════════════════════════════════════════════╝
{ColorText.END}""")


def find_analytics_files():
    """Find all analytics JSON files"""
    files = [f for f in os.listdir('.') if f.startswith('analytics_') and f.endswith('.json')]
    return sorted(files, reverse=True)


def load_analytics(filename):
    """Load analytics from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"{ColorText.RED}Error loading {filename}: {e}{ColorText.END}")
        return None


def display_single_analytics(data, filename):
    """Display analytics from a single file"""
    print(f"\n{ColorText.BOLD}{ColorText.CYAN}File: {filename}{ColorText.END}")
    print("═" * 70)
    print(f"{ColorText.GREEN}URL:{ColorText.END} {data.get('url', 'Unknown')}")
    print(f"{ColorText.GREEN}Timestamp:{ColorText.END} {data.get('timestamp', 'Unknown')}")
    print(f"{ColorText.GREEN}Title:{ColorText.END} {data.get('title', 'No title')}")
    print("\n" + "─" * 70)
    print(f"{ColorText.YELLOW}📊 Statistics:{ColorText.END}")
    print(f"  🔗 Links: {data.get('links', 0)}")
    print(f"  🖼️  Images: {data.get('images', 0)}")

    if isinstance(data.get('headings'), dict):
        total_headings = sum(data['headings'].values())
        print(f"  📰 Headings: {total_headings}")
        print(f"     H1: {data['headings'].get('h1', 0)}, H2: {data['headings'].get('h2', 0)}, H3: {data['headings'].get('h3', 0)}")
    else:
        print(f"  📰 Headings: {data.get('headings', 0)}")

    print(f"  📝 Paragraphs: {data.get('paragraphs', 0)}")

    if 'forms' in data:
        print(f"  📋 Forms: {data.get('forms', 0)}")
    if 'tables' in data:
        print(f"  📊 Tables: {data.get('tables', 0)}")
    if 'lists' in data:
        print(f"  📑 Lists: {data.get('lists', 0)}")

    print(f"  📏 Text Length: {data.get('total_text_length', 0):,} characters")

    if 'word_count' in data:
        print(f"  💬 Word Count: {data.get('word_count', 0):,} words")

    print("═" * 70)


def compare_analytics(file1, file2):
    """Compare two analytics files"""
    data1 = load_analytics(file1)
    data2 = load_analytics(file2)

    if not data1 or not data2:
        return

    print(f"\n{ColorText.BOLD}{ColorText.HEADER}📊 COMPARISON{ColorText.END}")
    print("═" * 70)
    print(f"{ColorText.CYAN}File 1:{ColorText.END} {file1}")
    print(f"{ColorText.CYAN}File 2:{ColorText.END} {file2}")
    print("═" * 70)

    # Compare metrics
    metrics = [
        ('Links', 'links', '🔗'),
        ('Images', 'images', '🖼️'),
        ('Paragraphs', 'paragraphs', '📝'),
        ('Text Length', 'total_text_length', '📏'),
    ]

    if 'word_count' in data1 and 'word_count' in data2:
        metrics.append(('Word Count', 'word_count', '💬'))

    print(f"\n{ColorText.YELLOW}Metric Comparison:{ColorText.END}")
    print(f"{'Metric':<20} {'File 1':<15} {'File 2':<15} {'Difference':<15}")
    print("─" * 70)

    for name, key, emoji in metrics:
        val1 = data1.get(key, 0)
        val2 = data2.get(key, 0)
        diff = val2 - val1

        if diff > 0:
            diff_str = f"{ColorText.GREEN}+{diff:,}{ColorText.END}"
        elif diff < 0:
            diff_str = f"{ColorText.RED}{diff:,}{ColorText.END}"
        else:
            diff_str = f"{diff:,}"

        print(f"{emoji} {name:<17} {val1:>13,} {val2:>13,} {diff_str:>15}")

    print("═" * 70)


def generate_summary():
    """Generate summary of all scraped pages"""
    files = find_analytics_files()

    if not files:
        print(f"{ColorText.YELLOW}No analytics files found!{ColorText.END}")
        return

    print(f"\n{ColorText.BOLD}{ColorText.BLUE}📈 SUMMARY OF ALL SCRAPED PAGES{ColorText.END}")
    print("═" * 70)

    total_links = 0
    total_images = 0
    total_words = 0

    for filename in files:
        data = load_analytics(filename)
        if data:
            total_links += data.get('links', 0)
            total_images += data.get('images', 0)
            total_words += data.get('word_count', 0)

            print(f"\n{ColorText.CYAN}{filename}{ColorText.END}")
            print(f"  URL: {data.get('url', 'Unknown')[:60]}")
            print(f"  Title: {data.get('title', 'No title')[:60]}")
            print(f"  Links: {data.get('links', 0)}, Images: {data.get('images', 0)}")

    print("\n" + "═" * 70)
    print(f"{ColorText.BOLD}{ColorText.GREEN}TOTALS:{ColorText.END}")
    print(f"  📄 Pages scraped: {len(files)}")
    print(f"  🔗 Total links found: {total_links:,}")
    print(f"  🖼️  Total images found: {total_images:,}")
    if total_words > 0:
        print(f"  💬 Total words analyzed: {total_words:,}")
    print("═" * 70)


def main():
    """Main function"""
    print_banner()

    files = find_analytics_files()

    if not files:
        print(f"\n{ColorText.YELLOW}No analytics files found!{ColorText.END}")
        print(f"{ColorText.CYAN}Run the web scraper first to generate some data.{ColorText.END}")
        return

    print(f"\n{ColorText.GREEN}Found {len(files)} analytics file(s){ColorText.END}")

    while True:
        print(f"\n{ColorText.BOLD}OPTIONS:{ColorText.END}")
        print(f"  {ColorText.CYAN}1.{ColorText.END} View single file")
        print(f"  {ColorText.CYAN}2.{ColorText.END} Compare two files")
        print(f"  {ColorText.CYAN}3.{ColorText.END} View summary of all files")
        print(f"  {ColorText.CYAN}4.{ColorText.END} List all files")
        print(f"  {ColorText.RED}0.{ColorText.END} Exit")

        choice = input(f"\n{ColorText.BOLD}Choose option: {ColorText.END}").strip()

        if choice == '1':
            print(f"\n{ColorText.CYAN}Available files:{ColorText.END}")
            for i, f in enumerate(files, 1):
                print(f"  {i}. {f}")

            try:
                idx = int(input(f"\n{ColorText.YELLOW}Enter file number: {ColorText.END}")) - 1
                if 0 <= idx < len(files):
                    data = load_analytics(files[idx])
                    if data:
                        display_single_analytics(data, files[idx])
                else:
                    print(f"{ColorText.RED}Invalid number!{ColorText.END}")
            except ValueError:
                print(f"{ColorText.RED}Please enter a valid number!{ColorText.END}")

        elif choice == '2':
            if len(files) < 2:
                print(f"{ColorText.YELLOW}Need at least 2 files to compare!{ColorText.END}")
                continue

            print(f"\n{ColorText.CYAN}Available files:{ColorText.END}")
            for i, f in enumerate(files, 1):
                print(f"  {i}. {f}")

            try:
                idx1 = int(input(f"\n{ColorText.YELLOW}Enter first file number: {ColorText.END}")) - 1
                idx2 = int(input(f"{ColorText.YELLOW}Enter second file number: {ColorText.END}")) - 1

                if 0 <= idx1 < len(files) and 0 <= idx2 < len(files):
                    compare_analytics(files[idx1], files[idx2])
                else:
                    print(f"{ColorText.RED}Invalid numbers!{ColorText.END}")
            except ValueError:
                print(f"{ColorText.RED}Please enter valid numbers!{ColorText.END}")

        elif choice == '3':
            generate_summary()

        elif choice == '4':
            print(f"\n{ColorText.CYAN}All analytics files:{ColorText.END}")
            for i, f in enumerate(files, 1):
                size = os.path.getsize(f)
                print(f"  {ColorText.GREEN}{i:2d}.{ColorText.END} {f} ({size:,} bytes)")

        elif choice == '0':
            print(f"\n{ColorText.CYAN}Goodbye! 👋{ColorText.END}\n")
            break

        else:
            print(f"{ColorText.RED}Invalid option!{ColorText.END}")


if __name__ == "__main__":
    main()

