# Logs time for specific task in Zoho

## It logs 8 hours for each weekday in specific month

### **Parameters

*month=, Month for that you want to log time (1,2,3,4,5,6,7,8,9,10,11,12)
*days_to_skip=, Days to skip (days from 1 to 31)
*notes=, Notes added in time logged

### **Examples
*month=3 days_to_skip=1,5,6 notes=development
*month=5 notes=development
*month=5 days_to_skip=2,7

### Configuration

###### Generate Auth Token - Browser Mode

Log In Zoho
Go to: https://accounts.zoho.com/apiauthtoken/create?SCOPE=ZohoCreator/creatorapi
authtoken is in response

###### User ID
you can see user_id when you click profile icon (image) in top right corner

###### Project ID, Task ID
when you navigate to specific task you can get
from url

example: https://projects.zoho.com/portal/symphonyis#taskdetail/965106000000101027/965106000000104001/965106000000122487
*project_id=965106000000101027
*task_id=965106000000122487


Populate zoho.conf with authtoken, user_id, portal_id, project_id, task_id,
