from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from telegram import Chat
from uuid import uuid4


class Kaomoji:

    def __init__(self, token):
        self.token = token
        self.mood = ("joy", "anger", "love", "embarrassment", "dissatisfaction", "sympathy", "sadness", "confusion",
                     "surprised", "greeting")
        self.joy = ('o(≧▽≦)o', '(*≧ω≦*)', '(((o(*°▽°*)o)))', '<(￣︶￣)>', '(o^▽^o)', '(─‿‿─)', '☆*:.｡.o(≧▽≦)o.｡.:*☆',
                    '凸(`△´＃)', '(o･ω･o)', '(*≧ω≦*)', '(*・ω・)', 'o(>ω<)o', '(๑˘︶˘๑)', '＼(≧▽≦)／', '(´･ᴗ･ ` )', '(*°▽°*)',
                    '( ´ ▽ ` )', 'ヽ(*⌒▽⌒*)ﾉ', '(⌒‿⌒)', '(◕‿◕)', '(≧◡≦)', '(o´∀`o)', '(´｡• ω •｡`)', '(*⌒―⌒*)')
        self.anger = ('(＃`Д´)', '(`皿´＃)', '( ` ω ´ )', 'ヽ( `д´*)ノ', '(╬ Ò﹏Ó)', '(`ー´)', 'ヽ(`⌒´メ)ノ', '凸(`△´＃)',
                      '( `ε´ )', '٩(╬ʘ益ʘ╬)۶', 'ヾ(`ヘ´)ﾉﾞ', 'ヽ(‵﹏´)ノ', '(ﾒ` ﾛ ´)', '(╬`益´)', '┌∩┐(◣_◢)┌∩┐', '↑_(ΦwΦ)Ψ',
                      '＼＼٩(๑`^´๑)۶／／', '(°ㅂ°╬)', '←~(Ψ▼ｰ▼)∈', '(ノ°益°)ノ', '(҂ `з´ )', '(‡▼益▼)', '(҂` ﾛ ´)凸', '((╬◣﹏◢))')
        self.love = ('(─‿‿─)♡', '	(´,,•ω•,,)♡', '♡( ◡‿◡ )', '(❤ω❤)', '(￣З￣)', '(⌒▽⌒)♡', '(´• ω •`)', 'Σ>―(〃°ω°〃)♡→',
                     '♡＼(￣▽￣)／♡', '(´｡• ᵕ •｡`)', 'ヽ(♡‿♡)ノ', '( ´ ∀ `)ノ～ ♡', '(´ ω `♡)', 'σ(≧ε≦σ)', '(´｡• ω •｡`)',
                     '(*♡∀♡)', '♡(｡- ω -)', '( ´ ▽ ` ).｡ｏ♡', '(⇀ 3 ↼)', '(* ^ ^ * )♡', '(≧◡≦) ♡', '(っ˘з(˘⌣˘ )',
                     '(*˘︶˘ * ).: * ♡', '(♡°▽°♡)')
        self.embarrassment = ('(⌒_⌒;)', '(o^ ^o)', '(*/ω＼)', '(*/_＼)', '(*ﾉωﾉ)', '(o-_-o)', '(*μ_μ)',
                              '( ◡‿◡ *)', '(ᵔ.ᵔ)', '(*ﾉ∀`*)', '(//▽//)', '(//ω//)', '(ノ*°▽°*)', '(*^.^*)', '(*ﾉ▽ﾉ)',
                              '(￣▽￣*)ゞ', '(⁄ ⁄•⁄ω⁄•⁄ ⁄)', '(*/▽＼*)', '(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)', '(„ಡωಡ„)', '(ง ื▿ ื)ว')
        self.dissatisfaction = ('(＃＞＜)', '(；⌣̀_⌣́)', '☆ｏ(＞＜；)○', '(￣ ￣|||)', '(＃￣0￣)', '(￣□￣」)', '(；￣Д￣)', '(〃＞＿＜;〃)',
                                '(￢_￢;)', '(」°ロ°)」', '(＞ｍ＜)', '<(￣ ﹌ ￣)>', '(￣ヘ￣)', '(」＞＜)」', 'o(>< )o', '(⇀‸↼‶)',
                                '(ᗒᗣᗕ)՞', 'ヾ( ￣O￣)ツ', '(＞﹏＜)', '(--_--)', '凸(￣ヘ￣)', '(＞﹏＜)', '(＞﹏＜)', 'ヾ( ￣O￣)ツ')
        self.sympathy = ('(ノ_<。)ヾ(´ ▽ ` )', '｡･ﾟ･(ﾉД`)ヽ(￣ω￣ )', 'ρ(- ω -、)ヾ(￣ω￣; )', 'ヽ(~_~(・_・ )ゝ', 'ヽ(￣ω￣(。。 )ゝ',
                         '(ｏ・_・)ノ”(ノ_<、)', '(っ´ω`)ﾉ(╥ω╥)', 'ヽ(~_~(・_・ )ゝ', '(; ω ; )ヾ(´∀`* )')
        self.sadness = ('(´-ω-`)', '.･ﾟﾟ･(／ω＼)･ﾟﾟ･.', '。゜゜(´Ｏ`) ゜゜。', '(-ω-、)', '｡･ﾟﾟ*(>д<)*ﾟﾟ･｡', "o(TヘTo)",
                        '(っ˘̩╭╮˘̩)っ', '(╥_╥)', '(╥﹏╥)', '(T_T)', '(｡T ω T｡)', '( ╥ω╥ )', '(μ_μ)', '(个_个)', '( ; ω ; )',
                        '･ﾟ･(｡>ω<｡)･ﾟ･', 'o(〒﹏〒)o', '(ಥ﹏ಥ)', '(｡•́︿•̀｡)', '｡ﾟ･ (>﹏<) ･ﾟ｡', '(-_-)')
        self.confusion = ('(￣ω￣;)', 'σ(￣、￣〃)', '(￣～￣;)', '(-_-;)・・・', "┐('～`;)┌", '(・_・ヾ', '(〃￣ω￣〃ゞ', '┐(￣ヘ￣;)┌',
                          '(・_・;)', '(￣_￣)・・・', '╮(￣ω￣;)╭', '(¯ . ¯;)', 'Σ(￣。￣ﾉ)', '＠_＠)', '	(・・;)ゞ', '(#•ิ_•ิ)?',
                          '(◎ ◎)ゞ', '(ーー;)', 'ლ(ಠ_ಠ ლ)', 'ლ#(¯ロ¯"ლ)', '(¯ . ¯٥)')
        self.surprised = ('w(°ｏ°)w', 'ヽ(°〇°)ﾉ', 'Σ(O_O)', 'Σ(°ロ°)', '(⊙_⊙)', '(o_O)', '(O_O;)', '(O.O)', '(°ロ°) !',
                          '(o_O) !', '∑(O_O;)', '( : ౦ ‸ ౦ : )')
        self.greeting = ('(*・ω・)ﾉ', '(￣▽￣)ノ', '(°▽°)/', '( ´ ∀ ` )ﾉ', '(^-^*)/', '(＠´ー`)ﾉﾞ', '(´• ω •`)ﾉ',
                         '( ° ∀ ° )ﾉﾞ', '(*°ｰ°)ﾉ', '(・_・)ノ', '(o´ω`o)ﾉ', "ヾ(☆'∀'☆)", "ヾ(*'▽'*)", '＼(⌒▽⌒)', 'ヾ(☆▽☆)',
                         '( ´ ▽ ` )ﾉ', 'ヾ(^ω^*)', '(・∀・)ノ', '~ヾ(・ω・)', '(^０^)ノ', '(⌒ω⌒)ﾉ', '( ´ ω ` )ノﾞ', '(￣ω￣)/',
                         '(≧▽≦)/', '(✧∀✧)/', '(o´▽`o)ﾉ', '(￣▽￣)/')
        self.indifference = ("¯\_(ツ )_/¯", 'ᕕ( ᐛ )ᕗ', 'ヽ(ー_ー )ノ', 'ヽ(　￣д￣)ノ', '┐(‘～` )┌', 'ヽ(´ー` )┌', 'ヽ(ˇヘˇ)ノ',
                             '┐(￣ヘ￣)┌', '╮(￣_￣)╭', 'ヽ(￣～￣　)ノ', '┐(￣ヮ￣)┌', '╮(￣～￣)╭')


    # Handles the incoming keyboard querys
    def query_handling(self, update, context):
        query = update.callback_query.data

        if query.startswith("kaomoji"):
            self.kaomoji_buttons(update, context)
        elif query.startswith("smiley"):
            self.kaomoji_buttons_send(update, context)

    # Displays the help keyboard
    def start(self, update, context):
        up_msg = update.message

        start_text = "Hello!\nI am the Kaomoji Bot.\nTo look at the smiley index use /kaomoji"

        if up_msg.chat.type == "private":
            up_msg.reply_text(start_text)

    def help(self, update, context):
        up_msg = update.message

        help_text = "To look at the smiley index use /kaomoji"

        up_msg.reply_text(help_text)

    # Displays the kamoji selection keyboard
    def kamoji_keyboard(self, update, context):
        up_msg = update.message
        up_msg_id = update.message.message_id

        if up_msg.reply_to_message:
            context.user_data['reply_id'] = up_msg.reply_to_message.message_id
        else:
            pass

        size_of_mood = len(self.mood)

        keyboard_kamoji = [[InlineKeyboardButton(self.mood[2 * x + j], callback_data="kaomoji_" + self.mood[2 * x + j])
                            for j in range(2)] for x in range(int(size_of_mood/2))]

        reply_markup = InlineKeyboardMarkup(keyboard_kamoji)

        context.user_data['message_id'] = up_msg_id

        up_msg.reply_text('Hewwo QT!\nPick a feeling:', reply_markup=reply_markup)

    # Displays all the kamoji from the specific smiley category
    def kaomoji_buttons(self, update, context):
        query_data = update.callback_query.data
        query_id = update.callback_query.message.chat_id
        query_msg_id = update.callback_query.message.message_id


        # If user chooses joy start kamoji process

        for i in self.mood:
            if i in query_data:
                size_of_tuple = len(getattr(self, i))
                category_smiley = [[InlineKeyboardButton(getattr(self, i)[3 * x + j], callback_data="smiley_" + i +
                                                                                                    "_{}".format(3 * x +
                                                                                                                 j))
                                    for j in range(3)] for x in range(int(size_of_tuple/3))]

                # Edit existing with the kamoji table
                context.bot.edit_message_reply_markup(chat_id=query_id, message_id=query_msg_id,
                                                      reply_markup=InlineKeyboardMarkup(category_smiley))



    # Send the smiley either as a normal message or reply
    def kaomoji_buttons_send(self, update, context):
        query_data = update.callback_query.data
        query_id = update.callback_query.message.chat_id
        query_msg_id = update.callback_query.message.message_id

        # Function for sending the kamoji
        def bot_send_it(joy_smile):
            # Deletes the selection message
            try:
                context.bot.delete_message(chat_id=query_id, message_id=query_msg_id)
            except:
                pass

            # Deletes the CommandHandler Message
            try:
                context.bot.delete_message(chat_id=query_id, message_id=context.user_data['message_id'])
            except:
                pass

            # When reply data exist send the kamoji per reply
            if context.user_data.get('reply_id'):  # .get('reply_id')
                context.bot.send_message(reply_to_message_id=context.user_data['reply_id'], chat_id=query_id,
                                         text=joy_smile)
            else:
                # Else send it it like a normal message
                context.bot.send_message(chat_id=query_id, text=joy_smile)


            context.user_data.clear()

        # If user chooses a kaomoji check if smiley is in callback_data
        if 'smiley' in query_data:

            # Split callback_data into segments
            name_callback, mood_callback, number_callback = query_data.split("_")

            # Check if callback_data has the kaomoji table the start bot_send_it function
            for i in self.mood:
                if mood_callback == i:
                    bot_send_it(getattr(self, i)[int(number_callback)])

    def inlinequery(self, update, context):
        """Handle the inline query."""

        query = update.inline_query.query
        results = [
            InlineQueryResultArticle(
                id=uuid4(),
                title="shrug\t\t\t" + str(self.indifference[0]),
                input_message_content=InputTextMessageContent(self.indifference[0])),
            InlineQueryResultArticle(
                id=uuid4(),
                title="kiss\t\t\t" + str(self.love[13]),
                input_message_content=InputTextMessageContent(self.love[13])),
            InlineQueryResultArticle(
                id=uuid4(),
                title="sad\t\t\t" + str(self.sadness[5]),
                input_message_content=InputTextMessageContent(self.sadness[5])),
            InlineQueryResultArticle(
                id=uuid4(),
                title="confused\t\t\t" + str(self.confusion[19]),
                input_message_content=InputTextMessageContent(self.confusion[19])),
            InlineQueryResultArticle(
                id=uuid4(),
                title="joy\t\t\t" + str(self.joy[0]),
                input_message_content=InputTextMessageContent(self.joy[0])),
            InlineQueryResultArticle(
                id=uuid4(),
                title="greet\t\t\t" + str(self.greeting[10]),
                input_message_content=InputTextMessageContent(self.greeting[10])),
            InlineQueryResultArticle(
                id=uuid4(),
                title="angry\t\t\t" + str(self.anger[17]),
                input_message_content=InputTextMessageContent(self.anger[17]))]

        update.inline_query.answer(results)
