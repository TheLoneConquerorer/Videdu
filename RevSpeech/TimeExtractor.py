import requests
import json
import time

API_KEY = "Bearer 01MquRaDz0HvlYEPA-gMc6F7L2OVUfaNdJHQcxwBbP_wpH_Z9lkZhZjKBvwaE4bC1CQnfj4A5uZcIbjIqeFhW0OR73vxc"
HEADERS = {'Authorization': API_KEY}


def view_job(id=59594172):
    url = f'https://api.rev.ai/revspeech/v1beta/jobs/{id}'
    request = requests.get(url, headers=HEADERS)
    print(request.status_code)

    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body


def submit_job_file(file):
    url = "https://api.rev.ai/revspeech/v1beta/jobs"
    files = {'media': (file, open(file, 'rb'), 'audio/mp3')}
    request = requests.post(url, headers=HEADERS, files=files)
    if request.status_code != 200:
        raise

    response_body = request.json()
    return response_body['id']


def test_workflow_with_file(file):
    print("Submitting job with file")
    id = submit_job_file(file)
    print("Job created")
    view_job(id)

    while True:
        job = view_job(id)
        status = job["status"]
        print(f'Checking job transcription status: { status }')
        if status == "transcribed":
            break
        if status == "failed":
            raise

        print("Trying in another 30 seconds")
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

    listy = []
    evenmorelist = []

    for i in range(0, (len(dataz['monologues'][0]['elements']))):
        try:
            first_start_time = round((dataz["monologues"][0]['elements'][i]['ts']), 3)
            first_end_time = round((dataz["monologues"][0]['elements'][i]['end_ts']), 3)
            # Do something.

            listy.append(first_start_time)
            listy.append(first_end_time)

            pass

        except:

            continue

    for i in range(0, len(listy), 4):
        try:
            if (listy[i + 2] - listy[i + 1]) > 0.45:
                evenmorelist.append((listy[i + 1], listy[i + 2]))
            pass

        except:

            continue

    print(evenmorelist)

    with open("moredata", "w") as output:
        output.write(str(evenmorelist))


if __name__ == "__main__":
    main()

