<?php

function main ($argc, $argv) {
  $accessToken = $argv[0];
  $keyword = $argv[1];
  $url = 'https://challenge-server.tracks.run/hotel-reservation/hotels'; // エンドポイントURL

  // URLにクエリパラメータを追加
  $queryParams = http_build_query(['keyword' => $keyword]);
  $requestUrl = "{$url}?{$queryParams}";

  // cURLの初期化
  $ch = curl_init();

  // cURLオプションの設定
  curl_setopt($ch, CURLOPT_URL, $requestUrl);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, [
      "X-ACCESS-TOKEN: $accessToken"
  ]);

  // APIのレスポンスを取得
  $response = curl_exec($ch);
  curl_close($ch);

  // レスポンスをJSONとしてデコード
  $data = json_decode($response, true);

  foreach($data as $hotel) {
    echo $hotel['name'] . "\n";
  }
}

main($argc - 1, array_slice($argv, 1));
