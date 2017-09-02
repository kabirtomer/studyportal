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

Before making ANY CHANGE in the REPO:
**Make sure to commit changes from the vm and then make any changes. And after making any changes on your local machine, please commit the changes and pull them in the vm.**

superuser credentials
both username and password same as **youshouldknow**

-----------------------------------------------------------------------------------------
How to login to approve and disapprove requests?
Login:
	Go to /studapp/userlogin and enter the credentials
Logout:
	Go to /studapp/userlogout
-----------------------------------------------------------------------------------------
How to approve and disapprove requests?
Go to /studapp/approve and accept or reject each request
------
Explicit buttons not added for login, logout and approval so that the general mass remains in ignorance
