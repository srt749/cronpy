import json
import logging
from pprint import pprint
import pandas as pd
import requests

logging.basicConfig(filename='status.log', level=logging.INFO)
def main():
    print('started')
    records = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/1xBOlJmVv-aZf3dLBU3QL8OHkM2ADVTkgxriaCrccgjQ/export?format=csv').to_dict('records')
    for record in records:
        messages = []
        for lang_website in ['En_website', 'Fr_website']:
            website = record[lang_website]
            if website.startswith('www.'):
                website = 'http://' + website
            if website == 'na' or 'gov.nl.ca' in website:
                pass
            else:
                try:
                    r = requests.get(website)
                    status = r.status_code
                    if status in [200, 301]:
                        logging.info(f'Functioning correctly: {website}')
                        continue
                    else:
                        issue = {
                            'HR_UID': record['HR_UID'],
                            'Province': record['Province'],
                            'health_region': record['health_region'],
                            'url': website,
                            'status_code': r.status_code
                        }
                        messages.append(issue)
                        logging.warning(
                            f'Malfunctioning link: {website} \n Details: {issue}')
                except Exception as e:
                    logging.error(
                        f'Could not retrieve {website}.\nError details: {e}')
                    continue
    # json.dumps(messages, indent=2)
if __name__ == "__main__":
    main()