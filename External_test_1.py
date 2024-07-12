""""class Storage():
    list_val={"username":"NULL","password":"NULL"}
    def store_text(self,uname,passText):
        self.list_val["username"]=uname
        self.list_val["password"]=passText

    def disp_text(self):
            print(self.list_val)

if __name__=="__main__":
     s = Storage()
     s.store_text(" Doe", "12345")
     x=s.list_val.get("username")
     print(x)"""

from datetime import datetime, timedelta

# Define a datetime object
dt = datetime.now()
print(f"Current datetime: {dt}")

# Create a timedelta of 5 days
delta = timedelta(days=5)

# Subtract the timedelta from the datetime
diff = dt - delta

# Get the difference in days
diff_in_days = diff.total_seconds() / 86400

# Print the difference in days
print(f"Difference in days: {diff_in_days:.2f}")


"""if __name__ == "__main__":
    cred = credentials.Certificate(r"E:\Programs\uaps-test1-firebase-adminsdk-v6vsd-53b0bcc3d6.json")
    firebase_admin.initialize_app(cred,{"databaseURL":"https://uaps-test1-default-rtdb.firebaseio.com"})
    db = firestore.client()
    db_check = Db_update()
    db_check.update_exixting_doc('seats','1',db,'MH10208',False)
    #db_check.clearData('seats',db)"""