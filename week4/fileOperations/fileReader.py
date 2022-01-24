import re
import sys
sys.path.append('models/')

from user import User
import json

def readJson(path:str) -> list:
    """
        This generator created to read given json file and convert User object
        :param path: <str> path of json file
        :return: <list> each item of User Object
        """
    try:
        with open(path, 'r') as file:
            datas = json.load(file)

            for data in datas:
                yield User(
                name = data['profile']['name'],
                username = data['username'],
                email = data['email'],
                emailuserlk = __checkEmail(data['username'], data['email']),
                usernamelk = __checkUsername(data['profile']['name'], data['username']),
                birthYear = __splitDOB(data['profile']['dob'])['year'],
                birthMonth = __splitDOB(data['profile']['dob'])['month'],
                birthDay = __splitDOB(data['profile']['dob'])['day'],
                country = __getCountry(data['profile']['address']),
                )
    except Exception as err:
        print(f'Failed to read {path}')

def __splitDOB(dob:str) -> dict:
    """
        This method created to split date of birth
        :param dob: <str>
        :return: <dict> birth year, birth month and birth day
        """
    pattern = re.compile(r"([0-9]{4})-([0-9]{2})-([0-9]{2})")
    match = pattern.search(dob)

    return {
        'year': int(match.group(1)),
        'month': int(match.group(2)),
        'day': int(match.group(3))
    }

def __checkEmail(username:str, email:str) -> int:
    """
        This method created to check do email have at least 3 letter of username
        :param username: <str> user's username
        :param email: <str> user's email
        :return: <int> 1 = True 0 = False
        """
    for i in range(3, len(username)+1):
        if username[:i].lower() in email.lower():
            return 1
    return 0

def __checkUsername(fullName:str, username:str) -> int:
    """
        This method created to check do username have at least 3 letter of full name
        :param fullName: <str> user's full name
        :param username: <str> user's username
        :return: <int> 1 = True 0 = False
        """
    name = fullName.split()[0].lower()
    surname = fullName.split()[1].lower()

    for i in range(3, len(name)+1):
        if name[:i] in username.lower():
            return 1

    for i in range(3, len(surname)+1):
        if surname[:i] in username.lower():
            return 1
    
    return 0

def __getCountry(adress:str) -> str:
    """
        This method created to get user country from full adress
        :param adress: <str> user full adress
        :return: <str> user country
        """
    return adress.split(',')[-1].strip()