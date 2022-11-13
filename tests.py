import requests
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def test_create_task():
    r = requests.post('http://localhost:5000/v1/tasks', json={"title": "My First Task"})
    assert isinstance(r.json()["id"], int)
    assert len(r.json()) == 1

def test_list_all_tasks():
    r = requests.get('http://localhost:5000/v1/tasks')
    assert isinstance(r.json()["tasks"], list)
    assert len(r.json()) == 1
    assert isinstance(r.json()["tasks"][0]["id"], int)
    assert isinstance(r.json()["tasks"][0]["title"], str)
    assert isinstance(r.json()["tasks"][0]["is_completed"], bool)
    assert len(r.json()["tasks"][0]) == 3

def test_get_task():
    r = requests.get('http://localhost:5000/v1/tasks/1')
    assert isinstance(r.json(),dict)
    assert isinstance(r.json()["id"], int)
    assert isinstance(r.json()["title"], str)
    assert isinstance(r.json()["is_completed"], bool)
    assert len(r.json()) == 3

def test_update_task():
    r = requests.put('http://localhost:5000/v1/tasks/1', json={"title": "My 1st Task", "is_completed": True})
    assert not r.content

def test_delete_task():
    r = requests.delete('http://localhost:5000/v1/tasks/1')
    assert not r.content



########### BONUS TASKS ##########################

def test_bulk_add_task():
    r = requests.post('http://localhost:5000/v1/tasks', json={
        'tasks': [
            {'title': "Test Task 1", 'is_completed': True},
            {'title': "Test Task 2", 'is_completed': False},
            {'title': "Test Task 3", 'is_completed': True}
        ]
    })
    assert len(r.json()['tasks']) == 3
    for i in range(len(r.json()['tasks'])):
        assert isinstance(r.json()['tasks'][i]["id"], int)

def test_bulk_delete_task():
    r = requests.delete('http://localhost:5000/v1/tasks', json={
    'tasks': [
        {'id': 1},
        {'id': 2},
        {'id': 3}
    ]}
    )
    assert not r.content




def run_tests():
    try:
        test_create_task()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 1 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 1!')

    try:
        test_list_all_tasks()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 2 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 2!')

    try:
        test_get_task()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 3 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 3!')

    try:
        test_update_task()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 4 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 4!')

    try:
        test_delete_task()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 5 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 5!')

    try:
        test_bulk_add_task()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 6 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 6!')

    try:
        test_bulk_delete_task()
        print(f'{bcolors.BOLD}OK PASSED{bcolors.ENDC} ... 7 of 7')
    except:
        print(f'{bcolors.FAIL}FAILED{bcolors.ENDC} ...  on test 7!')



run_tests()