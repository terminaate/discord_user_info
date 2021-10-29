from datetime import datetime


def convertIDtoUnix(id_d: str) -> int:
	bin_bin = bin(int(id_d))[2:]
	m = 64 - len(bin_bin)
	unixbin = bin_bin[0:42-m]
	unix = int(unixbin, 2)+1420070400000
	return unix


def convert(id_d: int) -> None:
    unix: int = convertIDtoUnix(str(id_d))
    timestamp = unix/1000
    date_twentyFour = str(datetime.fromtimestamp(timestamp)).split('.')[0]
    return date_twentyFour
