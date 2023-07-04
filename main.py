import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["Employee"]
mycol=mydb["registration and login"]
#print(myclient.list_database_names()) to check whether db is present in mongodb or not
dblist=myclient.list_database_names()
if "Employee" in dblist:
    print("The db exists")
else:
    print("The db doesnt exists")
e4={"employee_name":"Sid","Employee_id":"4","Salary":"800000","Designation":"Asst. Manager","Mail_id":"Sid@gmail.com","Mobile_num":"165328998","Address":"Hyderabad"}
a=mycol.insert_one(e4)