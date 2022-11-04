import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import ContentType


bot = Bot('5574053580:AAEKrjPGKpxFYty0xHHYeyt-ZG01WhETf2k', parse_mode="HTML")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1) #создаем клавиатуру
   webAppTest = types.WebAppInfo(url="https://telegram.mihailgok.ru") #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру


def webAppKeyboardInline(): #создание inline-клавиатуры с webapp кнопкой
   keyboard = types.InlineKeyboardMarkup(row_width=1) #создаем клавиатуру inline
   webApp = types.WebAppInfo(url="https://telegram.mihailgok.ru") #создаем webappinfo - формат хранения url
   one = types.InlineKeyboardButton(text="Веб приложение", web_app=webApp) #создаем кнопку типа webapp
   keyboard.add(one) #добавляем кнопку в клавиатуру

   return keyboard #возвращаем клавиатуру


@dp.message_handler(commands=['start']) #обрабатываем команду старт
async def start_fun(message: types.Message):
   await message.answer(
      f'Привет, я бот для проверки телеграмм webapps!)\n'
      f'Запустить тестовые страницы можно нажав на кнопки.', 
      reply_markup=webAppKeyboard()
   ) #отправляем сообщение с нужной клавиатурой


@dp.message_handler(content_types=[ContentType.TEXT])
async def new_mes(message):
   await start_fun(message)


@dp.message_handler(content_types=[ContentType.WEB_APP_DATA]) #получаем отправленные данные 
async def answer(web_msg):
   print(web_msg) #вся информация о сообщении
   print(web_msg.web_app_data.data) #конкретно то что мы передали в бота
   await bot.send_message(web_msg.chat.id, f"получили инофрмацию из веб-приложения: {web_msg.web_app_data.data}") 
   # отправляем сообщение в ответ на отправку данных из веб-приложения 


if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
