from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

L = instaloader.Instaloader()

# posts = instaloader.Profile.from_username(L.context, "loker.surabaya.sidoarjo.gresik").get_posts()

# SINCE = datetime(2020, 12, 23)
# UNTIL = datetime(2020, 12, 22)

# for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
#     print(post.date)
#     L.download_post(post, "instagram")


posts = instaloader.Hashtag.from_name(L.context, 'lowongankerja').get_posts()

users = set()

rr = 0
for post in posts:
    if not post.owner_profile in users:
        # L.download_post(post, '#loker')
        users.add(post.owner_profile)
        print (rr)
    elif rr == 10:
        break
    else:
        print("{} from {} skipped.".format(post, post.owner_profile))
    rr += 1
    
print (users)


# from instaloader import Instaloader, Profile

# PROFILE = ...        # profile to download from
# X_percentage = 10    # percentage of posts that should be downloaded

# L = Instaloader()

# posts = instaloader.Hashtag.from_name(L.context, 'loker')
# # profile = Profile.from_username(L.context, PROFILE)
# posts_sorted_by_likes = sorted(posts.get_posts(),
#                                key=lambda p: p.likes + p.comments,
#                                reverse=True)
# rr = 1
# for post in islice(posts_sorted_by_likes):
   
#     if rr == 100:
#         break
#     else:    
#         print (post.owner_profile)
#         users.add(post.owner_profile)
#     rr += 1
# print (users)