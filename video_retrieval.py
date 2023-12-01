import requests
import pprint
import os
from dotenv import load_dotenv
import random
import string

load_dotenv()

apiKey = os.getenv('AZURE_VISION_KEY')
endpoint = os.getenv('AZURE_VISION_ENDPOINT')
root_uri = endpoint  + "computervision/retrieval/indexes/"
apiversion = "?api-version=2023-05-01-preview"
headers = {
    'Ocp-Apim-Subscription-Key' : apiKey,
    'Content-Type' :  'application/json'
}

def get_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

# body to move to an argument
def create_index(index_name):

    resource = root_uri + index_name + apiversion
    body = {
        'metadataSchema': {
            'fields': [
            {
                'name': 'cameraId',
                'searchable': False,
                'filterable': True,
                'type': 'string'
            },
            {
                'name': 'timestamp',
                'searchable': False,
                'filterable': True,
                'type': 'datetime'
            }
            ]
        },
        'features': [
            {
            'name': 'vision',
            'domain': 'surveillance'
            },
            {
            'name': 'speech'
            }
        ]
        }
    response = requests.put(resource, headers=headers, json=body)
    return response

def get_list_of_indexes():

    resource = root_uri + apiversion
    data = requests.get(resource, headers=headers).json()
    return data

def get_index(index_name):

    resource = root_uri + index_name + apiversion
    data = requests.get(resource, headers=headers).json()
    return data

def delete_index(index_name):

    resource = root_uri + index_name + apiversion
    response = requests.delete(resource, headers=headers)
    return response

# body to move to an argument
def create_ingestion(index_name, ingestion_name):

    resource = root_uri + index_name + "/ingestions/" + ingestion_name + apiversion
    body = {
        'videos': [
            {
                'mode': 'add',
                'documentId': get_random_string(20),
                'documentUrl': 'https://spatanalystor.blob.core.windows.net/videos/videoRabbitOneMinute.mp4?sp=r&st=2023-11-30T10:21:36Z&se=2023-11-30T18:21:36Z&spr=https&sv=2022-11-02&sr=b&sig=cJ4QZke4dXD3bv1nbiw001do2GXL0GajASM15vR2MJk%3D',
                'metadata': {
                    'cameraId': 'camera1',
                    'timestamp': '2023-06-30 17:40:33'
                }
            }
        ]
    }
    response = requests.put(resource, headers=headers, json=body)
    return response

def get_ingestion(index_name, ingestion_name):

    resource = root_uri + index_name + "/ingestions/" + ingestion_name + apiversion
    data = requests.get(resource, headers=headers).json()
    return data

# body to move to an argument
def search_by_text(index_name):

    resource = root_uri + index_name + ":queryByText" + apiversion
    body = {
        'queryText': 'an apple',
        # 'filters': {
            # 'stringFilters': [
            # {
            #     'fieldName': 'cameraId',
            #     'values': [
            #     'camera1'
            #     ]
            # }
            # ],
            # 'featureFilters': ['vision']
        # }
    }
    response = requests.post(resource, headers=headers, json=body)
    return response

def list_documents(index_name):

    skip = 0
    top = 30
    resource = root_uri + index_name + "/documents" + apiversion + "&$skip=" + str(skip) + "&$top=" + str(top)
    response = requests.get(resource, headers=headers)
    data = response.json()
    return data


if __name__ == "__main__":

    index_name = "my-video-index"
    ingestion_name = "my-ingestion"

    # response = create_index(index_name)
    # pprint.pprint(response.json())

    # response = delete_index(index_name)
    # print(response)

    # data = get_list_of_indexes()
    # for item in data["value"]:
    #     print(item["name"])

    # data = get_index(index_name)
    # pprint.pprint(data)

    # response = create_ingestion(index_name, ingestion_name)
    # pprint.pprint(response.json())

    # data = get_ingestion(index_name, ingestion_name)
    # pprint.pprint(data)

    response = search_by_text(index_name)
    for item in response.json()['value']:
        print('best:', item['best'])
        print('relevance:', item['relevance'])
        print('start:', item['start'])
        print('end:', item['end'], '\n')

    # data = list_documents(index_name)
    # pprint.pprint(data)