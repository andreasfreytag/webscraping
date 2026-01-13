# 🚀 Super Web Scraper Collection

A collection of awesome web scraping tools with beautiful output and cool features!

## Features ✨

### Step 1: Enhanced Web Scraper (`step_1.py`)
The enhanced version with beautiful colored terminal output and comprehensive analytics!

**Features:**
- 🎨 **Colorful Terminal Output** - Easy-to-read colored text
- 📊 **Page Analytics** - Automatically analyze:
  - Page title
  - Number of links, images, headings, paragraphs
  - Total text length and word count
- 🔗 **Link Extraction** - Display all links with their text
- 📰 **Heading Structure** - View the page's heading hierarchy
- 💾 **Data Saving** - Save HTML and analytics to files
- ⚠️ **Error Handling** - Robust error handling for network issues

**Usage:**
```bash
python3 anton/step_1.py
```

### Step 2: Mega Web Scraper 9000 (`step_2.py`)
The ultimate interactive web scraper with advanced features!

**Features:**
- 🎯 **Interactive Menu** - Easy-to-use menu system
- 🌐 **Multi-URL Scraping** - Scrape multiple websites at once
- 🖼️ **Image Extraction** - Find and download all images
- 📄 **HTML Reports** - Generate beautiful HTML reports with:
  - Gradient backgrounds
  - Statistics cards
  - Formatted link lists
  - Professional styling
- 🔍 **Text Search** - Search for specific text within pages
- 📁 **File Management** - View all saved files
- 💬 **Word Count** - Get word count and text statistics
- 📊 **Advanced Analytics** - Track forms, tables, lists, and more

**Usage:**
```bash
python3 anton/step_2.py
```

### Stats Viewer & Comparator (`stats_viewer.py`)
Analyze and compare your scraped data!

**Features:**
- 📊 **View Analytics** - View detailed stats from any scraped page
- 🔄 **Compare Pages** - Side-by-side comparison of two scraped pages
- 📈 **Summary Reports** - Overview of all scraped pages
- 📁 **File Management** - List and browse all analytics files
- 💹 **Difference Tracking** - See what changed between pages

**Usage:**
```bash
python3 anton/stats_viewer.py
```

### Demo Script (`demo.py`)
Quick test to verify everything works!

**Usage:**
```bash
python3 anton/demo.py
```

## Installation 📦

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install beautifulsoup4
```

## Menu Options (Step 2) 📋

1. **Scrape a single URL** - Enter any URL to scrape and analyze
2. **Scrape multiple URLs** - Batch scraping with summary report
3. **Extract all images** - Find and download images from a page
4. **Generate HTML report** - Create a beautiful visual report
5. **Search for text** - Find specific text within a webpage
6. **View saved files** - See all your scraped data
0. **Exit** - Close the program

## Output Files 📁

The scraper generates several types of files:

- `scraped_YYYYMMDD_HHMMSS.html` - Raw HTML content
- `analytics_YYYYMMDD_HHMMSS.json` - Structured analytics data
- `report_YYYYMMDD_HHMMSS.html` - Beautiful visual report
- `multi_scrape_summary_YYYYMMDD_HHMMSS.json` - Multi-URL summary
- `batch_results_YYYYMMDD_HHMMSS.json` - Batch scraping results
- `batch_summary_YYYYMMDD_HHMMSS.txt` - Batch scraping summary
- `downloaded_images/` - Folder with downloaded images

## All Tools 🛠️

1. **step_1.py** - Enhanced web scraper with analytics
2. **step_2.py** - Interactive mega scraper with menu
3. **batch_scraper.py** - Automatic batch scraping from file
4. **stats_viewer.py** - View and compare scraped data
5. **demo.py** - Quick functionality test

## Examples 💡

### Scrape a website and generate a report:
1. Run `python3 anton/step_2.py`
2. Choose option `1` (Scrape a single URL)
3. Enter a URL (e.g., `github.com`)
4. Choose `y` to save data
5. Choose `y` to generate HTML report
6. Open the generated HTML file in your browser!

### Download all images from a page:
1. Run `python3 anton/step_2.py`
2. Choose option `3` (Extract all images)
3. Enter the URL
4. Choose `y` to download images
5. Check the `downloaded_images/` folder

### Search for specific content:
1. Run `python3 anton/step_2.py`
2. Choose option `5` (Search for text)
3. Enter the URL
4. Enter your search term
5. See all occurrences!

## Color Coding 🎨

The terminal output uses colors to make information easier to read:

- 🔵 **Blue** - Headers and section titles
- 🟢 **Green** - Success messages and item numbers
- 🟡 **Yellow** - Warnings and prompts
- 🔴 **Red** - Errors
- 🔷 **Cyan** - URLs and metadata
- 🟣 **Purple** - Special headers

## Tips & Tricks 💡

1. **Be Respectful** - Don't overwhelm servers with too many requests
2. **Check robots.txt** - Respect website scraping policies
3. **Use responsibly** - Only scrape publicly available data
4. **Save your work** - Always save analytics for later review
5. **Generate reports** - HTML reports are great for presentations!

## Requirements 📋

- Python 3.6+
- beautifulsoup4 4.12.0+

## Author ✍️

Created with ❤️ for the FU Web Scraping Project

## License 📄

Free to use for educational purposes!

---

**Happy Scraping! 🚀✨**

