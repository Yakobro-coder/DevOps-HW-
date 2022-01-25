import sqlite3
import aiosmtplib

import asyncio
import time


con = sqlite3.connect('contacts.db')
emails = [mail[0] for mail in con.execute("select email from contacts").fetchall()]

EMAIL_SERVER_HOST = '127.0.0.1'
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
    tasks = [asyncio.create_task(send_mail(email)) for email in emails]
    await asyncio.wait(tasks)


start = time.time()
event_loop = asyncio.run(main())
print(time.time() - start)
