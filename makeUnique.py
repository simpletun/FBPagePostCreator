#This script is designed to take input template files and transform them to create posts with unique identifiers, messages, and timestamps.
#This script will create a new generic Post object of type status that can be loaded through XD or manipulated with other scripts.  

#Command line options: 
#	1 - config id 
#	2 - input file name
#	3 - duplicate comment boolean
#	4 - message 
# All are optional.  If they are not passed in, the default parameters in the else statements below will be used.

import json
import sys
import time
import re

#Set my PageID
strPageId = "271821786239046"	#This could be passed in as another command line parameter if necessary

#set my timestamp using UTC time, and format.  
strTimeStamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) 

#get refreshtime unix timestamp
refreshTime = int(time.time()) * 1000

#see if a file name is passed in at the command line, else open the template
if (len(sys.argv) > 2):
	strFileName = sys.argv[2]
	json_data=open(strFileName)
else:
	#open file for writing
	json_data=open('271821786239046_STATUS_TEMPLATE.txt')
	
data = json.load(json_data)

#see if there's a config id
if (len(sys.argv) > 1):
	strConfigId = sys.argv[1]
	data["wt_external_config_id"] = strConfigId
else: 
	data["wt_external_config_id"] = "1023"

data["wt_account_id"] = "10314"


#look for duplicate comment flag
if (len(sys.argv) > 3):
	dupCommentFlag = sys.argv[3]
else: 
	dupCommentFlag = 'False'
	
	
#look for a message passed in as a command line parameter and use if it is present.
if (len(sys.argv) > 4):
	strMessage = sys.argv[4]
else: 
	strMessage = "A new post at " + strTimeStamp 


	
json_data.close()


#open file for output
f = open(strPageId + ".txt", 'w')

#Grab the post object in an array to make referencing it easier
my_post = data["data"][0]

#Set time and page variables
my_post["refreshed_time"] = refreshTime
my_post["accountId"] = strPageId

strCreatedTime = strTimeStamp + "+0000"

#create a unique post id based on the current date/time
strPostId = time.strftime("%Y%m%d%H%M%S%u")

#run through and reset all ids with unique values from the new PostId
my_post["id"] = strPageId + "_" + strPostId

my_post["message"] = strMessage

#change action links to point to the new unique postid
my_post["actions"][0]["link"] = "http://www.facebook.com/" + strPageId + "/posts/" + strPostId
my_post["actions"][1]["link"] = "http://www.facebook.com/" + strPageId + "/posts/" + strPostId


#set created time and updated time with 
my_post["created_time"]=strCreatedTime
my_post["updated_time"]=strCreatedTime


#iterate through comments and set the comment id and created_time
strCommentId = strPageId + "_" + strPostId + "_" + "123456"
i = 1

#FIX COMMENTS
for this_comment in my_post["comments"]["data"]:
	#If we're creating duplicate comments, don't make the comment ID unique, else do
	if dupCommentFlag == 'True': 
		this_comment["id"] = strCommentId
	else: 
		this_comment["id"] = strCommentId + str(i)		
	this_comment["created_time"] = strTimeStamp + "+0000"
	i += 1

i = 1
#FIX ALL_COMMENTS
for this_comment in my_post["all_comments"]:
	if dupCommentFlag == 'True': 
		this_comment["id"] = strCommentId
	else: 
		this_comment["id"] = strCommentId + str(i)
	this_comment["created_time"] = strTimeStamp + "+0000"
	i += 1


#FIX INSIGHTS ID VALUES
my_post_insights = my_post["insights"]["data"]

#Use regular expression search and replace to fix the insight id values

#first set my regex pattern and the new id to replace it with
p = re.compile('\d+_\d+')
newInsightPP = strPageId + "_" + strPostId

#next iterate through the insights and replace the page_post part of the id with the new page_post
for insight in my_post_insights:
	 insight["id"] = p.sub(newInsightPP, insight["id"])
	


#json.dumps writes into string format, removes all the u' and other json object formatting.
json_object = json.dumps(data)

#Write out object to file
f.write(json_object)

#close file handle
f.close()

