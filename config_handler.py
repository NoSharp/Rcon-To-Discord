import toml


class Server:
    def __init__(self, ip, game_port, rcon_port, rcon_password):
        self._ip = ip
        self._game_port = game_port
        self._rcon_port = rcon_port
        self._rcon_password = rcon_password

    def get_ip(self) -> str:
        return self._ip

    def get_game_port(self) -> str:
        return self._game_port

    def get_rcon_port(self) -> str:
        return self._rcon_port

    def get_rcon_password(self) -> str:
        return self._rcon_password


class Config:
    def __init__(self):
        self._raw_source = str(open("config/config.toml"))
        self._toml = toml.loads(self._raw_source)

    def get_server(self) -> Server:
        servers = []
        path = self._toml["server"]

        servers.append(Server(path["ip"], path["game_port"], path["rcon_port"], path["rcon_password"]))
        return servers

    def get_timestamp(self) -> str:
        return self._toml["timestamp"]

    def get_target_channel(self) -> str:
        return self._toml["target_channel"]

    def get_command(self) -> str:
        return self._toml["command"]

    def get_rank_name(self) -> str:
        return self._toml["rank_name"]

    def get_on_command_success(self) -> str:
        return self._toml["on_command_success"]

    def get_on_command_no_permission(self) -> str:
        return self._toml["on_command_no_permission"]

    def get_discord_token(self) -> str:
        return self._toml["discord_token"]
