import string

# Problem 64: Write a function make_slug that takes a name converts it into a slug. A slug is a string where spaces
# and special characters are replaced by a hyphen, typically used to create blog post URL from post title. It should
# also make sure there are no more than one hyphen in any place and there are no hyphens at the biginning and end
# of the slug.
def make_slug(name):
    slug = ''
    name = name.replace(' ', '-')
    hyphen = False
    for letter in name:
        if letter in string.ascii_letters:
            slug = slug + letter
            hyphen = False
        elif letter in string.punctuation:
            if not hyphen:
                slug = slug + '-'
                hyphen = True
    if slug.startswith('-'):
        slug = slug[1:]
    if slug.endswith('-'):
        slug = slug[:-1]
    return slug