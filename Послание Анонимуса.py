from telethon import events
from .. import loader, utils
import os
import requests
from PIL import Image,ImageFont,ImageDraw 
import re
import io
from textwrap import wrap

def register(cb):
	cb(AnonymPMod())
	
class AnonymPMod(loader.Module):
	"""Анонимус Послание"""
	strings = {
		'name': 'Анонимус Послание',
		'usage': 'Напиши <code>.help Анонимус Послание</code>',
	}
	def __init__(self):
		self.name = self.strings['name']
		self._me = None
		self._ratelimit = []
	async def client_ready(self, client, db):
		self._db = db
		self._client = client
		self.me = await client.get_me()
		
	async def anonymcmd(self, message):
		""".anonym <реплай на сообщение/свой текст>"""
		
		ufr = requests.get("https://github.com/ANDREW1000000/ftgtools/blob/main/8693.ttf?raw=true")
		f = ufr.content
		
		reply = await message.get_reply_message()
		args = utils.get_args_raw(message)
		if not args:
			if not reply:
				await utils.answer(message, self.strings('usage', message))
				return
			else:
				txt = reply.raw_text
		else:
			txt = utils.get_args_raw(message)
		await message.edit("<b>Взлом...</b>")
		pic = requests.get("https://otvet.imgsmail.ru/download/b0370f1beaf10458105912d2d5f6dadd_i-16.jpg")
		pic.raw.decode_content = True
		img = Image.open(io.BytesIO(pic.content)).convert("RGB")
 
		W, H = img.size
		#txt = txt.replace("\n", "𓃐")
		text = "\n".join(wrap(txt, 19))
		t = text + "\n"
		#t = t.replace("𓃐","\n")
		draw = ImageDraw.Draw(img)
		font = ImageFont.truetype(io.BytesIO(f), 32, encoding='UTF-8')
		w, h = draw.multiline_textsize(t, font=font)
		imtext = Image.new("RGBA", (w+10, h+10), (255, 250, 250, 1))
		draw = ImageDraw.Draw(imtext)
		draw.multiline_text((10, 10),t,(255, 255, 255),font=font, align='left')
		imtext.thumbnail((339, 181))
		w, h = 339, 181
		img.paste(imtext, (10,10), imtext)
		out = io.BytesIO()
		out.name = "anonym.jpg"
		img.save(out)
		out.seek(0)
		await message.client.send_file(message.to_id, out, reply_to=reply)
		await message.delete()