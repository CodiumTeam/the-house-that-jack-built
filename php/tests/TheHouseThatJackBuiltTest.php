<?php

namespace TheHouseThatJackBuilt\Test;

use PHPUnit\Framework\TestCase;
use TheHouseThatJackBuilt\TheHouseThatJackBuilt;

class TheHouseThatJackBuiltTest extends TestCase
{
    /** @test */
    public function verses_are_ok(): void
    {
        $song = (new TheHouseThatJackBuilt())->song();

        self::assertIsArray($song);
    }
}