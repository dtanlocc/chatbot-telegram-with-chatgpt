from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import openai
import config
openai.organization = config.ORGANIZATION
openai.api_key = config.API_KEY

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Xin chào {update.effective_user.first_name}')

async def ask(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response = openai.ChatCompletion.create(
                model= "gpt-3.5-turbo", # replace this value with the deployment name you chose when you deployed the associated model.
                messages = [{"role":"user","content":user_message}],
                temperature=0,
                max_tokens=350,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None)
    mess = response["choices"][0]["message"]["content"]
    await update.message.reply_text(mess)


app = ApplicationBuilder().token("5982177602:AAHoSrSIshoU3X9Nu-KSAYPPhz72crDvY6w").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("ask", ask))

app.run_polling()