import threading
import keyboard
from dict_analigze import dictionary
import get_text
import show
import config


def tanslate():

    config.word = get_text.copy_selected_text().lower().strip()
    print(f'拿到选中的单词: {config.word}')

    dictionary_1.look_up(config.word)

    config.flag = not config.flag
    show.showing()

def hot_key():
    keyboard.add_hotkey('ctrl+f1', tanslate)

    # 定义一个函数，在另一个线程中异步监听键盘事件
    def async_listen():
        keyboard.wait()

    # 在新线程中异步监听键盘事件
    threading.Thread(target=async_listen).start()

if __name__ == '__main__':
    hot_key()
    dictionary_1 = dictionary()
    window = show.pageset()

