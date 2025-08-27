#!/usr/bin/env python3
"""
Substack → Jekyll importer (single-run, one-by-one or batch)

- Input: list of Substack article URLs or a single URL
- Output: _posts/YYYY-MM-DD-slug.md with front matter, markdown body
- Also downloads images to assets/images/posts/<slug>/ and rewrites links

Dependencies (install once):
  pip install requests beautifulsoup4 readability-lxml markdownify python-slugify python-dateutil

Usage:
  python3 scripts/substack_to_jekyll.py --url <ARTICLE_URL>
  python3 scripts/substack_to_jekyll.py --file urls.txt
"""
from __future__ import annotations
import argparse
import os
import re
import sys
import time
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from readability import Document
from markdownify import markdownify as md
from slugify import slugify
from dateutil import parser as dateparser

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"
ASSETS_DIR = ROOT / "assets" / "images" / "posts"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
}


def fetch(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    return resp.text


def extract(html: str) -> dict:
    # Use Readability to get main content
    doc = Document(html)
    title = doc.short_title().strip() if doc.short_title() else None
    content_html = doc.summary()

    soup = BeautifulSoup(html, "html.parser")
    # Title fallbacks
    if not title:
        if soup.title and soup.title.string:
            title = soup.title.string.strip()
    ogt = soup.find("meta", attrs={"property": "og:title"})
    if ogt and ogt.get("content"):
        title = ogt["content"].strip()

    # Date detection
    pub_dt = None
    ogd = soup.find("meta", attrs={"property": "article:published_time"})
    if ogd and ogd.get("content"):
        try:
            pub_dt = dateparser.parse(ogd["content"])  # ISO
        except Exception:
            pub_dt = None
    if not pub_dt:
        # Look for time tag
        t = soup.find("time")
        if t and (t.get("datetime") or t.text):
            try:
                pub_dt = dateparser.parse(t.get("datetime") or t.text)
            except Exception:
                pass

    return {
        "title": title or "Untitled",
        "content_html": content_html,
        "raw_soup": soup,
        "published_at": pub_dt,
    }


def download_images(content_html: str, slug: str) -> tuple[str, list[str]]:
    soup = BeautifulSoup(content_html, "html.parser")
    img_dir = ASSETS_DIR / slug
    img_dir.mkdir(parents=True, exist_ok=True)

    downloaded = []
    for img in soup.find_all("img"):
        src = img.get("src")
        if not src or src.startswith("data:"):
            continue
        try:
            r = requests.get(src, headers=HEADERS, timeout=30)
            if r.status_code == 200 and r.content:
                ext = os.path.splitext(urlparse(src).path)[1] or ".jpg"
                fname = f"img_{len(downloaded)+1}{ext}"
                fpath = img_dir / fname
                with open(fpath, "wb") as f:
                    f.write(r.content)
                # rewrite src to local path
                rel = f"/assets/images/posts/{slug}/{fname}"
                img["src"] = rel
                downloaded.append(rel)
        except Exception:
            continue
    return str(soup), downloaded


def html_to_markdown(html: str) -> str:
    # Convert to Markdown, keep links and code blocks reasonably
    md_text = md(html, heading_style="ATX", strip=['a'])
    # Normalize excessive blank lines
    md_text = re.sub(r"\n{3,}", "\n\n", md_text).strip() + "\n"
    return md_text


def write_post(title: str, date_obj, markdown: str, url: str) -> Path:
    POSTS_DIR.mkdir(exist_ok=True)
    slug = slugify(title)[:80] or f"post-{int(time.time())}"
    date_part = (date_obj or dateparser.parse("today")).strftime("%Y-%m-%d")
    fname = f"{date_part}-{slug}.md"
    path = POSTS_DIR / fname

    excerpt = re.sub(r"\s+", " ", markdown.strip())[:180].replace('"', '\\"')

    fm = (
        f"---\n"
        f"layout: post\n"
        f"title: \"{title}\"\n"
        f"date: {date_part} 10:00:00 +0530\n"
        f"categories: [engineering]\n"
        f"original_url: \"{url}\"\n"
        f"excerpt: \"{excerpt}...\"\n"
        f"---\n\n"
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(fm)
        f.write(markdown)
    return path


def import_one(url: str) -> Path:
    html = fetch(url)
    meta = extract(html)
    # images
    rewritten_html, _ = download_images(meta["content_html"], slug=slugify(meta["title"])[:80])
    markdown = html_to_markdown(rewritten_html)
    post_path = write_post(meta["title"], meta["published_at"], markdown, url)
    return post_path


def main():
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group(required=True)
    g.add_argument("--url", help="Single Substack article URL")
    g.add_argument("--file", help="Text file with one URL per line")
    args = parser.parse_args()

    created = []
    if args.url:
        print(f"Importing: {args.url}")
        created.append(import_one(args.url))
    else:
        with open(args.file, "r", encoding="utf-8") as f:
            for line in f:
                url = line.strip()
                if not url or url.startswith("#"):
                    continue
                try:
                    print(f"Importing: {url}")
                    created.append(import_one(url))
                except Exception as e:
                    print(f"Failed: {url} -> {e}")
    print("\nCreated posts:")
    for p in created:
        print(f" - {p.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
