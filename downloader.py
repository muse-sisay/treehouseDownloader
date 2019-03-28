from selenium import webdriver
from bs4 import BeautifulSoup
import subprocess
import youtube_dl
import os

# aria2c options
EXTERNAL_DL = "  --external-downloader aria2c --external-downloader-args '-j1 -x16 -s16 -k1M' "

# contents file


# path where all the folder will be downloaded
courses_folder_path = ''
os.chdir( courses_folder_path )
email = ''
password = ''

def create_folder ( path ):
	if not os.path.exists(path):
		os.mkdir( path)
	os.chdir( path)

def login ( driver ):

	url_signin = 'https://teamtreehouse.com/signin'
	driver.get(url_signin)

	email_input = driver.find_element_by_xpath('//*[@id="user_session_email"]')
	email_input.send_keys(email)

	password_input = driver.find_element_by_xpath('//*[@id="user_session_password"]')
	password_input.send_keys(password)

	signin_button = driver.find_element_by_xpath('/html/body/main/div/div/div/div/div/form/button')
	signin_button.click()

url_course = input('Track url : ')

driver = webdriver.Chrome(executable_path ='/usr/local/bin/chromedriver')

login(driver)


driver.get(url_course)

# get SOUP OBJECT
soup = BeautifulSoup(driver.page_source , 'lxml')

# to get to the title
course_title = soup.find('div' , id='syllabus-title').find('h1')
course_title = course_title.getText().strip()

create_folder( course_title)
conntent_md = open( "content.md" ,'w+')
print ( course_title )
conntent_md.write( course_title +'\n' )

# dont know what to name it is found under the course_title
course_title_under = soup.find('div' , id='syllabus-title').find('h2')
course_title_under = course_title_under.getText().strip()
print ( course_title_under) 
conntent_md.write( course_title_under +'\n' )

#  course description - from the 'about this course'section
about_course = soup.find('div' , id='syllabus-description').find_all('p')[1]
print( about_course.getText() )
conntent_md.write( about_course.text +'\n' )


# course checklist - from the 'about this course' section
course_check_list = soup.find('div' , id='syllabus-description' ).find_all('li')
for li in course_check_list :
	print ( li.getText() )
	conntent_md.write( "\t-" + li.getText()  +'\n')

# gets ( all ) individual chapters
course_stage = soup.find('div' , id ='syllabus-stages')
course_chapters = course_stage.find_all( 'div' , class_= 'featurette')

chapter_no = 0
video_no = 0

for chapter in course_chapters :

	#  getting chapter title
	chapter_title = chapter.find('h2')
	chapter_title = str(chapter_no) + '. ' + chapter_title.getText().strip()
	create_folder( chapter_title )

	# getting chapter description
	chapter_description = chapter.find_all('p')[1]
	chapter_description = chapter_description.getText()

	print ( "\tCHAPTER : " + chapter_title )
	conntent_md.write( "\tCHAPTER : " + chapter_title  +'\n' )
	print ( "\tDescription : " +chapter_description  )
	conntent_md.write( "\tDescription : " +chapter_description +'\n' )

	# getting the chapter videos
	chapter_videos = chapter.find('ul' , class_='steps-list')
	chapter_videos = chapter_videos.find_all('a')

	

	video_links = []

	for video in chapter_videos :

		p_tag = video.find('p')

		if ( p_tag == None ):
			pass
		elif ( ':' in p_tag.getText() ) :
			# getting video title
		# if ( ':' in ( video.find('p').getText() )  ):
			video_title = video.find('h4')
			video_link = video['href']
			video_link = 'https://teamtreehouse.com'+ video_link
			video_links.append( video_link )
			print (" \t+ " +  video_title.getText() )
			conntent_md.write( " \t+ " +  video_title.getText() +'\n')

	for video_link in video_links :

		driver.get(video_link)
		soup = BeautifulSoup(driver.page_source , 'lxml')

		video_meta = soup.find('div' , id ='video-meta')

		video_title = video_meta.find('h1')
		video_description = video_meta.find('p')

		video_link = soup.find('source', type = 'video/webm')['src']
		output = " -o '{} - {}.%(ext)s' ".format(video_no , video_title.getText().strip())

		os.system( 'youtube-dl --no-check-certificate' + output + ' ' + video_link + EXTERNAL_DL)
		# os.system( "aria2c '-j1 -x16 -s16 -k1M' ' + output + ' " + video_link )

		video_no +=1
	
	# revert back to the parent folder ( course folder )
	os.chdir( '..')
	chapter_no +=1 





















