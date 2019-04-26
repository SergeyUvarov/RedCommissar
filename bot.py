# Использование VK API
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

#Ключ группы
token = '778892b40fb7f44a542d65a0ff71b5d8f3b948974829f349b252b8fe462a0e2c9a4204b94812a1b2b830a'

def write_msg(user_id, message, random_id):
    vk.method('messages.send',
                {
                'user_id': user_id,
                'message': message,
                'random_id': random_id
                }
              )

#Авторизация группы
vk = vk_api.VkApi(token=token)

#Работа с сообщениями
longpoll = VkLongPoll(vk)
for event in longpoll.listen():
    if (event.type == VkEventType.MESSAGE_NEW) and (event.to_me):
        userMessage = event.text
        if userMessage.title() == "Привет":
            write_msg(event.user_id, "Хай", event.random_id)
        else:
            write_msg(event.user_id, "Напиши 'привет'", event.random_id)
