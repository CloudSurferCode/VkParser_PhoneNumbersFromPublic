import vk_api
import json
import pandas as pd


vk_session = vk_api.VkApi('Your Login', 'Your Password')  # логин и пароль
vk_session.auth()
vk = vk_session.get_api()





def main():
    #    x = vk.friends.get(fields='contacts')
    y = vk.groups.getMembers(group_id='Your Public Id',
                             fields='contacts')  # Id группы и номера телефонов пользователей этой группы



    data = y
    json_str = json.dumps(data)
    resp = json.loads(json_str)
    print(resp)
    df = pd.io.json.json_normalize(data['items'])
    print(df)
    df.to_csv(r'out.csv', index=False)



if __name__ == '__main__':
    main()

