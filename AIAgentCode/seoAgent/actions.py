from SimplerLLM.tools.rapid_api import RapidAPIClient
from constant import rapid_api_key

def get_seo_page_report(url :str):
    api_url = "https://website-seo-analyzer.p.rapidapi.com/seo/seo-audit-basic"
    api_params = {
        'url': url
    }
    headers = {
        "X-RapidAPI-Key": rapid_api_key,
        "X-RapidAPI-Host": "website-seo-analyzer.p.rapidapi.com"
    }
    api_client = RapidAPIClient(api_key=rapid_api_key)
    response = api_client.call_api(api_url, method='GET', params=api_params , headers_extra=headers)
    return response
