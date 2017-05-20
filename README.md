# studyportal

For usage: 
1. Install requirements.txt file and run server at your local device. 
2. Thereafter, go to the home page at localhost:<port_number>/studapp/
3. For admin page go to localhost:<port_number>/admin/

-------------------------------------------------------------------------------------------------------------------------------------------
I've added the actual upload feature which adds the files to media/documents/. I've also reworked the models such that the minors and majors and other displays the actual  files. I've added some sample files for APL100, go browse them using the website. Currently the workpattern is this, people contibute using the upload button, this dumps the file in media/document. using the admin website we add the papers from this folder. You can try yourself.
-------------------------------------------------------------------------------------------------------------------------------------------
We will work using python 2.7
and latest version of django that is django 1.11.1

ANYONE WHO WORKS ON THIS MAKE SURE YOU INSTALL THE REQUIREMENTS USING:-
pip install -r requirements.txt

superuser credentials
both username and password same as iitddevclub

The basic structure of the repo is completed(I(Mayank) used the most basic UI)
	*Now we have to add the upload feature
	*Provide a better UI
	*Think about the storage of files

