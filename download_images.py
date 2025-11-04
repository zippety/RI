"""
Download Reiki images from free sources
Downloads Gassho, Symbols, and Chakra images from direct URLs
"""

import os
import requests
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Direct image URLs (free to use, no attribution required)
# These are placeholder URLs - will need actual free image URLs
# For now, using Pixabay direct download URLs (free commercial use)

IMAGES_TO_DOWNLOAD = {
    "Gassho": [
        # These will be actual download URLs from Pixabay or other free sources
        # For now, creating structure for manual download
    ],
    "Symbols": [
        # Reiki symbol images from free sources
    ],
    "Chakras": [
        # Chakra diagram images from free sources
    ]
}

def download_image(url, save_path):
    """Download an image from URL and save to path"""
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, timeout=30, allow_redirects=True, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response.raise_for_status()
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save image
        with open(save_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded: {save_path} ({len(response.content)} bytes)")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def download_from_pixabay(query, save_folder, prefix, count=3):
    """Download images from Pixabay using their API"""
    # Note: Pixabay API requires an API key
    # For now, we'll provide manual download instructions
    print(f"\nTo download {query} images from Pixabay:")
    print(f"1. Go to: https://pixabay.com/images/search/{query.replace(' ', '%20')}/")
    print(f"2. Filter by: Free images")
    print(f"3. Download images and save to: {save_folder}/")
    print(f"4. Name them: {prefix}_1.png, {prefix}_2.png, etc.")
    return 0

def main():
    """Main download function"""
    print("=" * 60)
    print("RI Reiki Resources - Image Downloader")
    print("=" * 60)
    print("\nNOTE: Automated downloading requires API keys or direct URLs.")
    print("For now, please use manual download method:")
    print("\n1. See download guides in each folder:")
    print("   - 01_Images/Gassho/DOWNLOAD_GUIDE.md")
    print("   - 01_Images/Symbols/DOWNLOAD_GUIDE.md")
    print("   - 01_Images/Chakras/ (create guide if needed)")
    print("\n2. Or use the quick links below:")
    print("\nGassho Images:")
    print("  - Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Gassho")
    print("  - Pixabay: https://pixabay.com/images/search/prayer%20hands/")
    print("\nReiki Symbols:")
    print("  - Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Reiki_symbols")
    print("\nChakra Diagrams:")
    print("  - Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Chakras")
    print("  - Pixabay: https://pixabay.com/images/search/chakra/")
    print("\nAfter downloading manually:")
    print("1. Place images in appropriate folders")
    print("2. Update README.md files with attribution")
    print("3. Commit and push to GitHub")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nDownload interrupted by user")
    except Exception as e:
        print(f"\n\nError: {e}")
