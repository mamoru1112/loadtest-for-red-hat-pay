# Locust のインストール
* OpenShift クラスタへのログイン
* Locust インストールスクリプトの実行
```
./install-locust.sh
```

* Locust へのアクセス URL の確認
以下のコマンドを実行した取得した URL をブラウザから開く。
```
echo http://$(oc get route app --template={{.spec.host}})
```

# テストスクリプト・ターゲットホストの変更方法

TBD

