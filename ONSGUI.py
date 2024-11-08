import os
import tkinter
import tkinter.filedialog as filedialog

import dearpygui.dearpygui as dpg


def open_input():
    root = tkinter.Tk()
    root.withdraw()
    _path = filedialog.askdirectory()
    root.destroy()
    dpg.set_value("input", _path)


def open_output():
    root = tkinter.Tk()
    root.withdraw()
    _path = filedialog.askdirectory()
    root.destroy()
    dpg.set_value("output", _path)


def close():
    dpg.stop_dearpygui()


def garbro():
    print("GARbro")
    return


def copyrights():
    print("copyrights")
    return


dpg.create_context()

font_path = r"C:\Windows\Fonts\ipaexg.ttf"

with dpg.font_registry():
    with dpg.font(file=font_path, size=18) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)
    dpg.bind_font(default_font)
    with dpg.font(file=font_path, size=14) as small_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Japanese)

with dpg.window(label="Main Window", tag="Main Window"):
    with dpg.menu_bar():
        with dpg.menu(label="設定"):
            with dpg.menu(label="ハード変更"):
                dpg.add_menu_item(label="SONY PlayStation Portable")
                dpg.add_menu_item(label="SONY PlayStation Vita")
                dpg.add_menu_item(label="その他(Android/Linux/WinCE...)")
            
            dpg.add_menu_item(label="終了", callback=close)

        with dpg.menu(label="ツール"):
            dpg.add_menu_item(label="GARbroを起動", callback=garbro)

        with dpg.menu(label="このソフトについて"):
            dpg.add_menu_item(label="権利者表記", callback=copyrights)

    with dpg.group(horizontal=True):
        dpg.add_text("入力元：")
        dpg.add_input_text(tag="input", readonly = True)
        dpg.add_button(label="Browse", callback=open_input)

    with dpg.group(horizontal=True):
        dpg.add_text("出力先：")
        dpg.add_input_text(tag="output", readonly = True)
        dpg.add_button(label="Browse", callback=open_output)

    with dpg.tab_bar():
        with dpg.tab(label="画像"):
            dpg.add_input_text()
        with dpg.tab(label="音楽"):
            dpg.add_input_text()
        with dpg.tab(label="動画"):
            dpg.add_input_text()
        with dpg.tab(label="その他"):
            dpg.add_input_text()

    with dpg.group(horizontal=True):
        dpg.add_progress_bar(default_value=0, overlay="0%")
        dpg.add_button(label="Convert")

window_title = "ONScripter Multi Converter for ver.2.0.0"


def main():
    dpg.create_viewport(title=window_title, width=1280, height=720)
    dpg.set_primary_window("Main Window", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
