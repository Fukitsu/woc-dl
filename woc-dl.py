import re
import os
import sys
import requests
import concurrent.futures


authenticity_token = ''


def download(link):    
    with open(link.split('/')[4], 'wb') as f:
        f.write(requests.get(link).content)


def scrape(arg):
    cd = os.getcwd()
    user_id = arg.split('/')[4]
    next_page = '1'
    image_links = []

    r = requests.get(f'https://worldcosplay.net/api/member/photos.json?limit=1&member_id={user_id}&authenticity_token={authenticity_token}').text
    username = re.search(r"\"global_name\":\"(.*?)\"", r).group(1)
    print(f'Downlading: {username} User ID: {user_id}')

    while next_page != 'null':
        page = requests.get(f'https://worldcosplay.net/api/member/photos.json?limit=16&member_id={user_id}&page={next_page}&age_filter=0&authenticity_token={authenticity_token}').text
        next_page = re.search(r'\"next_page\":(\w+)', page).group(1)
        [image_links.append(i) for i in re.findall(r'\"img_url\":\"(.*?)\",', page)]

    if not os.path.isdir('World of Cosplay'):
        os.makedirs('World of Cosplay')
    os.chdir('World of Cosplay')

    user_dir = f'{username} ({user_id})'
    if not os.path.isdir(user_dir):
        os.makedirs(user_dir)
    os.chdir(user_dir)

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(download, image_links)    

    print(f'Finished downloading {len(image_links)} pictures')
    os.chdir(cd)


def main():
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            with open(arg, 'r') as f:
                for line in f:
                    scrape(line.strip())
        else:
            scrape(arg)


if __name__ == '__main__':
    main()
