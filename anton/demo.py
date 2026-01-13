# 🎯 Demo Script - Test the Web Scraper!
# Run this to see a quick demo of the scraper's capabilities

from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

print("""
╔══════════════════════════════════════════════════════╗
║              🌟 WEB SCRAPER DEMO 🌟                 ║
║         Testing basic functionality first!           ║
╚══════════════════════════════════════════════════════╝
""")

print("Step 1: Testing basic URL fetching...")
print("=" * 60)

url = "https://example.com"
print(f"🌐 Fetching: {url}")

try:
    headers = {'User-Agent': 'Mozilla/5.0 (Demo Scraper)'}
    req = Request(url, headers=headers)
    page = urlopen(req, timeout=10)
    html = page.read().decode("utf-8")

    print(f"✅ SUCCESS! Fetched {len(html):,} bytes")
    print(f"\nFirst 500 characters:")
    print("-" * 60)
    print(html[:500])
    print("-" * 60)

    print(f"\n✨ Basic fetching works! Now try the full scrapers:")
    print(f"   • python3 anton/step_1.py - For enhanced scraper")
    print(f"   • python3 anton/step_2.py - For interactive mega scraper")

except Exception as e:
    print(f"❌ Error: {e}")
    print("\nMake sure you have internet connection!")

print("\n🎉 Demo complete!")

