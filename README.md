# woc-dl
Python script to download profiles from worldcosplay.net

## Requirements

- Python 3.6+

- Requests library (install with `pip install requests`)

## Usage

You can suply multiple URLs or text files (with profile URLs, one per line). It can download private profiles if you edit the script and add your `authenticity_token` cookie.

Downloading a single profile:

`python woc-dl.py https://worldcosplay.net/member/458618`

Downloading multiple profiles:

`python woc-dl.py https://worldcosplay.net/member/458618 https://worldcosplay.net/member/1396`

Downloading from a text file:

`python woc-dl.py profiles.txt`

Downloading from a text file and URL:

`python woc-dl.py profiles.txt https://worldcosplay.net/member/728676`

It will create a directory named 'World of Cosplay' and inside will create directories for each profile in the form of `{username} ({user_id})`.
