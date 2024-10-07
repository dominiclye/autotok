"""
    Copyright (c) 2024 kexecq

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from colorama import Fore
from grab_id import grab_board_id
from download import download

"""
-   src/pinpy.py
-   Date: 30/09/2024
-   Author: @kexecq
"""

def main(url: str, save_directory: str):
    print(f"""                              
{Fore.RED}       (                 (    {Fore.RESET}
{Fore.RED} `  )  )\   (     `  )   )\ ) {Fore.RESET}
{Fore.RED} /(/( ((_)  )\ )  /(/(  (()/( {Fore.RESET}
{Fore.RED}((_)_\ (_) _(_/( ((_)_\  )(_)){Fore.RESET}
{Fore.RED}| '_ \)| || ' \))| '_ \)| || |{Fore.RESET} - pinterest scraper
{Fore.RED}| .__/ |_||_||_| | .__/  \_, |{Fore.RESET}
{Fore.RED}|_|              |_|     |__/ {Fore.RESET}
        """)
    download(grab_board_id(url), save_directory)
    
if __name__ == "__main__":
    board_url = input("[pinpy]: input the board URL: ")
    save_directory = input("[pinpy]: input directory to save images: ")
    main(board_url, save_directory)
