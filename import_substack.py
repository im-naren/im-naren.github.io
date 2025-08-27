#!/usr/bin/env python3
"""
Substack to Jekyll Post Converter

This script helps convert Substack articles to Jekyll posts.

Usage:
1. Copy your Substack article content
2. Run this script and paste the content
3. It will create a properly formatted Jekyll post

Author: Narendra Dubey
"""

import re
import datetime
from pathlib import Path

def clean_content(content):
    """Clean and format content for Jekyll"""
    # Remove extra whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)
    
    # Fix common Substack formatting
    content = content.replace('**', '**')  # Bold text
    content = content.replace('*', '*')    # Italic text
    
    return content.strip()

def create_jekyll_post(title, date, content, categories=None):
    """Create a Jekyll post file"""
    if categories is None:
        categories = ["engineering"]
    
    # Create filename
    date_str = date.strftime("%Y-%m-%d")
    filename = f"{date_str}-{title.lower().replace(' ', '-').replace(',', '').replace('?', '').replace('!', '')}.md"
    filename = re.sub(r'[^a-zA-Z0-9\-.]', '', filename)
    
    # Create frontmatter
    frontmatter = f"""---
layout: post
title: "{title}"
date: {date.strftime("%Y-%m-%d %H:%M:%S %z")}
categories: {categories}
excerpt: "{content[:150].replace('"', '\\"')}..."
---

"""
    
    # Full post content
    post_content = frontmatter + content
    
    # Write to _posts directory
    posts_dir = Path("_posts")
    posts_dir.mkdir(exist_ok=True)
    
    post_path = posts_dir / filename
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(post_content)
    
    print(f"✅ Created post: {filename}")
    return post_path

def main():
    print("🚀 Substack to Jekyll Converter")
    print("================================")
    
    title = input("📝 Enter post title: ")
    
    # Get date
    date_input = input("📅 Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date_input:
        try:
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Using today.")
            date = datetime.datetime.now()
    else:
        date = datetime.datetime.now()
    
    # Get categories
    categories_input = input("🏷️  Enter categories (comma-separated) or press Enter for 'engineering': ")
    if categories_input:
        categories = [cat.strip() for cat in categories_input.split(',')]
    else:
        categories = ["engineering"]
    
    print("\n📋 Paste your article content below. Press Ctrl+D (Unix) or Ctrl+Z (Windows) when done:")
    print("-" * 50)
    
    # Read content from stdin
    content_lines = []
    try:
        while True:
            line = input()
            content_lines.append(line)
    except EOFError:
        pass
    
    content = '\n'.join(content_lines)
    content = clean_content(content)
    
    if not content:
        print("❌ No content provided!")
        return
    
    # Create the post
    post_path = create_jekyll_post(title, date, content, categories)
    
    print(f"\n🎉 Post created successfully!")
    print(f"📁 File: {post_path}")
    print("\n💡 Next steps:")
    print("1. Review the generated file")
    print("2. Add any missing formatting")
    print("3. Commit and push to deploy!")

if __name__ == "__main__":
    main()
