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
            directive (Directive): 追加するディレクティブ
            database_no (int): ディレクティブを追加するDatabaseのインデックス。
        """
        config = self.get_database(database_no)
        key = directive["directive"]
        args = directive["args"]
        if key not in config:
            config[key] = [args]
        else:
            config[key].append(args)

    def get_database(self, database_no: int = -1):
        """
        データベースの取得
        database_noがself.databasesの範囲外を指定している場合は、
        self.global_configに設定を追加する。

        Args:
            database_no (int): 取得するDatabaseのインデックス (Default: -1)

        Returns:
            Database: 指定したデータベースの設定データ
        """
        if database_no < 0 or len(self.databases) <= database_no:
            return self.global_config
        return self.databases[database_no].config

    def get_database_no(self, dbtype: str):
        for index, db in enumerate(self.databases):
            if dbtype == db.type:
                return index
        return -1

    def get_value(self, key: str, database_no: int = -1):
        """
        値の取得
        database_noがself.databasesの範囲外を指定している場合は、
        self.global_configから値を取得する。
        Databaseにキーが存在しなかった場合はself.global_configから値を取得する。
        self.global_configにもキーが存在しなかった場合は空リストを返します。

        Args:
            key (str): ディレクティブのキー
            database_no (int): 取得するDatabaseのインデックス (Default: -1)

        Returns:
            Config: 設定の値リスト
        """
        config = self.get_database(database_no)
        result = config.get(key, None)
        if result is None:
            return self.global_config.get(key, [])
        return result
