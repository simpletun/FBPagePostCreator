import json

#take input from trimmed file
json_data=open('Other_Post_Type.txt')

#serialize json object
data = json.load(json_data)

json_data.close()

#open file for writing
f = open('Other_Post_Type-OUT.txt', 'w')

#create json my_object out of the first post object in the json post object array
my_post = data["data"][0]

#start renaming/transforming
for i in range(1,1000):
	#create new comment template dictionary
	my_comment_template = {}
	#create new from sub dictionary
	my_from = {}
	#set from dictionary values
	my_from["name"] = "Adam Olsen"
	my_from["id"] = "1440017152"
	#append from sub dict to comment template dict
	my_comment_template["from"] = my_from
	#set other comment values
	my_comment_template["like_count"] = str(i)
	my_comment_template["can_remove"] = "True"
	my_comment_template["created_time"] = "2012-07-05T18:55:11+" + str(1000 - i).zfill(4)
	my_comment_template["message"] = "A Test Comment Number -> " + str(i)
	my_comment_template["id"] = "271821786239046_328523953902162_727265" + str(i)
	my_comment_template["user_likes"] = "False"
	#append comment template dict to comments section of post object
	my_post["all_comments"].append(my_comment_template)

#json.dumps writes into string format, removes all the u' and other json object formatting.
json_object = json.dumps(my_post)

#Write out object to output file with the correct "Stitched-together" format
f.write("{\"data\":[")

f.write(json_object)

f.write("]}")

f.close()

