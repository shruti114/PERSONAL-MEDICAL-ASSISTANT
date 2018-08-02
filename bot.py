from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from watson_developer_cloud import ConversationV1
import json
from dbhelper import DBHelper
db=DBHelper()

context = None


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    print('Received /start command')
    update.message.reply_text('Hi!')


def help(bot, update):
    print('Received /help command')
    update.message.reply_text('Help!')


def message(bot, update):
    print('Received an update')
    global context

    conversation = ConversationV1(username='8a8eac1c-f2e1-4888-8408-c9aa338fb439',
                                  password='XZdNGGxnuEKv',
                                  version='2018-02-16')

    # get response from watson
    response = conversation.message(
        workspace_id='00433057-81db-4e1e-ac1e-ae6076790f6e',
        input={'text': update.message.text},
        context=context)
    print(json.dumps(response, indent=2))
    
    context = response['context']
    try:
	if ((context['Temperature']=='yes' and context['Fatigue']=='yes' and context['Chill']=='yes') or (context['Temperature']=='yes')) :
    		update.message.reply_text('You may have fever.')
		m="You can take "+db.get_med('Fever')
		update.message.reply_text(m)
    except Exception, e:
	print('Exception',e)
    #try:
	#if ((context['cold']=='yes' and context['Chill']=='yes')or(context['cold']=='yes')) :
        	#update.message.reply_text('You may have cold.')
		#m="You can take "+db.get_med('Cold')
		#update.message.reply_text(m)
    #except Exception, e:
	 #print('Exception',e)
   
    #try: 
	#if((context['anemia1']=='yes') or (context['anemia_symptoms']=='yes')):
		#update.message.reply_text('You may be suffering from Anemia.')
		#m="You can take "+db.get_med('Anemia')
		#update.message.reply_text(m)
    #except Exception, e:
	#print('Exception',e)
    try: 
        if(context['diarrhoea']=='yes' and context['vomiting']=='yes' and context['Fatigue']=='yes'):
		update.message.reply_text('You may be suffering from Foodpoisoning.')
		m="You can take "+db.get_med('Food poisoning')
		update.message.reply_text(m)
    except Exception, e:
        print('Exception',e)
    try:
	if (context['skin_allergy']=='yes' or context['skin_dis']=='yes'):
		update.message.reply_text('You may have Skin Allery.')
		m="You can take "+db.get_med('Skin Allergy')
		update.message.reply_text(m)
    except Exception, e:
	print('Exception',e)
    # build response
    resp = ''
    for text in response['output']['text']:
        resp += text

    update.message.reply_text(resp)


def main():
    #print(db.get_med('FEVER'))
    #print(db.get_med('Fever'))
    # Create the Updater and pass it your bot's token.
    updater = Updater('623887564:AAHtNb41KPMA77e27zkvfrXFBxp9kRSKzSs')
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, message))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
