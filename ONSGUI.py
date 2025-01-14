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
            with dpg.tree_node(label="基本設定", default_open=True):
                with dpg.tree_node(label="ファイル関連", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("画像圧縮先：")
                        dpg.add_combo(
                            label="",
                            items=("arc.nsa", "arc1.nsa", "arc2.nsa", "圧縮しない"),
                            default_value="arc.nsa",
                            fit_width=True,
                            tag="etc_filecompimg_nsa",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("BGM圧縮先：")
                        dpg.add_combo(
                            label="",
                            items=("arc.nsa", "arc1.nsa", "arc2.nsa", "圧縮しない"),
                            default_value="arc1.nsa",
                            fit_width=True,
                            tag="etc_filecompbgm_nsa",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("SE/VOICE圧縮先：")
                        dpg.add_combo(
                            label="",
                            items=("arc.nsa", "arc1.nsa", "arc2.nsa", "圧縮しない"),
                            default_value="arc2.nsa",
                            fit_width=True,
                            tag="etc_filecompse_nsa",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="""拡張子".dll"のファイルを全て除外""",
                            default_value=True,
                            tag="etc_fileexdll_chk",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="""ファイル"Thumbs.db"を全て除外""",
                            default_value=True,
                            tag="etc_fileexdb_chk",
                        )
                with dpg.tree_node(label="ons.ini関連(PSP用)", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("画面表示：")
                        dpg.add_combo(
                            label="",
                            items=("拡大しない", "拡大(比率維持)", "拡大(フルサイズ)"),
                            default_value="拡大(比率維持)",
                            fit_width=True,
                            tag="etc_iniscreen",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="常にメモリ内にフォントを読み込んでおく",
                            default_value=True,
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="マウスカーソルを利用",
                            default_value=False,
                        )
            with dpg.tree_node(label="詳細設定", default_open=True):
                with dpg.tree_node(label="0.txt関連", default_open=True):
                    with dpg.group(horizontal=True):
                        dpg.add_text("nbz変換設定：")
                        dpg.add_radio_button(
                            items=(
                                "変換後のファイルを拡張子nbzとwavで両方用意しておく",
                                """0.txtを".nbz"→".wav"で一括置換""",
                            ),
                            default_value="""0.txtを".nbz"→".wav"で一括置換""",
                            horizontal=True,
                            tag="etc_0txtnbz_radio",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("avi命令→mpegplay命令変換：")
                        dpg.add_combo(
                            items=(
                                "利用する(関数上書き)",
                                "利用する(正規表現置換)",
                                "利用しない",
                            ),
                            default_value="利用する(関数上書き)",
                            fit_width=True,
                            tag="etc_0txtavitompegplay",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_text("screenshot系命令無効化：")
                        dpg.add_combo(
                            items=(
                                "利用する(関数上書き)",
                                "利用する(正規表現置換)",
                                "利用しない",
                            ),
                            default_value="利用する(関数上書き)",
                            fit_width=True,
                            tag="etc_0txtnoscreenshot",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="低容量RAM搭載端末用maxkaisoupage最大値指定：",
                            default_value=True,
                            tag="etc_0txtmaxkaisoupage_chk",
                        )
                        dpg.add_combo(
                            items=("1", "3", "5", "10", "20"),
                            default_value="3",
                            fit_width=True,
                            tag="etc_0txtmaxkaisoupage_num",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="低解像度端末用setwindow/setwindow3文字潰れ防止",
                            default_value=True,
                            tag="etc_0txtsetwindowbigfont_chk",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="okcancelbox命令強制ok",
                            default_value=True,
                            tag="etc_0txtskipokcancelbox_chk",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="yesnobox命令強制yes",
                            default_value=True,
                            tag="etc_0txtskipyesnobox_chk",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="rnd2命令→rnd命令変換",
                            default_value=True,
                            tag="etc_0txtrndtornd2_chk",
                        )
                    with dpg.group(horizontal=True):
                        dpg.add_checkbox(
                            label="変換ファイル総数/処理時間/設定を末尾に記載",
                            default_value=True,
                            tag="etc_0txtresult0txt_chk",
                        )
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
