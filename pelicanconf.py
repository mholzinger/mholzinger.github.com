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

# Social Widget
LINKS = (('Resume', 'Resume.pdf'),
         ('',''))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGINS = [
    # ...
    'pelican_fontawesome'
    # ...
]