from typing import TypedDict

from openldap_config_parser.database import Config, Database


class Directive(TypedDict):
    directive: str
    args: list[str]


class SlapdConfig:
    """SlapdConfig

    slapd.conf の設定を保持するためのクラス

    :param dict[str, Config] global_config: globalの設定辞書
    :param list[Database] databases: データベースの設定クラスのリスト
    """

    def __init__(
        self, global_config: dict[str, Config] = None, databases: list[Database] = None
    ):
        if global_config is None:
            global_config = {}
        self.global_config: dict[str, Config] = global_config
        if databases is None:
            databases = []
        self.databases: list[Database] = databases

    def __repr__(self):
        args = [
            f"global_conig={repr(self.global_config)}",
            f"databases={repr(self.databases)}",
        ]
        return f"SlapdConfig({', '.join(args)})"

    def add_database(self, dbtype: str):
        """
        databaseの追加

        Args:
            dbtype (str): Databaseのtype
        """
        self.databases.append(Database(dbtype))

    def add_directive(self, directive: Directive, database_no: int = -1):
        """
        directiveの追加。
        database_noがself.databasesの範囲外を指定している場合は、
        self.global_configに設定を追加する。

        Args:
            directive (str): 追加するディレクティブ
            args (list[str]): ディレクティブの引数リスト
            database_no (int): ディレクティブを追加するDatabaseのインデックス。
        """
        if database_no < 0 or len(self.databases) <= database_no:
            config = self.global_config
        else:
            config = self.databases[database_no].config
        key = directive["directive"]
        args = directive["args"]
        if key not in config:
            config[key] = [args]
        else:
            config[key].append(args)
