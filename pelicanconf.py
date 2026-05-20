AUTHOR = 'Mike Holzinger'
SITENAME = 'Mike Holzinger'
#SITEURL = 'http://cipherpop.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
SOCIAL= (('LinkedIn', 'http://www.linkedin.com/in/mikeholzinger/'),
         ('GitHub', 'https://github.com/mholzinger?tab=repositories'),
         ('GitLab', 'https://gitlab.com/users/mholzinger/projects'))

# Sidebar "links" widget. Resume is in top nav, so dropped here.
LINKS = (('Games on itch.io', 'https://paisleyboxers.itch.io'),
         ('Overlay Editor',   'https://intellivision-overlay-editor.fly.dev/'))

DEFAULT_PAGINATION = 10

# Use the local theme (notmyidea + gitlab icon + banner-stripped footer).
import os
THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'theme')

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Pin top-nav order explicitly. Disable auto menus so pages don't duplicate.
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('Resume',      '/Resume.pdf'),
    ('Development', '/pages/development.html'),
    ('Bio',         '/pages/bio.html'),
    ('Game Design', '/pages/game-design.html'),
    ('Archive',     '/pages/archive.html'),
)

PLUGINS = [
    # ...
    'pelican_fontawesome'
    # ...
]

# Publish Resume.pdf at the site root (so /Resume.pdf works) instead of /images/Resume.pdf.
EXTRA_PATH_METADATA = {
    'images/Resume.pdf': {'path': 'Resume.pdf'},
}