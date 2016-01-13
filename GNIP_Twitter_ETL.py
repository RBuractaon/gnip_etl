# coding: utf-8
__author__ = "Richard Buractaon"
__license__ = "GPL"

import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
from acscsv import *
# unicode input
reload(sys)

def process_gnip(ROW):
    import pkg_resources
    try:
        __version__ = pkg_resources.require("gnacs")[0].version
    except pkg_resources.DistributionNotFound:
        __version__ = "N/A"
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    import codecs
    # needed only for the pretty-printing
    #import json as json_printer
    # use fastest option available for parsing
    try:
        import ujson as json
    except ImportError:
        try:
            import json
        except ImportError:
            import simplejson as json

    processing_obj = twitter_acs.TwacsCSV("|","","","","","","","","")

    for linenum, x in processing_obj.file_reader(json_string=ROW):
        row = []
        # postedTime - the time the action occurred
        try:
            row.append(x['postedTime'])
        except:
            row.append('')
        # id -  A unique IRI for the tweet. In more detail, "tag" is the scheme,
        #       "search.twitter.com" represents the domain for the scheme, and
        #       2005 is when the scheme was derived.
        try:
            row.append(x['id'])
        except:
            row.append('')
        # actor - An object representing the twitter user who tweeted. The Actor
        #         Object refers to a Twitter User, and contains all metadata
        #         relevant to that user.
        try:
            # Object Types - Article, Audio, Badge, Bookmark, Collection,
            #                Comment, Event, File, Group, Image, Note,
            #                Person, Place, Product, Question, Review,
            #                Service, Video
            row.append(x['actor']['objectType'])
        except:
            row.append('')
        # IRI for the twitter user
        try:
            id = x['actor']['id'].split(':')
            row.append(id[2])
        except:
            row.append('')
        # the user's name
        try:
            row.append(x['actor']['displayName'])
        except:
            row.append('')
        # the user's bio
        try:
            summary = x['actor']['summary'].replace('\t','<tab>')
            sum_oneline = ''.join(summary.splitlines())
            row.append(sum_oneline)
        except:
            row.append('')
        # the user account's creation date
        try:
            row.append(x['actor']['postedTime'])
        except:
            row.append('')
        # the user's screen name
        try:
            row.append(x['actor']['preferredUsername'])
        except:
            row.append('')
        # the user's default language
        try:
            row.append(x['actor']['languages'])
        except:
            row.append('')
        # the user's timezone
        try:
            row.append(x['actor']['twitterTimeZone'])
        except:
            row.append('')
        try:
            row.append(x['actor']['utcOffset'])
        except:
            row.append('')
        # number of people the user follows
        try:
            row.append(x['actor']['friendsCount'])
        except:
            row.append('')
        # number of followers the user has
        try:
            row.append(x['actor']['followersCount'])
        except:
            row.append('')
        # number of lists the user is in
        try:
            row.append(x['actor']['listedCount'])
        except:
            row.append('')
        # number of tweets the user has tweeted
        try:
            row.append(x['actor']['statusesCount'])
        except:
            row.append('')
        # number of favorties the user has
        try:
            row.append(x['actor']['favoritesCount'])
        except:
            row.append('')
        # verb -  the type of action being taken by the user
        #         post, share, delete
        try:
            row.append(x['verb'])
        except:
            row.append('')
        # generator - an object representing the utility used to post the
        #             Tweet. This will contain the name "displayName" and
        #             a "link" for the source generating the Tweet.
        try:
            row.append(x['generator']['displayName'])
        except:
            row.append('')
        # provider - provider of the activity
        try:
            row.append(x['provider']['objectType'])
            row.append(x['provider']['displayName'])
        except:
            row.append('')
            row.append('')
        # inReplyTo - indicates the tweet being replied to
        try:
            row.append(x['inReplyTo'])
        except:
            row.append('')
        # location - twitter place where the the tweet was created
        try:
            row.append(x['location']['objectType'])
        except:
            row.append('')
        try:
            row.append(x['location']['displayName'])
        except:
            row.append('')
        try:
            row.append(x['location']['name'])
        except:
            row.append('')
        try:
            row.append(x['location']['country_code'])
        except:
            row.append('')
        try:
            row.append(x['location']['twitter_country_code'])
        except:
            row.append('')
        try:
            row.append(x['location']['geo'])
        except:
            row.append('')
        try:
            address = x['location']['streetAddress'].replace('\t',' ')
            addr_oneline = ''.join(address.splitlines())
            row.append(addr_oneline)
        except:
            row.append('')
        # geo - point location where the tweet was created
        try:
            row.append(x['geo']['type'])
            coords = x['geo']['coordinates']
            row.append(coords)
            row.append(coords[0])
            row.append(coords[1])
        except:
            row.append('')
            row.append('')
            row.append('')
            row.append('')
        # twitter_entities - lists of urls, mentions, and hashtags
        try:
            row.append(x['twitter_entities']['hashtags'])
        except:
            row.append('')
        try:
            row.append(x['twitter_entities']['trends'])
        except:
            row.append('')
        try:
            row.append(x['twitter_entities']['urls'])
        except:
            row.append('')
        try:
            row.append(x['twitter_entities']['user_mentions'])
        except:
            row.append('')
        try:
            row.append(x['twitter_entities']['symbols'])
        except:
            row.append('')
        try:
            row.append(x['twitter_entities']['media'])
        except:
            row.append('')
        # twitter_extended_entities - native data format containing "Media"
        try:
            row.append(x['twitter_extended_entities']['media'])
        except:
            row.append('')
        # link - a permalink for the tweet
        try:
            row.append(x['link'])
        except:
            row.append('')
        # body - the tweet text
        try:
            body = x['body'].replace('\t','<tab>')
            body_oneline = ''.join(body.splitlines())
            row.append(body_oneline)
        except:
            row.append('')
        # objectType
        try:
            row.append(x['objectType'])
        except:
            row.append('')
        # object - an object representing tweet being posted or shared
        #          original tweets = "note" object
        #          retweets = "activity" object
        try:
            row.append(x['object']['objectType'])
            row.append(x['object']['id'])
            row.append(x['object']['postedTime'])
        except:
            row.append('')
            row.append('')
            row.append('')
        # retweetCount - number of times tweet was re-tweeted
        try:
            row.append(x['retweetCount'])
        except:
            row.append('')
        # Languages - twitter, gnip, and other language identifiers
        try:
            row.append(x['twitter_lang'])
        except:
            row.append('')
        try:
            row.append(x['gnip']['language'])
        except:
            row.append('')
        # favoritesCount - number of times this was favorited
        try:
            row.append(x['favoritesCount'])
        except:
            row.append('')
        # klout_score - retrieved klout score by gnip
        try:
            row.append(x['gnip']['klout_score'])
        except:
            row.append('')
        # matching_rules
        try:
            row.append(x['gnip']['matching_rules'])
        except:
            row.append('')
        # gnip expanded urls
        try:
            row.append(x['gnip']['urls'])
        except:
            row.append('')
        unicode_row = []
        for item in row:
            if isinstance(item, unicode):
                unicode_row.append(unicode(' ').join(item.split()))
            else:
                unicode_row.append(unicode(' ').join(unicode(item).split()))
        return unicode('\t').join(unicode_row)

# Save Flattened File to HDFS for Hive/Impala Table Import
raw = sc.textFile('/data/raw/GNIP/tw/*/*/*/*.gz')
gnip = raw.map(lambda x: process_gnip(x)).saveAsTextFile('/user/rburactaon/gnip_flattened')
