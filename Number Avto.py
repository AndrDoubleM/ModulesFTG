from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
def register(cb):
    cb(NumberAvtoMod())
class NumberAvtoMod(loader.Module):
    """Number Avto"""
    strings = {'name': 'Number Avto'}
    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []
    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()
    async def ruavtocmd(self, message):
        """.ruavto
            Пробив номера автомобиля в РФ
        """
        reply = await message.get_reply_message()
        if not reply:
            if utils.get_args_raw(message):
                user = utils.get_args_raw(message)
            else:
                await message.edit("<b>Куда пропал номер авто?</b>")
                return
        else:
            try:
                user = str(reply.text)
            except:
                await message.edit("<b>Err</b>")
                return
        await message.edit("<b>Пробив...</b>")
        chat = '@avtocodbot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Ожидаем ответ...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=278322988))
                m1 = await message.client.send_message(chat, "{0}".format(user))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()
    async def uaavtocmd(self, message):
        """.uaavto
            Пробив автомобиля в Украине
        """
        reply = await message.get_reply_message()
        if not reply:
            if utils.get_args_raw(message):
                name = utils.get_args_raw(message)
            else:
                await message.edit("<b>Куда пропал номер авто?</b>")
                return
        else:
            try:
                name = str(reply.text)
            except:
                await message.edit("<b>Err</b>")
                return
        await message.edit("<b>Пробив...</b>")
        chat = '@OpenDataUABot'
        async with message.client.conversation(chat) as conv:
            try:
                await message.edit("<b>Ожидаем ответ...</b>")
                response = conv.wait_event(events.NewMessage(incoming=True, from_users=215115043))
                m1 = await message.client.send_message(chat, "{0}".format(name))
                m2 = response = await response
            except YouBlockedUserError:
                await message.edit('<code>Unblock</code> ' + chat)
                return
            await m1.delete()
            if(response.text.startswith("⚠️")):
                await message.edit("⚠️ Ничего не найдено")
            else:
                await message.edit(response.text)
            await m2.delete()