# studyportal

For usage: 
1. Install requirements.txt file and run server at your local device. 
2. Thereafter, go to the home page at localhost:<port_number>/studapp/
3. For admin page go to localhost:<port_number>/admin/

-------------------------------------------------------------------------------------------------------------------------------------------
Presently, we've the papers for certain APL, CML, COL, ELL and MTL courses. More are to be soon updated - Besides, if anyone has any slides or tuts of any course and sem, either send it to Divyanshu/Mayank or upload it on the portal locally. Currently the workpattern is this, people contibute using the upload button, this dumps the file in media/document. using the admin website we add the papers from this folder. You can try yourself.
-------------------------------------------------------------------------------------------------------------------------------------------
We will work using python 2.7
and latest version of django that is django 1.11.1

ANYONE WHO WORKS ON THIS MAKE SURE YOU INSTALL THE REQUIREMENTS USING:-
pip install -r requirements.txt

superuser credentials
both username and password same as **youshouldknow**

TO-DO:
1. Find a cost-efficient platform to host this portal
2. **Build a REST API for this portal to allow remote access to the files and to allow upload/downloads remotely.** 
    In this, django_rest framework has been used. Presently, the rest functions are avaible at url "/studapp/rest/". Presently, it lists down the files for a given course code. Usage: 
    Go to url: /studapp/rest/<course_code>/
