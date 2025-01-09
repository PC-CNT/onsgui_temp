import os
import tkinter
import tkinter.filedialog as filedialog

import dearpygui.dearpygui as dpg


def open_input():
    root = tkinter.Tk()
    root.withdraw()
    _path = filedialog.askdirectory()
    root.destroy()
    dpg.set_value("input_dir", _path)


def open_output():
    root = tkinter.Tk()
    root.withdraw()
    _path = filedialog.askdirectory()
    root.destroy()
    dpg.set_value("output_dir", _path)


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
        dpg.add_text("入力元：　")
        dpg.add_input_text(tag="input_dir", readonly=True)
        dpg.add_button(label="Browse", callback=open_input, tag="input_browse_btn")

    with dpg.group(horizontal=True):
        dpg.add_text("出力先：　")
        dpg.add_input_text(tag="output_dir", readonly=True)
        dpg.add_button(label="Browse", callback=open_output, tag="output_browse_btn")

    with dpg.group(horizontal=True):
        dpg.add_text("個別設定：")
        dpg.add_combo(tag="title_setting", items=["未指定"], default_value="未指定", )

    with dpg.tab_bar():
        with dpg.tab(label="画像"):
            with dpg.tree_node(label="基本設定", default_open=True):
                with dpg.group(horizontal=True):
                    dpg.add_text("JPEG品質：")
                    dpg.add_slider_int(label="", default_value=100, min_value=0, max_value=100, tag="img_jpgquality_bar")
                with dpg.group(horizontal=True):
                    dpg.add_combo(("256", "192", "128"), label="色", default_value="256")
                    dpg.add_checkbox(label="PNGを減色：", tag="img_pngquantize_chk")
                    dpg.add_combo(label="色", items=("256", "192", "128"), default_value="256", fit_width=True, tag="img_pngquantize_num")
            with dpg.tree_node(label="詳細設定", default_open=True):
                dpg.add_checkbox(label="""透過形式"l","r"以外のBMPを検出しJPEGへ変換""", tag="img_bmptojpg_chk")
                dpg.add_checkbox(label="""透過形式"l","r"のBMPを検出しGIFへ変換""", tag="img_bmptogif_chk")
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(label="""一般的な非PNGの横解像度を特定の倍数にする：""", tag="img_multi_chk")
                    dpg.add_combo(label="の倍数", items=("1", "2", "3", "4",), default_value="1", fit_width=True, tag="img_multi_num",)
        with dpg.tab(label="音楽"):
            dpg.add_input_text()
        with dpg.tab(label="動画"):
            dpg.add_input_text()
        with dpg.tab(label="その他"):
            dpg.add_input_text()

    with dpg.group(horizontal=True):
        dpg.add_progress_bar(default_value=0, overlay="0%")
        dpg.add_button(label="Convert")

work_name = ""

window_title = f"ONScripter Multi Converter for {work_name} ver.2.0.0"


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
