<?php

interface Monster {
    public function attack();
}


class MonsterA {
    public function attack()
    {
        print('100ダメージを与えた');
    }
}


class MonsterB {
    public function attack()
    {
        print('1000ダメージを与えた');
    }
}

class MonsterC {
    public function attack()
    {
        print('2000ダメージを与えた');
    }
}


$monsters = [new MonsterA(), new MonsterB(), new MonsterC()];

foreach ($monsters as $monster) { 
    print($monster->attack());
}