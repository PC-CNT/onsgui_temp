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
        dpg.add_combo(
            tag="title_setting",
            items=["未指定"],
            default_value="未指定",
        )

    with dpg.tab_bar():
        with dpg.tab(label="画像"):
            with dpg.tree_node(label="基本設定", default_open=True):
                with dpg.group(horizontal=True):
                    dpg.add_text("JPEG品質：")
                    dpg.add_slider_int(
                        label="",
                        default_value=100,
                        min_value=0,
                        max_value=100,
                        tag="img_jpgquality_bar",
                    )
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(label="PNGを減色：", tag="img_pngquantize_chk")
                    dpg.add_combo(
                        label="色",
                        items=("256", "192", "128"),
                        default_value="256",
                        fit_width=True,
                        tag="img_pngquantize_num",
                    )
            with dpg.tree_node(label="詳細設定", default_open=True):
                dpg.add_checkbox(
                    label="""透過形式"l","r"以外のBMPを検出しJPEGへ変換""",
                    tag="img_bmptojpg_chk",
                )
                dpg.add_checkbox(
                    label="""透過形式"l","r"のBMPを検出しGIFへ変換""",
                    tag="img_bmptogif_chk",
                )
                with dpg.group(horizontal=True):
                    dpg.add_checkbox(
                        label="""一般的な非PNGの横解像度を特定の倍数にする：""",
                        tag="img_multi_chk",
                    )
                    dpg.add_combo(
                        label="の倍数",
                        items=(
                            "1",
                            "2",
                            "3",
                            "4",
                        ),
                        default_value="1",
                        fit_width=True,
                        tag="img_multi_num",
                    )
        with dpg.tab(label="音楽"):
            with dpg.tree_node(label="基本設定", default_open=True):
                with dpg.group(horizontal=True):
                    dpg.add_text("BGMフォーマット：")
                    dpg.add_radio_button(
                        items=("OGG", "MP3", "WAV"),
                        default_value="OGG",
                        horizontal=True,
                        tag="aud_bgmfmt_radio",
                    )
                with dpg.group(horizontal=True):
                    dpg.add_text("SE/VOICEフォーマット：")
                    dpg.add_radio_button(
                        items=("OGG", "MP3", "WAV"),
                        default_value="OGG",
                        horizontal=True,
                        tag="aud_sefmt_radio",
                    )
                with dpg.group(horizontal=True):
                    dpg.add_text("SE/BGMチャンネル数：")
                    dpg.add_radio_button(
                        items=("ステレオ", "モノラル"),
                        default_value="ステレオ",
                        horizontal=True,
                        tag="aud_bgmch_radio",
                    )
                with dpg.group(horizontal=True):
                    dpg.add_text("SE/SE/VOICEチャンネル数：")
                    dpg.add_radio_button(
                        items=("ステレオ", "モノラル"),
                        default_value="モノラル",
                        horizontal=True,
                        tag="aud_sech_radio",
                    )
            with dpg.tree_node(label="詳細設定", default_open=True):
                with dpg.tree_node(label="OGG変換時", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("BGMビットレート：")
                        dpg.add_combo(
                            label="kbps",
                            items=(
                                "192",
                                "160",
                                "128",
                                "112",
                                "96",
                                "64",
                                "56",
                                "48",
                                "32",
                            ),
                            default_value="192",
                            fit_width=True,
                            tag="aud_oggbgm_kbps",
                        )
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="44100",
                            fit_width=True,
                            tag="aud_oggbgm_hz",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("SE/VOICEビットレート：")
                        dpg.add_combo(
                            label="kbps",
                            items=(
                                "192",
                                "160",
                                "128",
                                "112",
                                "96",
                                "64",
                                "56",
                                "48",
                                "32",
                            ),
                            default_value="56",
                            fit_width=True,
                            tag="aud_oggse_kbps",
                        )
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="22050",
                            fit_width=True,
                            tag="aud_oggse_hz",
                        )
                with dpg.tree_node(label="MP3変換時", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("BGMビットレート：")
                        dpg.add_combo(
                            label="kbps",
                            items=(
                                "192",
                                "160",
                                "128",
                                "112",
                                "96",
                                "64",
                                "56",
                                "48",
                                "32",
                            ),
                            default_value="128",
                            fit_width=True,
                            tag="aud_mp3bgm_kbps",
                        )
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="44100",
                            fit_width=True,
                            tag="aud_mp3bgm_hz",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("SE/VOICEビットレート：")
                        dpg.add_combo(
                            label="kbps",
                            items=(
                                "192",
                                "160",
                                "128",
                                "112",
                                "96",
                                "64",
                                "56",
                                "48",
                                "32",
                            ),
                            default_value="96",
                            fit_width=True,
                            tag="aud_mp3se_kbps",
                        )
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="22050",
                            fit_width=True,
                            tag="aud_mp3se_hz",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("BGMカットオフ周波数：")
                        dpg.add_combo(
                            label="Hz",
                            items=(
                                "18000",
                                "16500",
                                "15000",
                                "13500",
                                "12000",
                                "10500",
                                "9000",
                                "7500",
                            ),
                            default_value="15000",
                            fit_width=True,
                            tag="aud_mp3bgm_cutoff",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("SE/VOICEカットオフ周波数：")
                        dpg.add_combo(
                            label="Hz",
                            items=(
                                "18000",
                                "16500",
                                "15000",
                                "13500",
                                "12000",
                                "10500",
                                "9000",
                                "7500",
                            ),
                            default_value="12000",
                            fit_width=True,
                            tag="aud_mp3se_cutoff",
                        )
                with dpg.tree_node(label="WAV変換時", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("BGMビットレート：")
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="44100",
                            fit_width=True,
                            tag="aud_wavbgm_hz",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("SE/VOICEビットレート：")
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="22050",
                            fit_width=True,
                            tag="aud_wavse_hz",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("BGMコーデック：")
                        dpg.add_radio_button(
                            items=("pcm_s16le", "pcm_u8"),
                            default_value="pcm_s16le",
                            horizontal=True,
                            tag="aud_bgmcodec_radio",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("SEコーデック：")
                        dpg.add_radio_button(
                            items=("pcm_s16le", "pcm_u8"),
                            default_value="pcm_s16le",
                            horizontal=True,
                            tag="aud_secodec_radio",
                        )
        with dpg.tab(label="動画"):
            with dpg.tree_node(label="基本設定", default_open=True):
                with dpg.group(horizontal=True):
                    dpg.add_text("動画フォーマット：")
                    dpg.add_radio_button(
                        items=("連番画像", "MJPEG", "MP4", "変換しない"),
                        default_value="連番画像",
                        horizontal=True,
                        tag="vid_movfmt_radio",
                    )
            with dpg.tree_node(label="詳細設定", default_open=True):
                with dpg.tree_node(label="連番画像変換時", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("画像フォーマット：")
                        dpg.add_radio_button(
                            items=("PNG", "JPEG"),
                            default_value="PNG",
                            horizontal=True,
                            tag="vid_renbanfmt_radio",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("解像度 - %指定：")
                        dpg.add_radio_button(
                            items=(
                                "100%(1/1)",
                                "75%(3/4)",
                                "66%(2/3)",
                                "50%(1/2)",
                                "33%(1/3)",
                                "25%(1/4)",
                            ),
                            default_value="100%(1/1)",
                            horizontal=True,
                            tag="vid_renbanres_radio",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("PNG利用時減色：")
                        dpg.add_combo(
                            label="色",
                            items=("256", "128", "64", "32"),
                            default_value="256",
                            fit_width=True,
                            tag="vid_renbanpngquantize_chk",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("JPEG利用時品質：")
                        dpg.add_slider_int(
                            label="",
                            default_value=90,
                            min_value=0,
                            max_value=100,
                            tag="vid_renbanjpgquality_bar",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("音声変換時の設定：")
                        dpg.add_radio_button(
                            items=("BGMに合わせる", "SE/VOICEに合わせる"),
                            default_value="BGMに合わせる",
                            horizontal=True,
                            tag="vid_renbanaudset_radio",
                        )
                with dpg.tree_node(label="MJPEG変換時", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("動画品質 - 数字が少ないほど高品質：")
                        dpg.add_slider_int(
                            label="",
                            default_value=8,
                            min_value=1,
                            max_value=30,
                            tag="vid_mjpegquality_bar",
                        )
                with dpg.tree_node(label="MP4変換時", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("動画品質 - 数字が少ないほど高品質：")
                        dpg.add_slider_int(
                            label="",
                            default_value=4,
                            min_value=1,
                            max_value=30,
                            tag="vid_mp4quality_bar",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("音声ビットレート：")
                        dpg.add_combo(
                            label="kbps",
                            items=(
                                "192",
                                "160",
                                "128",
                                "112",
                                "96",
                                "64",
                                "56",
                                "48",
                                "32",
                            ),
                            default_value="160",
                            fit_width=True,
                            tag="vid_mp4aud_kbps",
                        )
                        dpg.add_combo(
                            label="Hz",
                            items=("44100", "22050", "11025"),
                            default_value="44100",
                            fit_width=True,
                            tag="vid_mp4aud_hz",
                        )

        with dpg.tab(label="その他"):
            dpg.add_input_text()

    with dpg.group(horizontal=True):
        dpg.add_progress_bar(default_value=0, overlay="0%")
        dpg.add_button(label="Convert")

work_name = ""

window_title = f"ONScripter Multi Converter for {work_name} ver.2.0.0"


def main():
    dpg.create_viewport(title=window_title, width=1280, height=720, resizable=False)
    dpg.set_primary_window("Main Window", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    main()
