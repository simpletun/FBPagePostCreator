#This will create a new generic Post object of type status that can be loaded through XD or manipulated with other scripts.  It starts with a basic template file that has the right structure, then changes values to make the post unique.
import json
import sys
import time

#look for a message passed in as a command line parameter and use if it is present.
if (len(sys.argv) > 1):
	strMessage = sys.argv[1]
else: 
	strMessage = "A Post Message Template"


json_data=open('271821786239046_STATUS_TEMPLATE.txt')

data = json.load(json_data)

json_data.close()

if (len(sys.argv) > 2):
	strConfigId = sys.argv[2]
	data["wt_external_config_id"] = strConfigId

#open file for writing
f = open('Status_Post_Template.txt', 'w')

#Grab the post object in an array to make referencing it easier
my_post = data["data"][0]

strPageId = "271821786239046"

strCreatedTime = time.strftime("%Y-%m-%dT%H:%M:%S") + "+0000"

#create a unique post id based on the current date/time
strPostId = time.strftime("%Y%m%d%H%M%S%u")



#run through and reset all ids with unique values from the new PostId
my_post["id"] = strPageId + "_" + strPostId

my_post["message"] = strMessage

#change action links to point to the new unique postid
my_post["actions"][0]["link"] = "http://www.facebook.com/271821786239046/posts/" + strPostId
my_post["actions"][1]["link"] = "http://www.facebook.com/271821786239046/posts/" + strPostId


#set created time and updated time with 
my_post["created_time"]=strCreatedTime
my_post["updated_time"]=strCreatedTime


#set the comment id and created_time
strCommentId = strPageId + "_" + strPostId + "_" + time.strftime("%d%H%M%S")
my_post["comments"]["data"][0]["id"] = strCommentId
my_post["comments"]["data"][0]["created_time"] = strCreatedTime

#set the all_comments values
my_post["all_comments"][0]["created_time"] = strCreatedTime
my_post["all_comments"][0]["id"] = strCommentId

#FIX INSIGHTS ID values
my_post_insights = my_post["insights"]["data"]

#iterate through all insights and add in the pageid and postid to the ID value
for insight in my_post_insights:
	insight["id"] = strPageId + "_" + strPostId + insight["id"]



#json.dumps writes into string format, removes all the u' and other json object formatting.
json_object = json.dumps(data)

#Write out object to output file with the correct "Stitched-together" format
#f.write("{\"data\":[")

f.write(json_object)

#f.write("]}")

f.close()

