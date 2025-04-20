<?php
class Warehouse {
    private int $quantity;

    public function __construct(int $quantity)
    {
        // 在庫数をセット
        $this->quantity = $quantity;
    }

    public function shipment()
    {
        $this->removeInventory();

        // 実行結果をtrue or falseで返却
    }

    public function getQuantity(): int
    {
        return $this->quantity;
    }

    private function removeInventory()
    {
        // 在庫を減らす処理
    }

}

class WarehouseTest extends TestCase {
    public function testShipment() {
        // 準備
        $sut = new Warehouse(10); // 倉庫に在庫を10件セット

        // 実行
        $sut->shipment(); // 出荷処理を実行

        // 確認
        $this->assertEquals(9, $sut->getQuantity()); // 在庫数が9になっているか
    }

}

// 悪いテスト
use PHPUnit\Framework\TestCase;

class LogisticsCenterTest extends TestCase {
    public function testShipItemImplementationDetails() {
        $inventory = ['itemA' => 10];
        $logisticsCenter = new LogisticsCenter($inventory);

        // 実装の詳細に依存（在庫数を直接確認）
        $reflection = new ReflectionClass($logisticsCenter);
        $property = $reflection->getProperty('inventory');
        $property->setAccessible(true);

        // 出荷後の在庫数を直接確認
        $logisticsCenter->shipItem('itemA', 5);
        $this->assertEquals(['itemA' => 5], $property->getValue($logisticsCenter)); // 悪い例
    }
}