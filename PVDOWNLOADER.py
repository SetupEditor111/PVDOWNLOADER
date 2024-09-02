from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.enums import MessageMediaType
import random , os

'''
    ربات دانلود از کانال هایی که حفاظت از محتوا دارند
    همچنین دانلود تمام پیام های زمانداری که به پی وی اکانت ربات ارسال میشن
    فعلا فقط دانلود عکس و ویدیو 
    به امید اینکه تلگرام امنیتش رو توی این موارد افزایش بده!

    نویسنده: @DearAhmadi
    ورژن دوم پرایوت دانلودر هوشمند

    برای اولین بار در کانال هوش سیاه @DarkMindsTm
    آموزش راه اندازی توی کانال هوش سیاه..
'''

app = Client(
    name=           'downloader-pv',    # session name
    api_id=         22454967,            # api id
    api_hash=       '353e74226c24e32fd90e6c168c8ec942'     # api hash
)
admin = 1287257273                       # admin id

@app.on_message(filters.private and filters.text)
async def running(c: Client, m: Message) :
    text =          m.text
    from_id =       m.from_user.id
    if from_id == admin :
        if text == 'ربات' or text == 'bot' or text == '/bot':
            await m.reply_text('<b>Bot is Running</b>')

        if 'https://t.me/' in text :
            send =          await m.reply_text('<b>Wait a moment ..</b>')
            rand =          random.randint(1000, 9999999)
            link =          text
            link =          link.replace('https://t.me/', '').replace('c/', '').replace('?single', '')
            split =         link.split('/')
            try :
                if int(split[0]) :
                    chat_id =       str('-100' + split[0])
            except Exception :
                chat_id =       str('@' + split[0])
            message_id =        int(split[1])
            caption =           f"☑️ Downloaded successful!"
            try :
                await app.get_chat(chat_id=chat_id)
            except Exception as Error :
                await m.reply_text(Error)
            else :
                info =          await app.get_messages(chat_id=chat_id, message_ids=message_id)
                format =        None
                if info.media == MessageMediaType.VIDEO :
                    format =    'mp4'
                if info.media == MessageMediaType.PHOTO :
                    format =    'jpg'
                if format is not None:
                    try :
                        await app.edit_message_text(chat_id=admin, message_id=send.id, text='<b>📥 Downloading ..</b>')
                        await app.download_media(message=info, file_name=f'downloaded-{rand}.{format}')
                        path = f'downloads/downloaded-{rand}.{format}'
                        await app.edit_message_text(chat_id=admin, message_id=send.id, text='<b>🗳 sending ..</b>')
                        if format == 'mp4' :
                            await app.send_video(chat_id=admin, video=path, caption=caption)
                        if format == 'jpg' :
                            await app.send_photo(chat_id=admin, photo=path, caption=caption)
                    except Exception as error:
                            print(error)
                            await m.reply_text('<b>Video or Photo not found!</b>')
                    else :
                        os.remove(path)
                else :
                    await m.reply_text('<b>Video or Photo not found!</b>')
            finally :
                await app.delete_messages(chat_id=admin, message_ids=send.id)
        
@app.on_message(filters.photo)
async def onphoto(c: Client, m: Message) :
    try :
        if m.photo.ttl_seconds :
            rand = random.randint(1000, 9999999)
            local = f"downloads/photo-{rand}.png"
            await app.download_media(message=m, file_name=f"photo-{rand}.png")
            await app.send_photo(chat_id=admin, photo=local, caption=f"🔥 New timed image {m.photo.date} | time: {m.photo.ttl_seconds}s")
            os.remove(local)
    except :
        pass

@app.on_message(filters.video)
async def onvideo(c: Client, m: Message) :
    try :
        if m.video.ttl_seconds :
            rand = random.randint(1000, 9999999)
            local = f"downloads/video-{rand}.mp4"
            await app.download_media(message=m, file_name=f"video-{rand}.mp4")
            await app.send_video(chat_id=admin, video=local, caption=f"🔥 New timed video {m.video.date} | time: {m.video.ttl_seconds}s")
            os.remove(local)
    except :
        pass

'''
    نویسنده: @DearAhmadi
    ورژن دوم پرایوت دانلودر هوشمند

    برای اولین بار در کانال هوش سیاه @DarkMindsTm
    آموزش راه اندازی توی کانال هوش سیاه..
'''

app.start(), print("Bot is Running , @DarkMindsTm"), idle(), app.stop()