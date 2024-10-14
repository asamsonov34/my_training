def send_email(msg, recipient, sender = 'university.help@gmail.com'):
    for addr in [sender, recipient]:
        if not ('@' in addr and ('.com' in addr or '.ru' in addr or '.net' in addr)):
            print('Cannot send from <', sender, '> to <', recipient,
                  '>: invalid email address for sender and/or recipient.', sep = '')
            return
    if sender == recipient:
        print('Email not sent: cannot send to self.')
        return
    if sender != 'university.help@gmail.com':
        print('IRREGULAR SENDER! Email has been sent from <', sender, '> to <', recipient, '>.', sep = '')
    else:
        print('Email has been sent successfully from <', sender, '> to <', recipient, '>.', sep = '')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')