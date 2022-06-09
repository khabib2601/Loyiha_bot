from config import TOKEN 
import logging
from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from aiogram.types import Message, CallbackQuery
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("<b>Tilni tanlang / Choose language </b>",parse_mode='HTML',reply_markup = til)

@dp.callback_query_handler(text="uzb")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("<b>👋Assalomu alaykum! </b>,\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!\n\nYosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",parse_mode='HTML',reply_markup=bir)

@dp.callback_query_handler(text="loyiha")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("Loyiha haqida",reply_markup=bosh)

@dp.callback_query_handler(text="loyiha2")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?</b>\n\nMazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan yoshlar qatlamini loyihalar boshqaruvi bo'yicha nazariy jihatdan o'qitish, amaliy jihatdan yoshlarga ish tajribasini ulashish, turli fikr va dunyoqarashga ega shaxslar orasida muloqot almashinuvini yo'lga qo'yish maqsadida tashkil etilgan.""",parse_mode='HTML',reply_markup=orqa)
 await call.message.delete()

@dp.callback_query_handler(text="loyiha3")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 Loyihaning vazifalari nimalardan iborat?</b>  \n\n• Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab, davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;\n\n• Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;\n\n• Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, o'rtadagi "jarlik"ka ma'lum ma'noda chek qo'yish, ularning o'zaro hamkorligini ta'minlashga ko'maklashish.""",parse_mode='HTML',reply_markup=orqa)
 await call.message.delete()

@dp.callback_query_handler(text="loyiha4")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?</b>\n\n📝Yosh menejerlar dasturining o’tkazilish tartibi:\n\nLoyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi.\n\n📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok etishga nomzod shaxslarni ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:\n\n 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);\n• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;\n• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi).\n\n💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi, o'z ambitsiyalariga ega va kelajakda katta maqsadlari bor yoshlar tanlab olinadi.""",parse_mode='HTML',reply_markup=orqa)
 await call.message.delete()

@dp.callback_query_handler(text="loyiha5")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?</b>\n\n— ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;\n — IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;\n— 17-25 yosh orasida bo'lish;\n— Toshkent shahri va viloyati hududida istiqomat qilish.""",parse_mode='HTML',reply_markup=orqa)
 await call.message.delete()

@dp.callback_query_handler(text="savol")
async def menu_uchun(call: CallbackQuery):
    await call.message.answer("Assalomu alaykum!\n\nSavollaringizni @Ishonch_Dev_Admin ga yo'llashingiz mumkin. Sizga tez orada javob beramiz!\n\nE'tiboringiz uchun rahmat.",reply_markup=orqa1)
   

# English
###########################################
@dp.callback_query_handler(text="eng")
async def menu_uchun(call: CallbackQuery):
    await call.message.answer("<b>👋Assalomu alaykum! </b>,\n\nWe are glad to see you among our observers!\n\nThe Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company!\n\n Through this program personnel management skills system will be formed in the international arena.",parse_mode='HTML',reply_markup=one)
 
@dp.callback_query_handler(text="project")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("About the project",reply_markup=main)
 await call.message.delete()

@dp.callback_query_handler(text="project1")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 What is the main purpose of the Young Managers Program?</b>\n\nProject is designed to provide theoretical training in project management to young people from aged 17 to 25, to share practical work experience with young people, and to establish a community between people with different ideas and worldviews.""",parse_mode='HTML',reply_markup=old1)
 await call.message.delete()

@dp.callback_query_handler(text="project2")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 What are the objectives of project?</b>\n\n• Training of specialists with international qualifications in the field of management and creation of a potential human resources system for entities and objects in the public and private sectors;\n\n • Providing high-paid jobs to increase the knowledge and skills of youth; \n\n • To form a process of communication between the older and younger generations, to put an end to the "cliff" between them, to help them to ensure their interaction;""",parse_mode='HTML',reply_markup=old1)
 await call.message.delete()

@dp.callback_query_handler(text="project3")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 How long will the project last and what is the procedure?</b>\n\n📝 Procedure for the Young Managers Program:\n\nThe project will last for 10 weeks: practical and theoretical lessons will be conducted.\n\n📋 From August 25 to September 10, the process of registration and selection of candidates for participation in the project will be organized:\n\n • Round 1 qualifiers: September 13 will be announced. (100 participants);\n• 
  Qualifying Round 2: September 15-16;\n• Answers: to be announced on September 18 (50 participants).\n\n💡 Out of the candidates, 50 young people who are strong, fluent in English, have their own ambitions and have big goals for the future will be selected.""",parse_mode='HTML',reply_markup=old1)
 await call.message.delete()

@dp.callback_query_handler(text="project4")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("""<b>🔰 What are the requirements for candidates to participate?</b>\n\n— Office work in English, Russian, Uzbek: fluent speaking and writing skills;\n — Knowledge of IT and media; \n— 17-25 years old;\n— Resident of Tashkent city and region.""",parse_mode='HTML',reply_markup=old1)
 await call.message.delete()

@dp.callback_query_handler(text="question")
async def menu_uchun(call: CallbackQuery):
    await call.message.answer("Assalomu alaykum!\n\nYou can send your questions to @Ishonch_Dev_Admin. We will reply you soon.\n\nThank you for your attention..",reply_markup=old2)

    
# Back
@dp.callback_query_handler(text="back1")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("<b>👋Assalomu alaykum! </b>,\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!\n\nYosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",parse_mode='HTML',reply_markup=bir)
 await call.message.delete()

@dp.callback_query_handler(text="back2")
async def menu_uchun(call: CallbackQuery):
    await call.message.answer("Loyiha haqida",reply_markup=bosh)
  
@dp.callback_query_handler(text="back3")
async def menu_uchun(call: CallbackQuery):
     await call.message.answer("<b>👋Assalomu alaykum! </b>,\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!\n\nYosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",parse_mode='HTML',reply_markup=bir)

@dp.callback_query_handler(text="orqa")
async def menu_uchun(call: CallbackQuery):
 await call.message.answer("<b>👋Assalomu alaykum! </b>,\n\nWe are glad to see you among our observers!\n\nThe Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company!\n\n Through this program personnel management skills system will be formed in the international arena.",parse_mode='HTML',reply_markup=one)

@dp.callback_query_handler(text="orqa1")
async def menu_uchun(call: CallbackQuery):
    await call.message.answer("About the project",reply_markup=main)

@dp.callback_query_handler(text="orqa2")
async def menu_uchun(call: CallbackQuery):
     await call.message.answer("<b>👋Assalomu alaykum! </b>,\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!\n\nYosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",parse_mode='HTML',reply_markup=one)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)