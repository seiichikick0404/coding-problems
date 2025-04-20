import sys
import requests

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <accessToken> <keyword>")
        sys.exit(1)

    access_token = sys.argv[1]
    keyword = sys.argv[2]
    url = 'https://challenge-server.tracks.run/hotel-reservation/hotels'  # エンドポイントURL

    # URLにクエリパラメータを追加
    params = {'keyword': keyword}
    headers = {'X-ACCESS-TOKEN': access_token}

    try:
        # APIリクエストを送信
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # エラーが発生した場合に例外を発生させる

        # レスポンスをJSONとしてデコード
        data = response.json()

        # ホテル名を表示
        for hotel in data:
            print(hotel['name'])

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
