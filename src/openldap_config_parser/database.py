from typing import Dict, List

Config = List[List[str]]


class Database:
    """
    データベースの設定を保持するためのクラス

    :param str type: Databaseのタイプ (bdb, mdb, wt, monitor, ..etc)
    :param dict config: Databaseの設定辞書
    """

    def __init__(self, type: str, config: Dict[str, Config] = None):
        self.type = type
        if config is None:
            config = {}
        self.config: Dict[str, Config] = config

    def __repr__(self):
        args = [
            f"type={repr(self.type)}",
            f"config={repr(self.config)}",
        ]
        return f"Database({', '.join(args)})"
