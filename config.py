import os

GAME_SERVER_IP = os.environ.get("GAME_SERVER_IP", "66.33.22.2")
ROUTE_PREFIX = os.environ.get("ROUTE_PREFIX", "")
HTTP_PORT = os.environ.get("HTTP_PORT", "8000")
DATABASE_PATH = os.environ.get("DATABASE_PATH", "zewmsm.db")
HOME = os.environ.get("HOME", ".")
