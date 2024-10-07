from json import loads
from bs4 import BeautifulSoup
from requests import get
from log import log_out

"""
-   src/grab_id.py
-   Author: @kexecq
-   Date: 01/10/2024
"""

def grab_board_id(url: str) -> str:
    """Grabs the board id from the HTML.

    Args:
        url (str) The board URL to grab the board id from.

    Returns:
        board_id (str) The board id.
    """

    USER_AGENT = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1"

    soup = BeautifulSoup(get(f"{url}", 
        headers={"User-Agent": USER_AGENT}).text, 'html.parser')
    
    script = soup.find("script", {"id": "__PWS_INITIAL_PROPS__"})
    board_id = loads(script.string)

    """ Returns the board id from the parsed json. """
    log_out(f"grabbed board id -> {next(iter(board_id['initialReduxState']['boards']))}")
    return next(iter(board_id["initialReduxState"]["boards"]))


if __name__ == "__main__":
    grab_board_id(input("[pinpy]: input the board URL: "))
