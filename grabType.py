#This script will get an entire response for posts from facebook, then take copy all posts of a designated type out to a file.
#It will also output some stats to standard out to give you an idea of how many of those posts have various parameters.
import json


#open file for writing
json_data = open('FacebookPosts_40796308305_20120731_05-45-54.txt')

data = json.load(json_data)

#open file for output
f = open("picturePosts.txt", 'w')

my_swf_posts = []

pics = 0
names = 0
sources = 0
links = 0
messages = 0
icons = 0
descriptions = 0
stories = 0
captions = 0

i = 0
#Grab the post object in an array to make referencing it easier
for post in data["data"]:

    if post["type"] == "photo":
        my_swf_posts.append(post)
        i += 1

    if "picture" in post:
        pics += 1

    if "name" in post:
        names += 1

    if "source" in post:
        sources += 1

    if "link" in post:
        links += 1

    if "message" in post:
        messages += 1

    if "icon" in post:
        icons += 1

    if "description" in post:
        descriptions += 1

    if "story" in post:
        stories += 1

    if "caption" in post:
        captions += 1


print "I have this many pictures --> " + str(pics)
print "I have this many names --> " + str(names)
print "I have this many sources --> " + str(sources)
print "I have this many links --> " + str(links)
print "I have this many messages --> " + str(messages)
print "I have this many icons --> " + str(icons)
print "I have this many descriptions --> " + str(descriptions)
print "I have this many stories --> " + str(stories)
print "I have this many captions --> " + str(captions)


#json.dumps writes into string format, removes all the u' and other json object formatting.
json_object = json.dumps(my_swf_posts)

#Write out object to file
f.write(json_object)

#close file handle
f.close()
