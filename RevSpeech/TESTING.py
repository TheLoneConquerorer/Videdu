import requests
import json
import time

API_KEY = "Bearer 01MquRaDz0HvlYEPA-gMc6F7L2OVUfaNdJHQcxwBbP_wpH_Z9lkZhZjKBvwaE4bC1CQnfj4A5uZcIbjIqeFhW0OR73vxc"
HEADERS = {'Authorization': API_KEY}

"""
def submit_job_url(media_url):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    payload = {'media_url': media_url,
               'metadata': "Test"}
    request = requests.post(url, headers=HEADERS, json=payload)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']
    
    def view_job(id=59594172):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def get_transcript(id='59594172'):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def test_workflow_with_url(url):
    print ("Submitting job with URL")
    id = submit_job_url(url)
    print ("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print (f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

"""

def view_job(id=59594172):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)
    print (request.status_code)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def submit_job_file(file):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    files = { 'media': (file, open(file, 'rb'), 'audio/mp3') }
    request = requests.post(url, headers=HEADERS, files=files)
    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']

def test_workflow_with_file(file):
    print ("Submitting job with file")
    id = submit_job_file(file)
    print ("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print (f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print ("Trying in another 30 seconds")
        time.sleep(30)

    return get_transcript(id)

def get_transcript(id):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}/transcript'
    headers = HEADERS.copy()
    headers['Accept'] = 'application/vnd.rev.transcript.v1.0+json'
    request = requests.get(url, headers=headers)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body

def main():

    # Testing with file upload
    file = "test.mp3"
#    submit_job_file(file)
    dataz = (test_workflow_with_file(file))
    print (dataz)

    with open('data.json', 'w') as f:
        json.dump(dataz, f)

if __name__ == "__main__":
    main()

