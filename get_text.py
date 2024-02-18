import pyperclip
import pyautogui
import time
import keyboard

def copy_selected_text():
    # 模拟按下Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    # 等待剪贴板更新
    time.sleep(0.5)
    # 获取剪贴板中的内容
    clipboard_text = pyperclip.paste()

    return clipboard_text

if __name__ == "__main__":
    # 监听Ctrl+Alt+C按键事件
    keyboard.add_hotkey('ctrl+1', copy_selected_text)

    # 运行一个无限循环，保持监听状态
    keyboard.wait('esc')
