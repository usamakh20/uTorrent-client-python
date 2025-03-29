import sys
import time

from app.utorrentapi import UTorrentAPI

# Configure uTorrent WebUI connection
UTORRENT_URL = "http://127.0.0.1:35678/gui"
USERNAME = "admin"
PASSWORD = "admin"


def get_torrent_client():
    """Initialize and return the uTorrent client."""
    return UTorrentAPI(UTORRENT_URL, USERNAME, PASSWORD)


def stop_all_torrents(client: UTorrentAPI):
    """Stop all torrents."""
    for torrent in client.get_list()['torrents']:
        client.stop(torrent[0])
    print("✅  Stopped all torrents.")


def force_start_and_update_trackers(client: UTorrentAPI):
    """Force start all torrents and update trackers."""
    for torrent in client.get_list()['torrents']:
        client.forcestart(torrent[0])
    print("✅  Force started all torrents")


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["stop", "start"]:
        print("Usage: python script.py <stop|start>")
        sys.exit(1)

    client = get_torrent_client()

    if sys.argv[1] == "stop":
        stop_all_torrents(client)
    elif sys.argv[1] == "start":
        force_start_and_update_trackers(client)


if __name__ == "__main__":
    main()
