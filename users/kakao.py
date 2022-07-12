import requests

class KakaoAPI:
    def __init__(self, kakao_token):
        self.kakao_token = kakao_token
        self.user_url    = 'https://kapi.kakao.com/v2/user/me'

    def kakao_user(self):
        headers     = {'Authorization' : f'{self.kakao_token}'}
        response = requests.get(self.user_url, headers=headers, timeout=3).json()
        
        return response