from config import bot, yoomoney_token
from yoomoney import Quickpay

def give_quickpay(message):
    quickpay = Quickpay(
            receiver="4100118555470014",
            quickpay_form="shop",
            targets="Sponsor this project",
            paymentType="SB",
            sum=25,
            )
    bot.reply_to(message, text=f'Your fast quickpay form is: \n `{quickpay.base_url}`', parse_mode='MarkDown')