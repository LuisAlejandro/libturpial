# -*- coding: utf-8 -*-

"""A list containing all show media services"""

<<<<<<< HEAD
from libturpial.lib.services.media.preview.imgur import ImgurMediaContent
from libturpial.lib.services.media.preview.lockerz import LockerzMediaContent
from libturpial.lib.services.media.preview.twitpic import TwitpicMediaContent
from libturpial.lib.services.media.preview.yfrog import YfrogMediaContent
from libturpial.lib.services.media.preview.pictwitter import PicTwitterMediaContent
from libturpial.lib.services.media.preview.viame import ViameMediaContent
from libturpial.lib.services.media.preview.flickr import FlickrMediaContent
from libturpial.lib.services.media.preview.instagram import InstagramMediaContent
=======
from .imgur import ImgurMediaContent
from .lockerz import LockerzMediaContent
from .twitpic import TwitpicMediaContent
from .yfrog import YfrogMediaContent
from .pictwitter import PicTwitterMediaContent
from .viame import ViameMediaContent
from .flickr import FlickrMediaContent
>>>>>>> milmazz/fix_bug_33

PREVIEW_MEDIA_SERVICES = {
    'imgur': ImgurMediaContent(),
    'lockerz': LockerzMediaContent(),
    'twitpic': TwitpicMediaContent(),
    'yfrog': YfrogMediaContent(),
    'pic.twitter.com': PicTwitterMediaContent(),
    'via.me': ViameMediaContent(),
    'flic.kr': FlickrMediaContent(),
    'instragram': InstagramMediaContent(),
}
