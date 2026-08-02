# Jinja CMS

Content management system for a blog, written with Python and Jinja.

## Usage

### File Structure

Each page has a folder under pages, with three files:

- `front.png`, the front of a cup sleeve
- `back.png`, the back of a cup sleeve
- `info.json`, JSON document with the following keys: `location`, `website`, `approxDate`, `title`, `caption`

### Running

#### Initial Setup

- `python3 -m venv .venv`
- `. .venv/bin/activate`
- `pip install -r requirements.txt`

#### After Setup

- `. .venv/bin/activate`
- `python3 site_generator.py`

This will generate a list of HTML files with the names of the folders under the `pages` directory, with the images and information contained in that folder.