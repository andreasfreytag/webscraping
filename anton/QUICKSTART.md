# 🚀 Quick Start Guide

Welcome to the Super Web Scraper Collection! Here's how to get started in 60 seconds.

## Step 1: Install Dependencies ⚙️

```bash
cd "/Users/Tosha/Desktop/Projects/FU project/webscraping"
pip install beautifulsoup4
```

## Step 2: Test Basic Functionality ✅

```bash
python3 anton/demo.py
```

You should see a successful fetch from example.com!

## Step 3: Try the Enhanced Scraper 🌟

```bash
python3 anton/step_1.py
```

This will scrape a page and show you:
- Beautiful colored output
- Page analytics (links, images, headings, etc.)
- Saved HTML and JSON files

## Step 4: Try the Interactive Scraper 🎯

```bash
python3 anton/step_2.py
```

This opens an interactive menu where you can:
1. Scrape any URL you want
2. Extract images
3. Generate beautiful HTML reports
4. Search for text in pages
5. Much more!

## Step 5: Batch Scraping 📋

1. Edit `anton/urls.txt` and add your URLs (one per line)
2. Run the batch scraper:

```bash
python3 anton/batch_scraper.py
```

It will scrape all URLs and create summary reports!

## Step 6: View Your Results 📊

```bash
python3 anton/stats_viewer.py
```

This lets you:
- View analytics from any scraped page
- Compare two pages side-by-side
- See summary of all scraped pages

## Common Tasks 📝

### Scrape a Single URL
```bash
python3 anton/step_2.py
# Choose option 1
# Enter your URL
```

### Generate HTML Report
```bash
python3 anton/step_2.py
# Choose option 4
# Enter your URL
# Open the generated .html file in your browser!
```

### Download All Images from a Page
```bash
python3 anton/step_2.py
# Choose option 3
# Enter your URL
# Choose 'y' to download
# Check the 'downloaded_images' folder!
```

### Scrape Multiple URLs at Once
```bash
# Edit urls.txt with your URLs
python3 anton/batch_scraper.py
```

## Tips 💡

1. **Start Simple** - Try demo.py first to make sure everything works
2. **Be Respectful** - Don't overwhelm servers with too many requests
3. **Save Your Data** - Always say 'y' when asked to save
4. **Use HTML Reports** - They look professional and are easy to share
5. **Compare Results** - Use stats_viewer.py to track changes over time

## Troubleshooting 🔧

### "ModuleNotFoundError: No module named 'bs4'"
```bash
pip install beautifulsoup4
```

### "No analytics files found"
Run a scraper first to generate some data!

### URL doesn't work
Make sure it starts with `http://` or `https://`

## What to Try First 🎯

**Absolute beginners:** Start with `demo.py`
**Want quick results:** Use `step_1.py`
**Want full control:** Use `step_2.py` (interactive menu)
**Have many URLs:** Use `batch_scraper.py`
**Analyze results:** Use `stats_viewer.py`

## Help & Support 💬

All scripts have colorful output that guides you through the process.
Just follow the on-screen instructions!

---

**Now go scrape some websites! 🚀✨**

