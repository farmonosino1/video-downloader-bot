from aiogram import Bot, Dispatcher, executor, types
import logging
from pytube import YouTube
from buttons import lang
import os

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6705266646:AAHt-3j_2dSSNycjdAN8DLaX1s0Fvx4mfFg'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom {message.from_user.full_name}!\nmen YouTubedan video yuklovchi botmam\nmenga youtubedagi video linkini yuboring")

@dp.message_handler()
async def send_video(message: types.Message):
    if message.text.startswith("https://www.youtube.com/") or message.text.startswith("https://youtube.com/"):
        yt = YouTube(message.text)
        await message.answer("Kutib turing video yuklanmoqda...")
        video = yt.streams.get_highest_resolution().download()
        with open(video, 'rb') as video:
            await message.answer_video(video=video, caption=yt.title)
            if "#" in yt.title:
                title = yt.title.replace('#', '')
                try:
                    os.remove(f'{str(title)}.mp4')
                except:
                    pass 
            elif ":" in yt.title:
                title = yt.title.replace(':', '')
                try:
                    os.remove(f'{str(title)}.mp4')
                except:
                    pass 
            elif "/" in yt.title:
                title = yt.title.replace('/', '')
                try:
                    os.remove(f'{str(title)}.mp4')
                except:
                    pass
            else:
                try:
                    os.remove(f'{str(title)}.mp4')
                except:
                    pass
        voice = yt.streams.get_audio_only().download()
        with open(voice, 'rb') as voice:
            await message.answer_voice(voice=voice, caption=yt.title)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
