from API.InstagramAPI import InstagramAPI
import aux_funcs as f
import time
print("----------------------------------------------------------------------------------------------------")
USERNAME = str(input('- Put your Instagram username: '))
PASSWORD = str(input('- Put your Instagram username: '))
PAGE = str(
    input('- Which Instagram page do you want to follow followers/following?: '))
TYPE = int(input(
    '- Do you want to follow followers or followings? Type 1 for followers or 2 for followings: '))

while TYPE != 1 and TYPE != 2:
    print('Error! Please put only 1 or 2!')
    TYPE = int(input(
        '- Do you want to follow followers or followings? Type 1 for followers or 2 for followings: '))

HOW_MANY = int(input('- How many people you want to follow?: '))

print("----------------------------------------------------------------------------------------------------")
print('Starting...')

api = InstagramAPI(username=USERNAME, password=PASSWORD)
api.login()

print('Loged in as ' + USERNAME)
print('\n')

id = f.get_id(username=PAGE)

if TYPE == 1:
    people = api.getTotalFollowers(usernameId=id)
elif TYPE == 2:
    people = api.getTotalFollowings(usernameId=id)

i = 1
for person in people[:HOW_MANY]:
    api.follow(userId=person["pk"])
    print(str(i) + ". Followed " + "'" + person['username'] + "'" +
          ", waiting for 30 sec and following another one.")
    time.sleep(30)
    i += 1

print("Finished. Have a good day!")
