# Locust のインストール

* OpenShift クラスタへのログイン

* Locust インストールスクリプトの実行
```
./install-locust.sh
```

* Locust へのアクセス URL の確認

以下のコマンドを実行して取得した URL をブラウザから開く。
```
echo http://$(oc get route app --template={{.spec.host}})
```

# テストスクリプト・ターゲットホストの変更方法

* テストスクリプトの編集 (locustfile.py)

* テストスクリプト・ターゲットホストの変更

以下のコマンドを実行し、Locust Pod から読み込まれる ConfigMap の値を変更する。
```
./seed.sh locustfile.py (ターゲットホスト名)

# コマンド実行例
# ./seed.sh locustfile.py https://echo-api.3scale.net:443
```



