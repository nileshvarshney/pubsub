from google.cloud import pubsub_v1

project_id = "<PROJECT_ID>"
topic_id = "<topic-id>"

def create_topic(project_id: str, topic_id:str, service_account_file:str = None) -> None:
    if service_account_file:
       publisher = pubsub_v1.PublisherClient.from_service_account_file(filename=service_account_file)
    else:
        publisher = pubsub_v1.PublisherClient()

    topic_path = publisher.topic_path(project=project_id, topic=topic_id)

    # check the existance of the topic
    topic  = publisher.create_topic(request={"name": topic_path})
    print(f"Created topic {topic.name}")

       
if __name__ == "__main__":
  create_topic(project_id, topic_id)
