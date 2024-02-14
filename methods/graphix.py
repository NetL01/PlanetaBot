from io import BytesIO

import numpy as np
from matplotlib import pyplot as plt
from config import bot


def graphix(message):
    try:
        args = message.text.split()[1:]
        func_string = ' '.join(args)

        def func(x):
            return eval(func_string)

        x = np.linspace(-10, 10, 400)
        y = func(x)

        plt.figure()
        plt.plot(x, y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(f'График функции {func_string}')

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        bot.send_photo(message.chat.id, photo=buffer)

        buffer.close()
        plt.close()

    except Exception as e:
        bot.reply_to(message, f'Ошибка: {str(e)}')
