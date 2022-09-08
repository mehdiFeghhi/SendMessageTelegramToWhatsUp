from pyrogram import Client, filters
from pyrogram.types import Message

from config import chat_id_eita, chat_id_telegram, api_id, api_hash
from send_message_by_eita import send_message_to, send_file_to, send_by_binary_to

user_client = Client('user_telegram', api_id=api_id, api_hash=api_hash)


@user_client.on_message(filters.chat(chat_id_telegram))
def handle_message(bot: Client, message: Message):
    if message.text:
        text = message.text
        send_message_to(chat_id=chat_id_eita, text=text)
    elif message.photo:
        file_name = message.photo.file_id + '.png'
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)

    elif message.voice :
        file_name = message.voice.file_id+'webp'
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)

    elif message.video:
        file_name = message.video.file_id+'webp'
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)

    elif message.video_note:

        file_name = message.video_note.file_id+'webp'
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)



    elif message.document:
        file_name = message.document.file_id
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)



    elif message.animation:
        file_name = message.animation.file_id
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)



    elif message.sticker:
        file_name = message.sticker.file_id
        bot.download_media(message, file_name)
        send_file_to(chat_id=chat_id_eita, file_name=file_name, caption=message.caption)


    else:
        print("unkown file")

if __name__ == '__main__':
    user_client.run()
