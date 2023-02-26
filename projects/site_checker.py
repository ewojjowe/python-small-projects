import urllib.request as urllib

def check_site(site_link):
    print(f'Checking site {site_link}...')

    try:
        response = urllib.urlopen(site_link)
        connection_code = response.getcode()
        print(f'Successfully connected to {site_link}')
        print(f'Response code is {connection_code}')

    except Exception as e:
        print(f'Can\'t establish connection for {site_link} for now, please try again later.')

if __name__ == "__main__":
    print("This is a site connection checker.")
    site_link = input("Please enter the site to check: ")

    check_site(site_link)
