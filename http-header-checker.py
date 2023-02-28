import requests
import argparse
import os

# Define the HTTP security headers we're interested in checking for
http_security_headers = [
    'Strict-Transport-Security',
    'X-Frame-Options',
    'X-XSS-Protection',
    'X-Content-Type-Options',
    'Content-Security-Policy',
    'Referrer-Policy'
]

def check_security_headers(url):
    """
    Given a URL, checks for the presence of HTTP security headers.
    Returns a dictionary of security headers, where each key is a security header
    and each value is a boolean indicating whether the header is present or not.
    """
    response = requests.get(url)
    headers = {}
    for header in http_security_headers:
        headers[header] = header in response.headers
    return headers

def check_urls(urls):
    """
    Given a list of URLs, checks each URL for the presence of HTTP security headers.
    Prints the headers for each URL, indicating which headers are present and which are missing.
    """
    for url in urls:
        if not url.startswith('http://') and not url.startswith('https://'):
            print(f"Skipping invalid URL '{url}': URL must start with 'http://' or 'https://'.")
            continue
        try:
            headers = check_security_headers(url)
            all_headers_present = all(headers.values())
            if all_headers_present:
                print('\033[33m' + f"All HTTP security headers are active for {url}" + '\033[0m')
            else:
                print(f"Security headers for {url}:")
                for header, present in headers.items():
                    color = '\033[32m' if present else '\033[31m'
                    print(f"{color}{header}: {present}\033[0m")
        except requests.exceptions.RequestException:
            print(f"Unable to access {url}")

def write_output(output, filename):
    """
    Given an output string and a filename, writes the output to a file with the given filename.
    """
    with open(filename, 'w') as f:
        f.write(output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check HTTP security headers for a list of URLs.')
    parser.add_argument('-t', '--url', help='URL to check')
    parser.add_argument('-l', '--url-list', help='File containing a list of URLs to check')
    parser.add_argument('-o', '--output', help='File to write output to')
    args = parser.parse_args()

    urls = []
    if args.url:
        urls.append(args.url)
    if args.url_list:
        with open(args.url_list, 'r') as f:
            urls.extend([line.strip() for line in f])

    check_urls(urls)

    if args.output:
        output = '\n'.join(urls) + '\n\n'
        for url in urls:
            try:
                headers = check_security_headers(url)
                output += f"Security headers for {url}:\n"
                for header, present in headers.items():
                    color = '\033[32m' if present else '\033[31m'
                    output += f"{color}{header}: {present}\033[0m\n"
                output += '\n'
            except requests.exceptions.RequestException:
                output += f"Unable to access {url}\n\n"
        write_output(output, args.output)
