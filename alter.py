import json
from pprint import pprint

#take input from trimmed file
json_data=open('271821786239046.txt')

#serialize json object
data = json.load(json_data)

json_data.close()

#open file for writing
f = open('271821786239046-OUT.txt', 'w')

#create json my_object out of the first post object in the json post object array
my_objects = data["data"]

#start renaming/transforming
for i in range(2,1000):
	#create new comment template dictionary
	my_comment_template = {}
	#create new from sub dictionary
	my_from = {}
	#set from dictionary values
	my_from["name"] = "Adam Olsen"
	my_from["id"] = "1457951151"
	#append from sub dict to comment template dict
	my_comment_template["from"] = my_from
	#set other comment values
	my_comment_template["like_count"] = str(i)
	my_comment_template["can_remove"] = "True"
	my_comment_template["created_time"] = "2012-06-30T17:31:02+0000"
	my_comment_template["message"] = "Another Message -> " + str(i)
	my_comment_template["id"] = "40796308305_10151754715488306_2373811" + str(i + 3)
	my_comment_template["user_likes"] = "False"
	#append comment template dict to comments section of post object
	my_object["all_comments"].append(my_comment_template)

#json.dumps writes into string format, removes all the u' and other json object formatting.
json_object = json.dumps(my_object)

#Write out object to output file with the correct "Stitched-together" format
f.write("{\"data\":[")

f.write(json_object)

f.write("]}")

f.close()

