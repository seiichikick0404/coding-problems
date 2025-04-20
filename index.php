<?php

// 値オブジェクト: ItemId
class ItemId {
    private int $value;

    public function __construct(int $itemId) {
        if ($itemId <= 0) {
            throw new InvalidArgumentException("ItemId must be a positive integer.");
        }
        $this->value = $itemId;
    }

    public function getValue(): int {
        return $this->value;
    }
}

// 値オブジェクト: ItemName
class ItemName {
    private string $value;

    public function __construct(string $itemName) {
        if (empty(trim($itemName))) {
            throw new InvalidArgumentException("ItemName cannot be empty.");
        }
        $this->value = $itemName;
    }

    public function getValue(): string {
        return $this->value;
    }
}

// エンティティ: Item
class Item {
    private ItemId $id;
    private ItemName $name;

    public function __construct(ItemId $id, ItemName $name) {
        $this->id = $id;
        $this->name = $name;
    }

    public function getId(): ItemId {
        return $this->id;
    }

    public function getName(): ItemName {
        return $this->name;
    }
}

// データソース（模倣）
class ItemRepository {
    private array $items = [];

    public function save(Item $item): void {
        $this->items[$item->getId()->getValue()] = $item;
    }

    public function findById(ItemId $id): ?Item {
        return $this->items[$id->getValue()] ?? null;
    }

    public function findByName(ItemName $name): ?Item {
        foreach ($this->items as $item) {
            if ($item->getName()->getValue() === $name->getValue()) {
                return $item;
            }
        }
        return null;
    }
}

// ドメインサービス: ItemService
class ItemService {
    private ItemRepository $repository;

    public function __construct(ItemRepository $repository) {
        $this->repository = $repository;
    }

    public function isDuplicate(ItemName $name): bool {
        return $this->repository->findByName($name) !== null;
    }
}

// アプリケーションサービス
class ItemApplicationService {
    private ItemRepository $repository;
    private ItemService $checker;

    public function __construct(ItemRepository $repository, ItemService $checker) {
        $this->repository = $repository;
        $this->checker = $checker;
    }

    public function createItem(int $id, string $name): void {
        $itemName = new ItemName($name);

        if ($this->checker->isDuplicate($itemName)) {
            throw new RuntimeException("Item with the same name already exists.");
        }

        $item = new Item(new ItemId($id), $itemName);
        $this->repository->save($item);
    }

    public function getItemById(int $id): ?Item {
        return $this->repository->findById(new ItemId($id));
    }
}

// 利用例
$repository = new ItemRepository();
$checker = new ItemService($repository);
$service = new ItemApplicationService($repository, $checker);

try {
    // 登録処理
    $service->createItem(1, "Item A");
    $service->createItem(2, "Item B");
    $service->createItem(3, "Item A"); // 重複エラー
} catch (RuntimeException $e) {
    echo $e->getMessage() . PHP_EOL; // Output: Item with the same name already exists.
}

// 登録済みのアイテムを取得
$item = $service->getItemById(1);
if ($item) {
    echo "Item ID: " . $item->getId()->getValue() . ", Name: " . $item->getName()->getValue() . PHP_EOL;
}
