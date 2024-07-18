import json
import csv
import datetime
import random
from datetime import timedelta
from google.cloud import pubsub_v1

project_id = ""
topic_id = ""

def getlatlon()-> str:
    a=["-73.98174286,40.71915817", "-73.98508453, 40.74716568", "-73.97333527,40.76407242", "-73.99310303,40.75263214",
		"-73.98229218,40.75133133", "-73.96527863,40.80104065", "-73.97010803,40.75979996", "-73.99373627,40.74176025", "-73.98544312,	40.73571014",
		"-73.97686005,40.68337631", "-73.9697876,40.75758362", "-73.99397278,40.74086761", "-74.00531769,40.72866058", "-73.99013519, 40.74885178",
		"-73.9595108, 40.76280975", "-73.99025726,	40.73703384", "-73.99495697,40.745121", "-73.93579865,40.70730972", "-73.99046326,40.75100708",
		"-73.9536438,40.77526093", "-73.98226166,40.75159073", "-73.98831177,40.72318649", "-73.97222137,40.67683029", "-73.98626709,40.73276901",
		"-73.97852325,	40.78910065", "-73.97612, 40.74908066", "-73.98240662,	40.73148727", "-73.98776245,40.75037384", "-73.97187042,40.75840378",
		"-73.87303925,	40.77410507", "-73.9921875,	40.73451996", "-73.98435974,40.74898529", "-73.98092651,40.74196243", "-74.00701904,40.72573853",
		"-74.00798798,	40.74022675", "-73.99419403,40.74555969", "-73.97737885,40.75883865", "-73.97051239,40.79664993", "-73.97693634,40.7599144",
		"-73.99306488,	40.73812866", "-74.00775146,40.74528885", "-73.98532867,40.74198914", "-73.99037933,40.76152802", "-73.98442078,40.74978638",
		"-73.99173737,	40.75437927", "-73.96742249,40.78820801", "-73.97813416,40.72935867", "-73.97171021,40.75943375", "-74.00737,40.7431221",
		"-73.99498749,	40.75517654", "-73.91600037,40.74634933", "-73.99924469,40.72764587", "-73.98488617,40.73621368", "-73.98627472,40.74737167"
		]
    random_num = random.randint(0, 53)
    b = a[random_num]
    return b

def getstore()-> str:
    taxi = ['Y','N']
    random_num = random.randint(0, 1)
    return taxi[random_num]




def publish_messages(project_id: str, topic_id:str, message: dict, service_account_file:str = None) -> None:
    if service_account_file:
        publisher = pubsub_v1.PublisherClient.from_service_account_file(filename=service_account_file)
    else:
        publisher = pubsub_v1.PublisherClient()
    
    topic_path = publisher.topic_path(project=project_id, topic=topic_id)
    
    if publisher.get_topic(request={"topic": topic_path}):
        json_data = json.dumps(message).encode("utf-8")
        future = publisher.publish(topic_path, json_data)
        print(f'{future.result()}')
    else:
        print(f"Topic {topic_path} does not exists")
        exit(1)
    print(f"Published messages to {topic_path}.")


if __name__ == "__main__":
    i = 0
    for _ in range(1, 100):
        i = int(i) + 1
        id = 'id' + str(random.randint(1665586, 8888888))
        vendor_id = random.randint(1, 2)
        pickup_date = datetime.datetime.now().isoformat()
        dropoff_date = datetime.datetime.now() + timedelta(minutes=random.randint(30, 100))
        dropoff_date = dropoff_date.isoformat()
        passengerCount=random.randint(1, 9)
        location = getlatlon()
        location=location.split(",")
        pickupLongitude=location[0]
        pickupLatitude=location[1]
        location=getlatlon()
        location=location.split(",")
        dropoffLongitude=location[0]
        dropoffLatitude=location[1]	
        storeAndFwdFlag=getstore()
        gcDistance=random.randint(1, 7)
        tripDuration=random.randint(8, 10000)
        googleDistance=gcDistance
        googleDuration=tripDuration
	    
        new_dict={}
        new_dict["id"]=id
        new_dict["vendorId"]=vendor_id
        new_dict["pickupDate"]=pickup_date
        new_dict["dropoffDate"]=dropoff_date
        new_dict["passengerCount"]=passengerCount
        new_dict["pickupLongitude"]=pickupLongitude
        new_dict["pickupLatitude"]=pickupLatitude
        new_dict["dropoffLongitude"]=dropoffLongitude
        new_dict["dropoffLatitude"]=dropoffLatitude
        new_dict["storeAndFwdFlag"]=storeAndFwdFlag
        new_dict["gcDistance"]=gcDistance
        new_dict["tripDuration"]=tripDuration
        new_dict["googleDistance"]=googleDistance
        new_dict["googleDuration"]=googleDuration

    
        publish_messages(project_id, topic_id, new_dict)