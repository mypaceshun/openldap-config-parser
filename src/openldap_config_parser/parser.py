from pathlib import Path

from openldap_config_parser.config import Directive, SlapdConfig
from openldap_config_parser.exceptions import SlapdConfigParserError


def parse(target: Path):
    """
    slapd.confをパースし、設定を保持したSlapdConfigクラスを返す。

    Args:
        target (Path): パースする設定ファイルのパス

    Returns:
        SlapdConfig: 読み込んだ設定ファイルの内容
    """
    lines = read_config_file(target)
    directive_list = parse_directive(lines)
    config = SlapdConfig()
    current_database_no = -1  # global
    for directive in directive_list:
        if directive["directive"] == "database":
            dbtype = directive["args"][0]
            config.add_database(dbtype)
            current_database_no += 1
            continue
        config.add_directive(directive, current_database_no)
    return config


def parse_directive(lines: list[str]):
    """
    各行の文字列のリストをディレクティブと引数の関係に分ける。
    空白やタブから始まる行は前の行の引数となる。

    Args:
        lines (list[str]): 各行の文字列のリスト

    Returns:
        list[Directive]: ディレクティブのリスト
    """
    directive_list: list[Directive] = []
    for line in lines:
        _line = line.strip()
        args = _line.split(" ")
        if line.startswith(" "):
            if len(directive_list) == 0:
                msg = f"Directive not found [{line}]"
                raise SlapdConfigParserError(msg)
            current_directive = directive_list[-1]
            current_directive["args"] += args
        else:
            directive = args[0]
            _args = [a for a in args[1:] if len(a) > 0]
            directive_list.append({"directive": directive, "args": _args})
    return directive_list


def read_config_file(target: Path) -> list[str]:
    """
    設定ファイルを読み込み、各行を文字列のリストとして返す。
    このとき空白行やコメント行は除外する。

    Args:
        target (Path): 読み込む設定ファイルのパス

    Returns:
        list[str]: 読み込んだファイルの各行の文字列のリスト
    """
    lines = []
    with target.open() as fd:
        for line in fd:
            _line = line.strip()
            if len(_line) == 0:
                # brank line
                continue
            if _line.startswith("#"):
                # comment
                continue
            lines.append(line.replace("\t", " "))
    return lines
