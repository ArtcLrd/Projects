from firebase_admin import firestore , credentials
import firebase_admin
from google.cloud.firestore_v1.base_query import FieldFilter, Or
import datetime


class Db_update():

    def get_all_docs(self,collectionName,db):
        docs = (
            db.collection(collectionName).stream()
        )
        data_dict = {}
        doc_list=[]
        for doc in docs:
            doc_data = doc.to_dict()
            doc_data['id'] = doc.id
            doc_data['docData'] = doc._data
            doc_list.append(doc_data)
        
        for doc_data in doc_list:
            data_dict[doc_data['docData']['carNumber']] = doc_data['docData']['availability']
        
        return data_dict


    def get_document(self, collectionName, documentId, db):
        doc_ref = db.collection(collectionName).document(documentId)
        doc = doc_ref.get()

        data = {}

        if (doc.exists):
            data[doc.id] = doc.get("availability")
            return data
        else:
            print(f"No such document exists with id {documentId}")
            return None
        
    def get_documents_with_status(self,collection_name,status_value,db):
        try:
            doc_ref = db.collection(collection_name)
            query = doc_ref.where(filter=FieldFilter("availability", "==", status_value))
            docs = query.stream()
            dict_false = {}
            doc_list = []
            for doc in docs:
                doc_data = doc.to_dict()
                doc_data['id'] = doc.id
                doc_data['docData'] = doc._data
                doc_list.append(doc_data)

            for doc_data in doc_list:
                dict_false[doc_data['id']] = doc_data['docData']['carNumber']
            
            return dict_false

        except Exception as e:
            print('Error getting documents from the database,{str(e)}')
    
    def get_documents_with_status_only_id(self,collection_name,status_value,db):
        try:
            doc_ref = db.collection(collection_name)
            query = doc_ref.where(filter=FieldFilter("availability", "==", status_value))
            docs = query.stream()
            arr = []
            for doc in docs:
                data = doc.id
                arr.append(data)
                
            return arr[0]            
        except Exception as e:
            print(f'Error getting documents from the database,{str(e)}')

    def update_exixting_doc(self,collectionName,docID,db,num_str,value):

        val  = value

        num_str = num_str.upper()

        collection_ref = db.collection(collectionName)

        doc_ref = collection_ref.document(docID)
        
        exitTime = self.get_bookedMinutes(collectionName,docID,db)

        exitStr = exitTime.get(docID)
        
        time = datetime.datetime.now()

        if exitStr == 5:
            
            time_changed = datetime.timedelta(minutes = 5)

            Exittime = time + time_changed

        elif exitStr == 10:
            time_changed = datetime.timedelta(minutes = 10)

            Exittime = time + time_changed
        elif exitStr == 15:
            time_changed = datetime.timedelta(minutes = 5)

            Exittime = time + time_changed
        else:
            Exittime = time

        doc_ref.update({
            'carNumber' : num_str,
            'availability' : val,
            'EntTime' : time,
            'ExitTime' : Exittime

        })

    def get_bookedMinutes(self,collectionName,docId,db):
        doc_ref = db.collection(collectionName).document(docId)
        doc = doc_ref.get()

        data = {}

        if (doc.exists):
            data[doc.id] = doc.get("bookedMinutes")
            return data
        else:
            print(f"No such document exists with id {docId}")
            return None
    
    def get_Exit_time(self,collectionName,docId,db):
        doc_ref = db.collection(collectionName).document(docId)
        doc = doc_ref.get()

        data = {}

        if (doc.exists):
            data[doc.id] = doc.get("ExitTime")
            return data
        else:
            print(f"No such document exists with id {docId}")
            return None
        
    def clearData(self,collectionName,db):
        docs = db.collection(collectionName).get()
        for doc in docs:
            key = doc.id
            db.collection(collectionName).document(key).update({
                    'EntTime' : "",
                    'ExitTime' : "",
                    'availability' : True,
                    'bookedMinutes' : 0,
                    'carNumber' : "",
                    'customerEmail' : "",
                    'customerName' : ""

                })
            
 ###########################################################################################################       

if __name__ == "__main__":
    cred = credentials.Certificate(r"E:\Programs\uaps-test1-firebase-adminsdk-v6vsd-53b0bcc3d6.json")
    firebase_admin.initialize_app(cred,{"databaseURL":"https://uaps-test1-default-rtdb.firebaseio.com"})
    db = firestore.client()
    db_check = Db_update()
    #db_check.update_exixting_doc('seats','1',db,'MH10208',False)
    db_check.clearData('seats',db)