import sqlite3
import aiosmtplib

import asyncio
import time


con = sqlite3.connect('contacts.db')
emails = [mail[0] for mail in con.execute("select email from contacts").fetchall()]

EMAIL_SERVER_HOST = '89.108.79.53'
PORT = 1025

SUBJECT = 'TestMail'
FROM = 'pythonTestMail@coder.com'


async def send_mail(email):
    await aiosmtplib.send(
        message=f'From: {FROM}\n'
                f'To: {email}\n'
                f'Subject: {SUBJECT}\n'
                f'\n'
                f'Уважаемый {email}! Спасибо, что пользуетесь нашим сервисом объявлений.'.encode(),
        sender=FROM,
        recipients=email,
        hostname=EMAIL_SERVER_HOST,
        port=PORT
    )


async def main():
    tasks = [asyncio.ensure_future(send_mail(email)) for email in emails[:10]]
    await asyncio.wait(tasks)


start = time.time()
event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(main())
event_loop.close()
print(time.time() - start)
