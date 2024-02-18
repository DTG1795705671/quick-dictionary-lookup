import webview
from pynput.mouse import Listener
import config
"""
An example of serverless app architecture
"""


class Api:
    def addItem(self, title):
        print('Added item %s' % title)

    def removeItem(self, item):
        print('Removed item %s' % item)

    def editItem(self, item):
        print('Edited item %s' % item)

    def toggleItem(self, item):
        print('Toggled item %s' % item)

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()

def pageset():
    api = Api()
    global window
    # 加载页面时添加禁用缓存的 HTTP 标头
    headers = {'Cache-Control': 'no-store'}
    window = webview.create_window('word',
                          config.temp_worditem_save_url_2,
                          js_api=api,
                          width=500,
                          height=350,
                          frameless=True,
                          easy_drag=True,
                          focus=False)
    window.events.minimized += hide
    webview.start(hide)
    return window


# def processing_of_show():
#     p = multiprocessing.Process(target=pageset)
#     p.start()

def hide():
    window.minimize()
    window.hide()


# 定义鼠标点击事件处理函数
def on_click(x, y, button, pressed):
    if pressed:
        hide()
        return False


def showing():
    window.set_title(config.word)
    if config.flag:
        window.load_url(config.temp_worditem_save_url)
    else:
        window.load_url(config.temp_worditem_save_url_2)
    window.show()
    window.restore()
    # 创建鼠标监听器
    with Listener(on_click=on_click) as listener:
        listener.join()






if __name__ == '__main__':
    api = Api()
    window = webview.create_window('Todos magnificos',
                          "file:///C:/Users/l'w'y/Desktop/新建文件夹/2.html",
                          js_api=api,
                          width=500,
                          height=350,
                          frameless=False,
                          easy_drag=True,
                          focus=False)
    # window.events.closing += on_closing
    webview.start()
    print('已经开始了')


