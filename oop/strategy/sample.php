<?php

interface ECInterface {
    public function getOrders();

    public function getItems();
}

class AmazonStrategy implements ECInterface {
    public function getOrders()
    {
        print("Amazonの注文を取得しました。");
    }

    public function getItems()
    {
        print("Amazonの商品を取得しました。");
    }
}

class YahooStrategy implements ECInterface {
    public function getOrders()
    {
        print("Yahooの注文を取得しました。");
    }

    public function getItems()
    {
        print("Yahooの商品を取得しました。");
    }
}

class Context {
    public ECInterface $strategy;

    public function __construct(ECInterface $strategy)
    {
        $this->strategy = $strategy;
    }

    public function getOrders()
    {
        $this->strategy->getOrders();
    }

    public function getItems()
    {
        $this->strategy->getItems();
    }
}


$context = new Context(new YahooStrategy());
$context->getOrders();