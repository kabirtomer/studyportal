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
How to approve and disapprove requests?
Go to /studapp/approve and accept or reject each request
PS: You must be logged in to do that ;)  

Tracking: Tracking and Page hits are currently implemented in two ways:
1. Google Analytics - Currently, Google analytics is operational for **www.cse.iitd.ac.in/devclub/studyportal**
2. Admin Panel - Course Page hits can also be found from the admin panel. Go to the requisite course code and check the pagehits field :)
-----------------------------------------------------------------------------------------
API
/studapp/api/departments/ : would return all departments with their coursecodes
/studapp/api/departments?code=apl : would only return codes of apl
/studapp/api/course_codes/ : would return all course codes along with their minors, majors and others
/studapp/api/course_codes/?code=apl100 : would only return papers of apl100
/studapp/api/document/ : only post requests allowed to upload files.
						request.data must contain *coursecode*(like APL100), *type_exam*(minor1/minor2/major/QuantumBook), *document*(file)
						optionally it may also have, *sem*(1 or 2), *year*(2016-17), 
						

