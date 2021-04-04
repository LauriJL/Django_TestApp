"""import string
import random

from django.utils.text import slugify

#Random string generator
def rndm_str_gen(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    #Checks if slug exists. If not, creates new slug from title
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    classInstance = instance.__class__

    qs_exists = classInstance.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=rndm_str_gen(size=4)
        )

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug"""
